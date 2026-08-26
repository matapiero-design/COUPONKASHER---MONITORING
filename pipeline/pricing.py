#!/usr/bin/env python3
"""Calcule le prix package CouponKasher a partir d'un run brut vol (Kiwi) + hotel (Booking).

Entree  : pipeline/destinations.json + Data/runs/run-<date>.json
Sortie  : Data/package-prices.json (machine) et Data/package-prices.md (lisible)
          + signalement des ecarts > SEUIL_ECART vs les prix actuellement publies
            dans site/prices.json.

Ce script ne publie rien : il ne touche jamais a site/prices.json ni a site/index.html.
La publication reste une decision de Jacques (voir README).

    python3 pipeline/pricing.py Data/runs/run-2026-08-25.json
"""
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# --- Parametres metier -------------------------------------------------------
# Le taux et la marge sont la propriete de Jacques : ne jamais les changer sans
# demande explicite de sa part (regle reprise du skill dashboard-suivi-prix).
TAUX_USD_ILS = 3.05   # 1 USD = 3.05 ILS, taux fixe du business (PAS le taux du jour).
                      # Confirme par Jacques le 25/08/2026. C'est LE taux de reference :
                      # le 3.65 qui figure encore dans le skill dashboard-suivi-prix est
                      # perime (il datait d'un dollar beaucoup plus fort) et c'est lui qui
                      # explique que les prix publies sur le site soient trop hauts.
MARGE = 0.85          # 15 % de marge integree : prix / 0.85
SEUIL_ECART = 0.15    # au-dela, l'ecart vs le prix publie doit etre confirme


def prix_package_ils(vol_usd, hotel_usd_pp, devise_hotel="USD"):
    """Prix par personne, arrondi a la dizaine inferieure.

    Deux formules, et il ne faut surtout pas les confondre :

      etranger  (vol + hotel/pers en $) / 0.85 x 3.05
      Israel    (hotel/pers en ILS) / 0.85          — pas de vol, pas de conversion

    Appliquer le taux a un prix deja libelle en shekels le multiplierait par
    trois. C'est le piege principal de l'offre domestique.
    """
    if devise_hotel == "ILS":
        brut = hotel_usd_pp / MARGE          # deja en ILS, aucune conversion
    else:
        brut = (vol_usd + hotel_usd_pp) / MARGE * TAUX_USD_ILS
    return int(math.floor(brut / 10) * 10)


def charger(chemin):
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def construire(run, destinations, publies):
    # Les destinations hors Booking ont quand meme un vol a chiffrer.
    index = {d["cle_site"]: d
             for liste in ("groupe_a", "groupe_b", "groupe_israel", "hors_booking")
             for d in destinations.get(liste, [])}
    lignes = []
    for entree in run["destinations"]:
        cle = entree["cle_site"]
        dest = index[cle]
        ligne = {
            "cle_site": cle,
            "semaine": entree.get("semaine", "S1"),
            "ville": dest["ville"],
            "iata": dest["iata"],
            "hotel": entree.get("hotel_trouve") or dest.get("booking_name") or dest.get("hotel", "—"),
            "depart": entree.get("depart"),
            "retour": entree.get("retour"),
            "jour_depart": entree.get("jour_depart"),
            "vol_usd": entree.get("vol_usd"),
            "hotel_total_usd": entree.get("hotel_total_usd"),
            "statut": entree.get("statut", "ok"),
            # Une cacherout non tranchee interdit la publication, quel que soit l'ecart.
            "cacherout_bloquee": bool(dest.get("certification")),
            "note": entree.get("note", ""),
        }
        if ligne["hotel_total_usd"] is not None:
            # Booking renvoie le total du sejour pour 2 adultes ; le site affiche un prix par personne.
            ligne["hotel_usd_pp"] = round(ligne["hotel_total_usd"] / 2, 2)
        else:
            ligne["hotel_usd_pp"] = None

        devise = dest.get("devise_hotel", "USD")
        ligne["devise_hotel"] = devise
        ligne["sans_vol"] = bool(dest.get("sans_vol"))
        if devise == "ILS" and ligne["hotel_usd_pp"] is not None:
            # Sejour domestique : l'hotel seul suffit, il n'y a pas de vol a attendre.
            ligne["prix_ils"] = prix_package_ils(None, ligne["hotel_usd_pp"], "ILS")
        elif ligne["vol_usd"] is not None and ligne["hotel_usd_pp"] is not None:
            ligne["prix_ils"] = prix_package_ils(ligne["vol_usd"], ligne["hotel_usd_pp"])
        else:
            ligne["prix_ils"] = None
            ligne["statut"] = ligne["statut"] if ligne["statut"] != "ok" else "incomplet"

        ligne["prix_publie_ils"] = (publies.get("prices") or {}).get(cle, {}).get("price_ils")
        lignes.append(ligne)

    # Le site affiche un prix "à partir de" : la référence d'une destination est donc son
    # meilleur prix sur la fenêtre, pas celui d'une semaine en particulier.
    meilleurs = {}
    for l in lignes:
        if l["prix_ils"] is not None:
            actuel = meilleurs.get(l["cle_site"])
            if actuel is None or l["prix_ils"] < actuel:
                meilleurs[l["cle_site"]] = l["prix_ils"]
    for l in lignes:
        l["meilleur_ils"] = meilleurs.get(l["cle_site"])
        publie, meilleur = l["prix_publie_ils"], l["meilleur_ils"]
        if publie and meilleur:
            l["ecart"] = round((meilleur - publie) / publie, 4)
            l["a_confirmer"] = abs(l["ecart"]) > SEUIL_ECART
        else:
            l["ecart"] = None
            l["a_confirmer"] = False
    return lignes


