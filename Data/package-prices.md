# Prix package séjour casher — CouponKasher

Généré par `pipeline/pricing.py` à partir du run vol (Kiwi.com) + hôtel (Booking.com).
Ne pas éditer à la main — le prochain run écrase ce fichier.

- **Run** : 2026-08-25 (premier run package vol+hotel — validation de bout en bout du branchement Kiwi.com + Booking.com)
- **Schéma** : 3 nuits / 4 jours — depart dimanche 30/08/2026, retour mercredi 02/09/2026 (repli lundi 31/08 → jeudi 03/09 si pas de vol direct le dimanche)
- **Taux appliqué** : 1 USD = 3.05 ILS · marge 15 % · formule `(vol + hôtel/pers) ÷ 0.85 × 3.05`
- **Généré le** : 2026-08-25 18:48 UTC

## Prix calculés (par personne, base 2 adultes en chambre double)

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Publié ₪ | Écart | Statut |
|---|---|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-08-30 · dimanche | 236 | 250.14 | 1740 | 1740 | +0 % | ok · nom Booking retourne = 'Hotel & Residence, Palace Quarter' alors que la reference dit 'Hotel & Apartments' — a confirmer par Jacques |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-08-30 · dimanche | 401 | 128.62 | 1900 | 2240 | -15 % | ⚠️ à confirmer — ok · vol Blue Bird A/R, 0 escale |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-08-30 · dimanche | 160 | 377.84 | 1920 | 1920 | +0 % | ok · vol Israir aller / Blue Bird retour, 0 escale |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-08-30 · dimanche | 364 | 340.68 | 2520 | 2520 | +0 % | ok · vol Blue Bird A/R, 0 escale |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-08-31 · lundi (repli) | 543 | 285.99 | 2970 | 2970 | +0 % | ok · aucun vol direct le dimanche 30/08 — repli lundi applique, hotel re-interroge sur les memes dates decalees |
| Paphos (PFO) | Paphos Hills Resort & Spa by Brown Hotels | 2026-08-30 · dimanche | 166 | 809.03 | 3490 | 2965 | +18 % | ⚠️ à confirmer — ok · hotel a 270 $/nuit pour 2 en pic d'aout |
| Londres (LON) | Croft Court Hotel | 2026-08-30 · dimanche | 829 | 185.02 | 3630 | 3630 | +0 % | ok · Arkia TLV-STN A/R, 0 escale. Kiwi ne renvoie AUCUN direct sur LHR : les directs TLV-Londres passent par Stansted, Luton et Gatwick. Interroger la ville et non LHR, sinon faux gap. Croft Court est a Golders Green, donc STN/LTN conviennent |
| Budva (TIV) | Hotel Harmonia by Dukley | 2026-08-30 · dimanche | 515 | 559.97 | 3850 | 3850 | +0 % | ok · Israir TLV-TIV A/R, 0 escale. Le direct est sur Tivat, pas Podgorica (TGD) |
| Venise (VCE) | Rimon Place Kosher | 2026-08-30 · dimanche | 687 | 426.55 | 3990 | 3675 | +9 % | certification a trancher · El Al A/R 0 escale, hotel dispo. Prix NON publie : statut cacherout contradictoire entre le master portfolio (Tier 3) et la reference promo (mehadrin) |
| Prague (PRG) | Kosher Hotel King David Prague | 2026-08-30 · dimanche | 456 | 1013.19 | 5270 | 2945 | +79 % | ⚠️ à confirmer — ok · hotel a 675 $/nuit pour 2 en pic d'aout — c'est lui qui fait exploser le package, pas le vol |
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-08-30 · dimanche | 166 | — | — | 2790 | — | gap hotel · Booking: WellClub Resort complet sur ces dates (hotel_names_no_availability). Vol OK a 166 $ — c'est l'hotel qui bloque |
| Paphos (PFO) | Greek Village Hotel | 2026-08-30 · dimanche | 166 | — | — | 2355 | — | gap hotel · Booking: aucune disponibilite sur ces dates (hotel_names_no_availability) |
| Rome (FCO) | NEMAN Maison | 2026-08-30 · dimanche | 359 | — | — | 3290 | — | gap hotel · Wizz Air A/R 0 escale. NEMAN Maison est hors Booking.com : prix hotel a fournir par Jacques |

## Lecture

- Un écart supérieur à 15 % vs le prix publié sur couponkasher.co.il n'est **jamais** publié automatiquement : il doit être confirmé par Jacques.
- Un vol est retenu uniquement s'il est **direct** (0 escale) et hors samedi. Pas de vol direct le dimanche → repli sur le lundi, signalé dans la colonne Départ.
- Le prix hôtel vient de Booking.com par **nom d'hôtel exact** : si le nom retourné diffère du partenaire attendu, la ligne est marquée à confirmer.
