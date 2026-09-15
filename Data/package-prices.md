# Prix package séjour casher — CouponKasher

Généré par `pipeline/pricing.py` à partir du run vol (Kiwi.com) + hôtel (Booking.com).
Ne pas éditer à la main — le prochain run écrase ce fichier.

- **Run** : 2026-09-15 (run quotidien package vol+hotel Groupe A S1-S8 — run manuel (trigger trig_01AC9Z8TrgTpLToieNmSJ6G4 sans connecteurs, blocage API connu). Dernier run : 2026-08-25.)
- **Schéma** : 3 nuits / 4 jours, depart dimanche -> retour mercredi (repli lundi si pas de direct dimanche). Fenetre S1-S8 : S1 20/09, S2 27/09, S3 04/10, S4 11/10, S5 18/10, S6 25/10, S7 01/11, S8 08/11.
- **Taux appliqué** : 1 USD = 3.05 ILS · marge 15 % · formule `(vol + hôtel/pers) ÷ 0.85 × 3.05`
- **Généré le** : 2026-09-15 03:38 UTC

> **Calendrier** — Haggim 5787 (Israel) : RH 22-23/09 (aeroport ferme), YK 1/10 (aeroport ferme), Sukkot j1 6/10 (aeroport ferme), Shimini Atzeret+Sim'hat Torah 13/10 (aeroport ferme). CORRECTION calendrier Israel vs diaspora : en Israel le 2e jour de Sukkot (07/10) est Hol HaMoed, aeroport BEN GURION OUVERT — S3 (depart 04/10, retour 07/10) est VALIDE. S4 (depart 11/10, retour 14/10) : retour post-Shimini Atzeret, VALIDE. DECISION JACQUES (15/09/2026) : flexibilite exceptionnelle accordee pour S2/Erev YK (retour 30/09) et S3/Hol HaMoed (retour 07/10) — ces semaines sont desormais vendables. TBS : aucun vol direct TLV-TBS le dimanche avant S5 (18/10). MNE : directs TLV-TIV uniquement S3 et S5 sur la fenetre.

## À publier — meilleur prix par destination

| Destination | Meilleur ₪ | Semaine | Publié ₪ | Écart | Décision |
|---|---|---|---|---|---|
| Paphos (PFO) | 1360 | S5 | 1590 | -14 % | publiable |
| Budapest (BUD) | 1380 | S8 | 1390 | -1 % | publiable |
| Chalkida (ATH) | 1590 | S8 | 1800 | -12 % | publiable |
| Vienne (VIE) | 1930 | S4 | 2520 | -23 % | ⚠️ hors seuil — arbitrage Jacques |
| Tbilissi (TBS) | 2090 | S6 | 2000 | +4 % | publiable |
| Budva (TIV) | 2430 | S3 | 2580 | -6 % | publiable |
| Londres (LON) | 2520 | S8 | 2660 | -5 % | publiable |
| Amsterdam (AMS) | 2610 | S5 | 1900 | +37 % | ⚠️ hors seuil — arbitrage Jacques |
| Prague (PRG) | 2690 | S8 | 3260 | -17 % | ⚠️ hors seuil — arbitrage Jacques |

## Détail S1

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-09-20 · dimanche | 186 | 228.44 | 1480 | bloque roch hachana · retour 23/09 = RH j2. Vol 0 escale disponible |
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-09-20 · dimanche | 418 | 242.81 | 2370 | bloque roch hachana · retour 23/09 = RH j2. Wizz Air 0 escale |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-09-20 · dimanche | 486 | 239.23 | 2600 | bloque roch hachana · retour 23/09 = RH j2, aeroport ferme. Blue Bird 0 escale |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-09-20 · dimanche | 805 | 158.93 | 3450 | bloque roch hachana · retour 23/09 = RH j2. Blue Bird BZ612. AMS n'a pas de direct TLV-AMS les dimanches de S3, S4, S6, S7 — gaps confirmes |
| Prague (PRG) | מלון כשר קינג דייויד פראג | 2026-09-20 · dimanche | 579 | 443.04 | 3660 | bloque roch hachana · retour 23/09 = RH j2, aeroport ferme. Vol TUS Airways 0 escale, prix pour reference uniquement |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | — | — | 374.86 | — | gap vol · aucun vol direct TLV-TBS dimanche sur S1-S4. Premier direct : S5 18/10 |
| Venise (VCE) | Rimon Place | — | — | — | — | cacherout bloquee · certification Rimon Place contestee (destinations.json) — aucun prix calcule tant que Jacques ne tranche pas. Non traite dans ce run |

