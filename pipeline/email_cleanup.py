#!/usr/bin/env python3
"""Nettoyage de la boite matapiero@gmail.com : requetes, garde-fous, rapport.

Ce script ne touche JAMAIS a Gmail. Il ne sait ni archiver ni supprimer : c'est la
session Claude, avec le connecteur Gmail, qui execute. Le script fait deux choses,
et rien d'autre :

  1. il fabrique les requetes Gmail exactes a partir de pipeline/email_rules.json,
     protections comprises, pour qu'aucune requete ne soit improvisee a la main ;
  2. il relit le releve d'un run et refuse celui-ci si un thread protege s'y est
     glisse, avant que la moindre suppression ne soit faite.

    python3 pipeline/email_cleanup.py --requetes
    python3 pipeline/email_cleanup.py Data/email-runs/run-2026-08-26.json
"""
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REGLES = RACINE / "pipeline" / "email_rules.json"

# Les deux etages du nettoyage. Nommes ici une fois pour toutes : le prompt de la
# Routine, le releve de run et le rapport parlent tous le meme vocabulaire.
ARCHIVE = "archive"
CORBEILLE = "corbeille"

ACTIONS = {
    "archive_puis_corbeille": (ARCHIVE, CORBEILLE),
    "archive_seulement": (ARCHIVE,),
}


def charger(chemin):
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def requete(regle, etage, parametres, protection):
    """Requete Gmail d'une regle a un etage donne, protections incluses."""
    expediteurs = " OR ".join("from:%s" % a for a in regle["expediteurs"])
    jours = (parametres["jours_avant_archive"] if etage == ARCHIVE
             else parametres["jours_avant_corbeille"])

    morceaux = ["{%s}" % expediteurs, "older_than:%dd" % jours]
    # L'archivage se fait sur la boite de reception ; la corbeille frappe aussi
    # ce qui a deja ete archive par un run precedent (donc sans in:inbox).
    if etage == ARCHIVE:
        morceaux.append("in:inbox")
    else:
        morceaux.append("-in:trash")
    morceaux.extend(protection["conditions_gmail"])
    if etage == CORBEILLE:
        morceaux.extend(protection["conditions_gmail_corbeille"])
    return " ".join(morceaux)


def plan(donnees):
    """Toutes les requetes a executer, dans l'ordre du run."""
    parametres, protection = donnees["parametres"], donnees["protection"]
    lignes = []
    for regle in donnees["regles"]:
        for etage in ACTIONS[regle["action"]]:
            lignes.append({
                "id": regle["id"],
                "libelle": regle["libelle"],
                "etage": etage,
                "requete": requete(regle, etage, parametres, protection),
            })
    return lignes


def domaine(adresse):
    return adresse.rsplit("@", 1)[-1].lower() if "@" in adresse else ""


def motif_protection(thread, protection):
    """Pourquoi ce thread doit etre ecarte, ou None s'il peut etre traite."""
    expediteur = (thread.get("expediteur") or "").strip().lower()
    if expediteur in {a.lower() for a in protection["expediteurs"]}:
        return "expediteur protege"
    if domaine(expediteur) in {d.lower() for d in protection["domaines"]}:
        return "domaine protege (%s)" % domaine(expediteur)
    sujet = (thread.get("sujet") or "").lower()
    for mot in protection["mots_cles_sujet"]:
        if mot.lower() in sujet:
            return "mot-cle sujet : %s" % mot
    return None


def verifier(releve, donnees):
    """Relit un releve de run. Renvoie (traites, ecartes, anomalies)."""
    index = {r["id"]: r for r in donnees["regles"]}
    protection = donnees["protection"]
    plafond = donnees["parametres"]["plafond_threads_par_run"]

    traites, ecartes, anomalies = [], [], []
    for bloc in releve["regles"]:
        regle = index.get(bloc["id"])
        if regle is None:
            anomalies.append("regle inconnue dans email_rules.json : %s" % bloc["id"])
            continue
        etage = bloc["etage"]
        if etage not in ACTIONS[regle["action"]]:
            anomalies.append(
                "%s : etage '%s' interdit — la regle est en '%s'"
                % (bloc["id"], etage, regle["action"]))
            continue
        for thread in bloc.get("threads", []):
            ligne = dict(thread, regle=bloc["id"], etage=etage)
            motif = motif_protection(thread, protection)
            if motif:
                ligne["motif"] = motif
                ecartes.append(ligne)
            else:
                traites.append(ligne)

    if releve.get("mode") != "blanc" and len(traites) > plafond:
        anomalies.append(
            "plafond depasse : %d threads a traiter pour un maximum de %d — "
            "scinder le rattrapage sur plusieurs runs, ou passer au plafond de "
            "rattrapage sur demande explicite de Jacques" % (len(traites), plafond))
    return traites, ecartes, anomalies


