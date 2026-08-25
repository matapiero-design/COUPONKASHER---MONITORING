# Prix package séjour casher — CouponKasher

Généré par `pipeline/pricing.py` à partir du run vol (Kiwi.com) + hôtel (Booking.com).
Ne pas éditer à la main — le prochain run écrase ce fichier.

- **Run** : 2026-08-25 (premier run package vol+hotel — validation de bout en bout du branchement Kiwi.com + Booking.com)
- **Schéma** : 3 nuits / 4 jours, depart dimanche -> retour mercredi (repli lundi -> jeudi si pas de direct le dimanche). S1 = 30/08 -> 02/09/2026, S2 = 06/09 -> 09/09/2026.
- **Taux appliqué** : 1 USD = 3.05 ILS · marge 15 % · formule `(vol + hôtel/pers) ÷ 0.85 × 3.05`
- **Généré le** : 2026-08-25 18:52 UTC

> **Calendrier** — Roch Hachana 5787 : du vendredi 11/09 au soir au dimanche 13/09 au soir. Le depart dominical de S3 (13/09) tombe donc en plein Yom Tov — inutilisable. Repli lundi 14/09 -> jeudi 17/09. Yom Kippour et Souccot saturent ensuite tout le mois : forte demande israelienne a prevoir sur S3-S6.

## À publier — meilleur prix par destination

| Destination | Meilleur ₪ | Semaine | Publié ₪ | Écart | Décision |
|---|---|---|---|---|---|
| Budapest (BUD) | 1740 | S1 | 1740 | +0 % | publiable |
| Amsterdam (AMS) | 1900 | S1 | 2240 | -15 % | ⚠️ hors seuil — arbitrage Jacques |
| Chalkida (ATH) | 1920 | S1 | 1920 | +0 % | publiable |
| Paphos (PFO) | 1990 | S2 | 2790 | -29 % | ⚠️ hors seuil — arbitrage Jacques |
| Vienne (VIE) | 2520 | S1 | 2520 | +0 % | publiable |
| Tbilissi (TBS) | 2970 | S1 | 2970 | +0 % | publiable |
| Prague (PRG) | 3260 | S2 | 3260 | +0 % | publiable |
| Paphos (PFO) | 3490 | S1 | 2965 | +18 % | ⚠️ hors seuil — arbitrage Jacques |
| Londres (LON) | 3630 | S1 | 3630 | +0 % | publiable |
| Budva (TIV) | 3850 | S1 | 3850 | +0 % | publiable |
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
| Prague (PRG) | Kosher Hotel King David Prague | 2026-09-06 · dimanche | 359 | 550.05 | 3260 | ok · TUS Airways A/R 0 escale. Hotel a 1100 $ contre 2026 $ une semaine plus tot : le +79 % de S1 etait bien le pic d'aout, pas un prix structurel |
| Paphos (PFO) | Greek Village Hotel | 2026-09-06 · dimanche | 171 | — | — | faux match Booking · PIEGE : Booking repond 'Filerimos Village Hotel' a Ialyssos, en GRECE (Rhodes) — un autre hotel, un autre pays. Ne jamais retenir un resultat dont le nom ne correspond pas |

## Lecture

- Un écart supérieur à 15 % vs le prix publié sur couponkasher.co.il n'est **jamais** publié automatiquement : il doit être confirmé par Jacques.
- Le site affiche un prix « à partir de » (החל ב-) : la valeur publiable est donc le meilleur prix de la destination sur la fenêtre, toutes semaines confondues.
- Un vol est retenu uniquement s'il est **direct** (0 escale) et hors samedi. Pas de vol direct le dimanche → repli sur le lundi, signalé dans la colonne Départ.
- Le prix hôtel vient de Booking.com par **nom d'hôtel exact**. Si le nom retourné diffère du partenaire attendu, la ligne est écartée — le connecteur peut répondre par un hôtel homonyme situé dans un autre pays.