## Détail S2

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-09-27 · dimanche | 567 | 239.23 | 2890 | ok · retour 30/09 = Erev YK — flexibilite exceptionnelle validee par Jacques (15/09/2026). Vols operationnels, clientele informee. Blue Bird BZ612 |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-09-27 · dimanche | 805 | 158.93 | 3450 | ok · retour 30/09 = Erev YK — flexibilite exceptionnelle validee par Jacques (15/09/2026). Blue Bird BZ612 |
| Londres (LON) | Croft Court Hotel (Golders Green NW11) | 2026-09-27 · dimanche | 1144 | 303.2 | 5190 | ok · retour 30/09 = Erev YK — flexibilite exceptionnelle validee par Jacques (15/09/2026). Vol direct TLV-STN/LGW/LTN (flyTo=London) |

## Détail S3

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-10-04 · dimanche | 169 | 228.44 | 1420 | ok · retour 07/10 = Hol HaMoed Israel — VALIDE |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-10-05 · lundi (repli — pas de direct dimanche 04/10) | 142 | 305.14 | 1600 | ok · retour 08/10 = Hol HaMoed, aeroport ouvert. Israir 0 escale |
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-10-04 · dimanche | 383 | 242.81 | 2240 | ok · retour 07/10 = Hol HaMoed Israel — VALIDE |
| Budva (TIV) | Hotel Harmonia by Dukley | 2026-10-04 · dimanche | 346 | 332.97 | 2430 | ok · retour 07/10 = Hol HaMoed Israel — VALIDE. Israir TLV-TIV 0 escale. Pas de direct TLV-TIV en S4, S6, S7, S8 — gaps |
| Prague (PRG) | מלון כשר קינג דייויד פראג | 2026-10-04 · dimanche | 525 | 443.04 | 3470 | ok · retour 07/10 = Hol HaMoed Sukkot (Israel, aeroport ouvert) — VALIDE pour clientele israelienne. Hotel reference S5 |
| Londres (LON) | Croft Court Hotel (Golders Green NW11) | 2026-10-04 · dimanche | 1048 | 303.2 | 4840 | ok · retour 07/10 = Hol HaMoed Israel — VALIDE |

## Détail S4

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-10-11 · dimanche | 149 | 242.81 | 1400 | ok |
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-10-11 · dimanche | 170 | 228.44 | 1420 | ok |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-10-11 · dimanche | 146 | 305.14 | 1610 | ok |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-10-11 · dimanche | 301 | 239.23 | 1930 | ok |
| Prague (PRG) | מלון כשר קינג דייויד פראג | 2026-10-11 · dimanche | 317 | 443.04 | 2720 | ok · retour 14/10 = lendemain de Shimini Atzeret (13/10), aeroport ouvert |
| Londres (LON) | Croft Court Hotel (Golders Green NW11) | 2026-10-11 · dimanche | 1297 | 303.2 | 5740 | ok · vol plus cher que S3 et S5 — verifier si contrainte disponibilite ou tarif dynamique post-fetes |