def rendre_markdown(run, lignes):
    def cel(v, vide="—"):
        return vide if v is None else v

    semaines = sorted({l["semaine"] for l in lignes})
    out = [
        "# Prix package séjour casher — CouponKasher",
        "",
        "Généré par `pipeline/pricing.py` à partir du run vol (Kiwi.com) + hôtel (Booking.com).",
        "Ne pas éditer à la main — le prochain run écrase ce fichier.",
        "",
        f"- **Run** : {run['run_id']} ({run['motif']})",
        f"- **Schéma** : {run['schema']}",
        f"- **Taux appliqué** : 1 USD = {TAUX_USD_ILS} ILS · marge {int((1 - MARGE) * 100)} %"
        f" · formule `(vol + hôtel/pers) ÷ {MARGE} × {TAUX_USD_ILS}`",
        f"- **Généré le** : {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC",
    ]
    if run.get("alerte_calendrier"):
        out += ["", f"> **Calendrier** — {run['alerte_calendrier']}"]

    # Vue de publication : le site affiche "à partir de", donc le meilleur prix de la fenêtre.
    out += [
        "",
        "## À publier — meilleur prix par destination",
        "",
        "| Destination | Meilleur ₪ | Semaine | Publié ₪ | Écart | Décision |",
        "|---|---|---|---|---|---|",
    ]
    vus = set()
    for l in sorted(lignes, key=lambda x: (x["meilleur_ils"] is None, x["meilleur_ils"] or 0)):
        if l["cle_site"] in vus or l["meilleur_ils"] is None:
            continue
        vus.add(l["cle_site"])
        semaine = next(x["semaine"] for x in lignes if x["cle_site"] == l["cle_site"]
                       and x["prix_ils"] == l["meilleur_ils"])
        ecart = f"{l['ecart'] * 100:+.0f} %" if l["ecart"] is not None else "—"
        if l["cacherout_bloquee"]:
            decision = "⛔ cacherout à trancher — ne pas publier"
        elif l["a_confirmer"]:
            decision = "⚠️ hors seuil — arbitrage Jacques"
        elif l["prix_publie_ils"] is None:
            decision = "pas de prix affiché sur le site"
        else:
            decision = "publiable"
        out.append(f"| {l['ville']} ({l['iata']}) | {l['meilleur_ils']} | {semaine} | "
                   f"{cel(l['prix_publie_ils'])} | {ecart} | {decision} |")

    for sem in semaines:
        out += [
            "",
            f"## Détail {sem}",
            "",
            "| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |",
            "|---|---|---|---|---|---|---|",
        ]
        for l in sorted((x for x in lignes if x["semaine"] == sem),
                        key=lambda x: (x["prix_ils"] is None, x["prix_ils"] or 0)):
            jour = f" · {l['jour_depart']}" if l["jour_depart"] else ""
            statut = l["statut"] + (f" · {l['note']}" if l["note"] else "")
            out.append(f"| {l['ville']} ({l['iata']}) | {l['hotel']} | {cel(l['depart'])}{jour} | "
                       f"{cel(l['vol_usd'])} | {cel(l['hotel_usd_pp'])} | {cel(l['prix_ils'])} | {statut} |")

    out += [
        "",
        "## Lecture",
        "",
        f"- Un écart supérieur à {int(SEUIL_ECART * 100)} % vs le prix publié sur couponkasher.co.il "
        "n'est **jamais** publié automatiquement : il doit être confirmé par Jacques.",
        "- Le site affiche un prix « à partir de » (החל ב-) : la valeur publiable est donc le meilleur "
        "prix de la destination sur la fenêtre, toutes semaines confondues.",
        "- Un vol est retenu uniquement s'il est **direct** (0 escale) et hors samedi. "
        "Pas de vol direct le dimanche → repli sur le lundi, signalé dans la colonne Départ.",
        "- Le prix hôtel vient de Booking.com par **nom d'hôtel exact**. Si le nom retourné diffère du "
        "partenaire attendu, la ligne est écartée — le connecteur peut répondre par un hôtel homonyme "
        "situé dans un autre pays.",
        "",
    ]
    return "\n".join(out)


def main():
    chemin_run = sys.argv[1] if len(sys.argv) > 1 else None
    if not chemin_run:
        sys.exit("usage: pricing.py Data/runs/run-<date>.json")

    run = charger(chemin_run)
    destinations = charger(RACINE / "pipeline" / "destinations.json")
    chemin_publies = RACINE / "site" / "prices.json"
    publies = charger(chemin_publies) if chemin_publies.exists() else {}

    lignes = construire(run, destinations, publies)

    sortie_json = {
        "run_id": run["run_id"],
        "schema": run["schema"],
        "fx_usd_ils": TAUX_USD_ILS,
        "marge": MARGE,
        "genere_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "destinations": lignes,
    }
    (RACINE / "Data" / "package-prices.json").write_text(
        json.dumps(sortie_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (RACINE / "Data" / "package-prices.md").write_text(
        rendre_markdown(run, lignes), encoding="utf-8"
    )

    a_confirmer = [l["ville"] for l in lignes if l["a_confirmer"] and not l["cacherout_bloquee"]]
    bloquees = sorted({l["ville"] for l in lignes if l["cacherout_bloquee"]})
    incomplets = [l["ville"] for l in lignes if l["prix_ils"] is None]
    print(f"{len(lignes)} destinations traitées.")
    if incomplets:
        print("Incomplètes (gap vol ou hôtel) : " + ", ".join(incomplets))
    if bloquees:
        print("Cacherout à trancher, publication bloquée : " + ", ".join(bloquees))
    if a_confirmer:
        print(f"Écart > {int(SEUIL_ECART * 100)} % vs le site — à confirmer : " + ", ".join(a_confirmer))


if __name__ == "__main__":
    main()
