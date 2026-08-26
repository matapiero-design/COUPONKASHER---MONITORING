# Prix package séjour casher — CouponKasher

Généré par `pipeline/pricing.py` à partir du run vol (Kiwi.com) + hôtel (Booking.com).
Ne pas éditer à la main — le prochain run écrase ce fichier.

- **Run** : 2026-08-25 (premier run package vol+hotel — validation de bout en bout du branchement Kiwi.com + Booking.com)
- **Schéma** : 3 nuits / 4 jours, depart dimanche -> retour mercredi (repli lundi -> jeudi si pas de direct le dimanche). Fenetre S1-S8 : S1 30/08, S2 06/09, S3 13/09, S4 20/09, S5 27/09, S6 04/10, S7 11/10, S8 18/10.
- **Taux appliqué** : 1 USD = 3.05 ILS · marge 15 % · formule `(vol + hôtel/pers) ÷ 0.85 × 3.05`
- **Généré le** : 2026-08-26 03:20 UTC

> **Calendrier** — Roch Hachana 5787 : vendredi 11/09 au soir -> dimanche 13/09 au soir. Le depart dominical de S3 (13/09) tombe en plein Yom Tov : repli lundi 14/09. Yom Kippour : dimanche 20/09 au soir -> lundi 21/09 au soir. Le depart de S4 tombe a l'entree de Kippour et le lundi est Kippour lui-meme : S4 est inexploitable, ni dimanche ni lundi. Souccot : 25/09 au soir -> 02/10 au soir, Sim'hat Torah en Israel jusqu'au 03/10 au soir. S5 (27/09) est en 'hol hamoed : vendable mais en pic de demande israelienne. S6 a S8 (04/10, 11/10, 18/10) sont le creux post-fetes — c'est la que les prix s'effondrent.

## À publier — meilleur prix par destination

| Destination | Meilleur ₪ | Semaine | Publié ₪ | Écart | Décision |
|---|---|---|---|---|---|
| Budapest (BUD) | 1390 | S8 | 1740 | -20 % | ⚠️ hors seuil — arbitrage Jacques |
| Paphos (PFO) | 1720 | S7 | 1720 | +0 % | publiable |
| Amsterdam (AMS) | 1900 | S1 | 1900 | +0 % | publiable |
| Chalkida (ATH) | 1920 | S1 | 1920 | +0 % | publiable |
| Tbilissi (TBS) | 2000 | S8 | 2970 | -33 % | ⚠️ hors seuil — arbitrage Jacques |
| Paphos (PFO) | 2360 | S7 | 2820 | -16 % | ⚠️ hors seuil — arbitrage Jacques |
| Vienne (VIE) | 2520 | S1 | 2520 | +0 % | publiable |
| Budva (TIV) | 2580 | S8 | 3850 | -33 % | ⚠️ hors seuil — arbitrage Jacques |
| Londres (LON) | 2660 | S6 | 3630 | -27 % | ⚠️ hors seuil — arbitrage Jacques |
| Prague (PRG) | 3260 | S2 | 3260 | +0 % | publiable |
| Venise (VCE) | 3990 | S1 | 3675 | +9 % | ⛔ cacherout à trancher — ne pas publier |

## Détail S1

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-08-30 · dimanche | 236 | 250.14 | 1740 | ok · nom Booking retourne = 'Hotel & Residence, Palace Quarter' alors que la reference dit 'Hotel & Apartments' — a confirmer par Jacques |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-08-30 · dimanche | 401 | 128.62 | 1900 | ok · vol Blue Bird A/R, 0 escale |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-08-30 · dimanche | 160 | 377.84 | 1920 | ok · vol Israir aller / Blue Bird retour, 0 escale |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-08-30 · dimanche | 364 | 340.68 | 2520 | ok · vol Blue Bird A/R, 0 escale |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-08-31 · lundi (repli) | 543 | 285.99 | 2970 | ok · aucun vol direct le dimanche 30/08 — repli lundi applique, hotel re-interroge sur les memes dates decalees |
| Paphos (PFO) | Paphos Hills Resort & Spa by Brown Hotels | 2026-08-30 · dimanche | 166 | 809.03 | 3490 | ok · hotel a 270 $/nuit pour 2 en pic d'aout |
| Londres (LON) | Croft Court Hotel | 2026-08-30 · dimanche | 829 | 185.02 | 3630 | ok · Arkia TLV-STN A/R, 0 escale. Kiwi ne renvoie AUCUN direct sur LHR : les directs TLV-Londres passent par Stansted, Luton et Gatwick. Interroger la ville et non LHR, sinon faux gap. Croft Court est a Golders Green, donc STN/LTN conviennent |
| Budva (TIV) | Hotel Harmonia by Dukley | 2026-08-30 · dimanche | 515 | 559.97 | 3850 | ok · Israir TLV-TIV A/R, 0 escale. Le direct est sur Tivat, pas Podgorica (TGD) |
| Venise (VCE) | Rimon Place Kosher | 2026-08-30 · dimanche | 687 | 426.55 | 3990 | certification a trancher · El Al A/R 0 escale, hotel dispo. Prix NON publie : statut cacherout contradictoire entre le master portfolio (Tier 3) et la reference promo (mehadrin) |
| Prague (PRG) | Kosher Hotel King David Prague | 2026-08-30 · dimanche | 456 | 1013.19 | 5270 | ok · hotel a 675 $/nuit pour 2 en pic d'aout — c'est lui qui fait exploser le package, pas le vol |
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-08-30 · dimanche | 166 | — | — | gap hotel · Booking: WellClub Resort complet sur ces dates (hotel_names_no_availability). Vol OK a 166 $ — c'est l'hotel qui bloque |
| Paphos (PFO) | Greek Village Hotel | 2026-08-30 · dimanche | 166 | — | — | gap hotel · Booking: aucune disponibilite sur ces dates (hotel_names_no_availability) |
| Rome (FCO) | NEMAN Maison | 2026-08-30 · dimanche | 359 | — | — | gap hotel · Wizz Air A/R 0 escale. NEMAN Maison est hors Booking.com : prix hotel a fournir par Jacques |