## Détail S5

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-10-18 · dimanche | 151 | 228.44 | 1360 | ok · meilleur vol de la fenetre. Hotel interroge sur ces dates |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-10-18 · dimanche | 146 | 305.14 | 1610 | ok · hotel interroge sur ces dates |
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-10-18 · dimanche | 250 | 242.81 | 1760 | ok · hotel interroge sur ces dates |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-10-18 · dimanche | 301 | 239.23 | 1930 | ok · hotel interroge sur ces dates |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-10-18 · dimanche | 305 | 374.86 | 2430 | ok · hotel interroge sur ces dates |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-10-18 · dimanche | 571 | 158.93 | 2610 | ok · vol Blue Bird BZ612 13:10->17:35, retour BZ611 18:35->00:20. Hotel interroge sur ces dates |
| Prague (PRG) | מלון כשר קינג דייויד פראג | 2026-10-18 · dimanche | 321 | 443.04 | 2740 | ok · hotel interroge sur ces dates (reference du run) |
| Budva (TIV) | Hotel Harmonia by Dukley | 2026-10-18 · dimanche | 491 | 332.97 | 2950 | ok · hotel interroge sur ces dates. Seules 2 semaines disponibles sur la fenetre S1-S8 pour ce O&D |
| Londres (LON) | Croft Court Hotel (Golders Green NW11) | 2026-10-18 · dimanche | 853 | 303.2 | 4140 | ok · hotel interroge sur ces dates |
| Paphos (PFO) | Brown Hills | 2026-10-18 · dimanche | 151 | — | — | gap hotel · Booking: Brown Hills aucune disponibilite sur 18-21/10. Vol PFO disponible a 151 $. Hotel interroge en S6 (25-28/10) = 761.48 $ total pour reference |

## Détail S6

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-10-25 · dimanche | 220 | 242.81 | 1660 | ok |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-10-25 · dimanche | 175 | 305.14 | 1720 | ok |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-10-25 · dimanche | 311 | 239.23 | 1970 | ok |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-10-25 · dimanche | 210 | 374.86 | 2090 | ok |
| Prague (PRG) | מלון כשר קינג דייויד פראג | 2026-10-25 · dimanche | 339 | 443.04 | 2800 | ok · prix hotel extrapole depuis reference S5 |
| Londres (LON) | Croft Court Hotel (Golders Green NW11) | 2026-10-25 · dimanche | 613 | 303.2 | 3280 | ok |
| Paphos (PFO) | Paphos Hills Resort & Spa by Brown Hotels | — | — | 380.74 | — | gap vol · hotel 761.48 $ disponible en S6 (25-28/10) mais aucun vol direct TLV-PFO dimanche 25/10 dans Kiwi — gap vol confirme |

## Détail S7

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-11-01 · dimanche | 212 | 374.86 | 2100 | ok |

## Détail S8

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-11-08 · dimanche | 142 | 242.81 | 1380 | ok · meilleur vol de la fenetre |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-11-08 · dimanche | 140 | 305.14 | 1590 | ok · meilleur vol de la fenetre pour Chalkida |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-11-08 · dimanche | 316 | 239.23 | 1990 | ok |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-11-08 · dimanche | 210 | 374.86 | 2090 | ok |
| Londres (LON) | Croft Court Hotel (Golders Green NW11) | 2026-11-08 · dimanche | 401 | 303.2 | 2520 | ok · meilleur vol de la fenetre pour Londres — premiere fois sous 500 $ |
| Prague (PRG) | מלון כשר קינג דייויד פראג | 2026-11-08 · dimanche | 309 | 443.04 | 2690 | ok · meilleur vol de la fenetre pour Prague |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-11-08 · dimanche | 690 | 158.93 | 3040 | ok · vol El Al LY337 06:00->10:15 |

## Lecture

- Un écart supérieur à 15 % vs le prix publié sur couponkasher.co.il n'est **jamais** publié automatiquement : il doit être confirmé par Jacques.
- Le site affiche un prix « à partir de » (החל ב-) : la valeur publiable est donc le meilleur prix de la destination sur la fenêtre, toutes semaines confondues.
- Un vol est retenu uniquement s'il est **direct** (0 escale) et hors samedi. Pas de vol direct le dimanche → repli sur le lundi, signalé dans la colonne Départ.
- Le prix hôtel vient de Booking.com par **nom d'hôtel exact**. Si le nom retourné diffère du partenaire attendu, la ligne est écartée — le connecteur peut répondre par un hôtel homonyme situé dans un autre pays.
