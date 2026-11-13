# Prix package séjour casher — CouponKasher

Généré par `pipeline/pricing.py` à partir du run vol (Kiwi.com) + hôtel (Booking.com).
Ne pas éditer à la main — le prochain run écrase ce fichier.

- **Run** : 2026-11-13 (run quotidien package vol+hotel Groupe A S1-S8 — declenche par Jacques le 13/11/2026. Dernier run : 2026-09-15.)
- **Schéma** : 3 nuits / 4 jours, depart dimanche ou lundi -> retour mercredi ou jeudi, jamais vendredi ni samedi. Fenetre S1-S8 : S1 15/11, S2 22/11, S3 29/11, S4 06/12, S5 13/12, S6 20/12, S7 27/12, S8 03/01/2027.
- **Taux appliqué** : 1 USD = 3.05 ILS · marge 15 % · formule `(vol + hôtel/pers) ÷ 0.85 × 3.05`
- **Généré le** : 2026-11-13 05:10 UTC

> **Calendrier** — Hanoucca 5787 : 4-12 decembre 2026 (S4-S5), vacances scolaires en Israel, demande interieure forte. Nouvel an civil : S7-S8 — les tarifs hoteliers de Venise, Budapest et Paphos portent la prime du 31/12, les vols au contraire y sont au plus bas. Aucune fermeture d'aeroport dans la fenetre. Israel est a l'heure d'hiver sur toute la periode : la limite d'atterrissage du vendredi est 11h00, pas 14h00.

## À publier — meilleur prix par destination

| Destination | Meilleur ₪ | Semaine | Publié ₪ | Écart | Décision |
|---|---|---|---|---|---|
| Paphos — WellClub (PFO) | 1290 | S7 | 1270 | +2 % | publiable |
| Paphos — Brown Hills (PFO) | 1300 | S7 | 1850 | -30 % | ⚠️ hors seuil — arbitrage Jacques |
| Tbilissi (TBS) | 1630 | S2 | 2090 | -22 % | ⚠️ hors seuil — arbitrage Jacques |
| Budapest (BUD) | 1660 | S8 | 1380 | +20 % | ⚠️ hors seuil — arbitrage Jacques |
| Amsterdam (AMS) | 1850 | S3 | 2610 | -29 % | ⚠️ hors seuil — arbitrage Jacques |
| Londres (LON) | 2240 | S6 | 2110 | +6 % | publiable |
| Vienne (VIE) | 2300 | S8 | 1930 | +19 % | ⚠️ hors seuil — arbitrage Jacques |
| Venise (VCE) | 3550 | S7 | — | — | ⛔ cacherout à trancher — ne pas publier |
| Prague (PRG) | 3930 | S1 | 2690 | +46 % | ⚠️ hors seuil — arbitrage Jacques |

## Détail S1

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Prague (PRG) | Kosher Hotel King David Prague | 2026-11-16 · lundi | 252 | 844.38 | 3930 | ok · Vol direct 0 escale, retour hors vendredi/samedi. Hotel teste aussi en S2 (22-25/11) a 1979,80 $ : la S1 reste la moins chere. Le King David est structurellement cher cet hiver. |

## Détail S1-S8

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budva (TIV) | Harmonia by Dukley | — | — | — | — | gap vol · Aucun vol direct TLV-Montenegro sur l'integralite de la fenetre 15/11-03/01, recherche sans plafond de prix. Route saisonniere d'ete : ce n'est pas un creux, c'est une absence de ligne en hiver. |

## Détail S2

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Tbilissi (TBS) | Cron Palace Kosher Tbilisi Hotel | 2026-11-23 · lundi | 208 | 248.75 | 1630 | ok · Vol direct 0 escale, retour hors vendredi/samedi. |

## Détail S3

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-11-29 · dimanche | 392 | 123.67 | 1850 | ok · Vol direct 0 escale, retour hors vendredi/samedi. Aucun direct sous 310 $ sur toute la fenetre : le vol a double depuis aout, l'hotel compense. |

## Détail S6

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Londres (LON) | Croft Court Hotel | 2026-12-20 · dimanche | 329 | 297.85 | 2240 | ok · Vol direct 0 escale. ATTENTION : l'option la moins chere de la fenetre (282 $, 23-27/11) atterrit a Tel Aviv le VENDREDI a 15h25, non conforme Shabbat en hiver (limite 11h) — ecartee. 329 $ est le premier prix conforme. Depart dimanche 21h55, arrivee lundi 01h25 : hotel du 21 au 24/12. |
| Chalkida (ATH) | Brown Beach | 2026-12-21 · lundi | 139 | — | — | gap hotel · Vol direct ATH a 139 $ disponible. Brown Beach sans aucune disponibilite sur deux fenetres testees (15-18/11 et 21-24/12) : fermeture hivernale probable, a confirmer aupres de l'hotel. |
| Londres — Pillar (LON) | Pillar Hotel | 2026-12-20 · dimanche | 329 | — | — | gap hotel · Vol conforme identique a Croft Court. Pillar Hotel non retourne par Booking sur 21-24/12 : pas de disponibilite a ces dates. |

## Détail S7

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Paphos — WellClub (PFO) | WellClub Resort - Suites & Wellness | 2026-12-28 · lundi | 130 | 230.07 | 1290 | ok · Vol direct 0 escale, retour hors vendredi/samedi. Hotel moins cher en S1 (404,37 $) mais aucun direct sous 200 $ cette semaine-la : le package S7 reste le meilleur. |
| Paphos — Brown Hills (PFO) | Paphos Hills Resort & Spa by Brown Hotels | 2026-12-28 · lundi | 130 | 233.72 | 1300 | ok · Vol direct 0 escale, retour hors vendredi/samedi. Meme tarif hotel en S1 et en S7 : c'est le vol a 130 $ qui fait le minimum. |
| Venise (VCE) | Rimon Place Kosher | 2026-12-28 · lundi | 218 | 771.45 | 3550 | ok · Vol direct 0 escale, retour hors vendredi/samedi. Kiwi n'a pas echoue sur VCE cette fois. Tarif hotel du Nouvel An. Publication bloquee : cacherout contestee. |

## Détail S8

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2027-01-03 · dimanche | 148 | 317.36 | 1660 | ok · Vol direct 0 escale, retour hors vendredi/samedi. S2 testee en contre-epreuve : hotel moins cher (595,66 $) mais vol a 173 $, package a 1680 contre 1660. Le Nouvel An coute sur l'hotel et rapporte sur le vol. |
| Vienne (VIE) | Vayalen Boutique Hotel | 2027-01-03 · dimanche | 310 | 331.55 | 2300 | ok · Vol direct 0 escale, retour hors vendredi/samedi. Vayalen complet en S2 (22-25/11), ou le vol etait a 300 $ : S8 est la seule semaine ou vol et hotel coincident. |

## Lecture

- Un écart supérieur à 15 % vs le prix publié sur couponkasher.co.il n'est **jamais** publié automatiquement : il doit être confirmé par Jacques.
- Le site affiche un prix « à partir de » (החל ב-) : la valeur publiable est donc le meilleur prix de la destination sur la fenêtre, toutes semaines confondues.
- Un vol est retenu uniquement s'il est **direct** (0 escale) et hors samedi. Pas de vol direct le dimanche → repli sur le lundi, signalé dans la colonne Départ.
- Le prix hôtel vient de Booking.com par **nom d'hôtel exact**. Si le nom retourné diffère du partenaire attendu, la ligne est écartée — le connecteur peut répondre par un hôtel homonyme situé dans un autre pays.