## Détail S2

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-09-06 · dimanche | 171 | 384.5 | 1990 | ok · l'hotel complet en S1 est disponible en S2 |
| Paphos (PFO) | Paphos Hills Resort & Spa by Brown Hotels | 2026-09-06 · dimanche | 171 | 615.09 | 2820 | ok · 1230 $ contre 1618 $ en S1 — meme effet de pic d'aout que Prague |
| Prague (PRG) | Kosher Hotel King David Prague | 2026-09-06 · dimanche | 359 | 550.05 | 3260 | ok · TUS Airways A/R 0 escale. Hotel a 1100 $ contre 2026 $ une semaine plus tot : le +79 % de S1 etait bien le pic d'aout, pas un prix structurel |
| Paphos (PFO) | Greek Village Hotel | 2026-09-06 · dimanche | 171 | — | — | faux match Booking · PIEGE REPRODUCTIBLE : Booking repond 'Filerimos Village Hotel' a Ialyssos (Rhodes, GRECE) meme avec destination='Paphos, Cyprus' en contexte. Teste deux fois, meme reponse. L'hotel n'est pas atteignable par le connecteur : prix a fournir par Jacques |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-09-06 · dimanche | — | 136.82 | — | gap vol · aucun direct TLV-AMS sous 450 $ en S2 (401 $ en S1) et hotel plus cher (274 $ contre 257 $) : S1 reste le meilleur prix de la fenetre pour cette destination |

## Détail S3-S8

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Vienne (VIE) | Vayalen | — | — | — | — | pas d'amelioration · aucun vol direct sous 364 $ (le prix de S1) sur toute la fenetre S3-S8 : S1 reste le meilleur |
| Amsterdam (AMS) | ibis budget Amsterdam City South | — | — | — | — | pas d'amelioration · aucun vol direct sous 400 $ sur toute la fenetre S3-S8 : S1 reste le meilleur |
| Prague (PRG) | King David | — | — | — | — | pas d'amelioration · meilleur vol de la fenetre = 359 $ le 14/09, identique a S2 : pas d'amelioration, hotel non re-interroge |

## Détail S6

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-10-04 · dimanche | 152 | 467.49 | 2220 | ok · vol Israir 152 $ (le moins cher de la fenetre) mais hotel a 935 $ contre 756 $ en S1 : le package reste moins bon qu'en S1 |
| Londres (LON) | Croft Court Hotel | 2026-10-04 · dimanche | 437 | 306.75 | 2660 | ok · Wizz UK 437 $ contre 829 $ en S1. Aller sur Gatwick, retour sur Luton : deux aeroports differents, a valider avec le client |

## Détail S7

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-10-11 · dimanche | 151 | 329.25 | 1720 | ok · vol El Al 151 $ et hotel 658 $ : meilleur package de toute la fenetre |
| Paphos (PFO) | Paphos Hills Resort & Spa by Brown Hotels | 2026-10-11 · dimanche | 151 | 507.62 | 2360 | ok · troisieme baisse consecutive : 1618 $ en S1, 1230 $ en S2, 1015 $ en S7 |

## Détail S8

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-10-18 · dimanche | 142 | 246.94 | 1390 | ok · vol Wizz a 142 $ contre 236 $ en S1 |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-10-18 · dimanche | 291 | 267.04 | 2000 | ok · vol Israir a 291 $ contre 543 $ en S1 — la destination la plus volatile du portfolio |
| Budva (TIV) | Hotel Harmonia by Dukley | 2026-10-18 · dimanche | 345 | 374.59 | 2580 | ok · vol Israir 345 $ contre 515 $ en S1, et l'hotel passe de 1120 $ a 749 $ hors saison balneaire |
| Rome (FCO) | NEMAN Maison | 2026-10-18 · dimanche | 132 | — | — | gap hotel · vol Wizz a 132 $ contre 359 $ en S1 — le vol le moins cher de tout le portfolio. Hotel NEMAN toujours hors Booking |

## Lecture

- Un écart supérieur à 15 % vs le prix publié sur couponkasher.co.il n'est **jamais** publié automatiquement : il doit être confirmé par Jacques.
- Le site affiche un prix « à partir de » (החל ב-) : la valeur publiable est donc le meilleur prix de la destination sur la fenêtre, toutes semaines confondues.
- Un vol est retenu uniquement s'il est **direct** (0 escale) et hors samedi. Pas de vol direct le dimanche → repli sur le lundi, signalé dans la colonne Départ.
- Le prix hôtel vient de Booking.com par **nom d'hôtel exact**. Si le nom retourné diffère du partenaire attendu, la ligne est écartée — le connecteur peut répondre par un hôtel homonyme situé dans un autre pays.