def rapport(releve, traites, ecartes, anomalies, donnees):
    date = releve.get("date", "?")
    mode = releve.get("mode", "?")
    par_regle = Counter((l["regle"], l["etage"]) for l in traites)
    par_expediteur = Counter(l.get("expediteur", "?") for l in traites)
    libelles = {r["id"]: r["libelle"] for r in donnees["regles"]}

    out = ["# Nettoyage des emails — run %s (mode : %s)" % (date, mode), ""]
    if mode == "blanc":
        out.append("Run **a blanc** : rien n'a ete archive ni supprime. "
                   "Ce rapport dit ce qui *serait* fait.")
        out.append("")

    out.append("## Ce qui serait traite" if mode == "blanc" else "## Ce qui a ete traite")
    out.append("")
    estimes = {(b["id"], b["etage"]): b for b in releve["regles"]}
    plafonnee = any(b.get("estimation_plafonnee") for b in releve["regles"])

    out.append("| Regle | Etage | Volume dans la boite | Threads releves |")
    out.append("|---|---|---|---|")
    for (rid, etage), n in sorted(par_regle.items(), key=lambda kv: -kv[1]):
        bloc = estimes.get((rid, etage), {})
        volume = bloc.get("total_estime", "?")
        if bloc.get("estimation_plafonnee"):
            volume = "> %s" % volume
        out.append("| %s | %s | %s | %d |"
                   % (libelles.get(rid, rid), etage, volume, n))
    out.append("| **Total** | | | **%d** |" % len(traites))
    out.append("")
    if plafonnee:
        out.append("> Les volumes marques `>` sont plafonnes par l'API Gmail, qui cesse "
                   "de compter au-dela de 200 threads. Le vrai volume est superieur, "
                   "parfois de beaucoup.")
        out.append("")

    if par_expediteur:
        out.append("## Par expediteur")
        out.append("")
        out.append("| Expediteur | Threads |")
        out.append("|---|---|")
        for adresse, n in par_expediteur.most_common(20):
            out.append("| %s | %d |" % (adresse, n))
        out.append("")

    out.append("## Ecartes par les protections")
    out.append("")
    if ecartes:
        out.append("Ces threads matchaient une regle mais ont ete retenus. "
                   "**Ils restent en place.**")
        out.append("")
        out.append("| Expediteur | Sujet | Motif |")
        out.append("|---|---|---|")
        for l in ecartes[:40]:
            sujet = (l.get("sujet") or "").replace("|", "/")[:70]
            out.append("| %s | %s | %s |" % (l.get("expediteur", "?"), sujet, l["motif"]))
        if len(ecartes) > 40:
            out.append("")
            out.append("_(%d ecartes au total, 40 affiches)_" % len(ecartes))
    else:
        out.append("Aucun. Aucun thread protege n'a ete remonte par les requetes.")
    out.append("")

    if anomalies:
        out.append("## Anomalies — run a ne pas appliquer en l'etat")
        out.append("")
        for a in anomalies:
            out.append("- %s" % a)
        out.append("")

    out.append("---")
    out.append("")
    out.append("_Genere par `pipeline/email_cleanup.py` le %s._"
               % datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"))
    return "\n".join(out) + "\n"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    donnees = charger(REGLES)

    if sys.argv[1] == "--requetes":
        for ligne in plan(donnees):
            print("# %-24s %s" % (ligne["id"], ligne["etage"]))
            print(ligne["requete"])
            print()
        return 0

    releve = charger(sys.argv[1])
    traites, ecartes, anomalies = verifier(releve, donnees)

    (RACINE / "Data" / "email-cleanup.md").write_text(
        rapport(releve, traites, ecartes, anomalies, donnees), encoding="utf-8")
    (RACINE / "Data" / "email-cleanup.json").write_text(
        json.dumps({"date": releve.get("date"), "mode": releve.get("mode"),
                    "traites": traites, "ecartes": ecartes, "anomalies": anomalies},
                   ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("%d threads a traiter, %d ecartes par les protections."
          % (len(traites), len(ecartes)))
    for a in anomalies:
        print("ANOMALIE : %s" % a)
    if anomalies and releve.get("mode") != "blanc":
        print("Run refuse : corriger les anomalies avant d'appliquer quoi que ce soit.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
