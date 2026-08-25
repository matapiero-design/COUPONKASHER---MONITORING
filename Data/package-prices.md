# Prix package séjour casher — CouponKasher

Généré par `pipeline/pricing.py` à partir du run vol (Kiwi.com) + hôtel (Booking.com).
Ne pas éditer à la main — le prochain run écrase ce fichier.

- **Run** : 2026-08-25 (premier run package vol+hotel — validation de bout en bout du branchement Kiwi.com + Booking.com)
- **Schéma** : 3 nuits / 4 jours — depart dimanche 30/08/2026, retour mercredi 02/09/2026 (repli lundi 31/08 → jeudi 03/09 si pas de vol direct le dimanche)
- **Taux appliqué** : 1 USD = 3.05 ILS · marge 15 % · formule `(vol + hôtel/pers) ÷ 0.85 × 3.05`
- **Généré le** : 2026-08-25 18:13 UTC

## Prix calculés (par personne, base 2 adultes en chambre double)

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Publié ₪ | Écart | Statut |
|---|---|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-08-30 · dimanche | 236 | 250.14 | 1740 | — | — | ok · nom Booking retourne = 'Hotel & Residence, Palace Quarter' alors que la reference dit 'Hotel & Apartments' — a confirmer par Jacques |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-08-30 · dimanche | 401 | 128.62 | 1900 | 2240 | -15 % | ⚠️ à confirmer — ok · vol Blue Bird A/R, 0 escale |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-08-30 · dimanche | 160 | 377.84 | 1920 | 2255 | -15 % | ok · vol Israir aller / Blue Bird retour, 0 escale |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-08-30 · dimanche | 364 | 340.68 | 2520 | 2290 | +10 % | ok · vol Blue Bird A/R, 0 escale |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-08-31 · lundi (repli) | 543 | 285.99 | 2970 | 2880 | +3 % | ok · aucun vol direct le dimanche 30/08 — repli lundi applique, hotel re-interroge sur les memes dates decalees |
| Prague (PRG) | Kosher Hotel King David Prague | 2026-08-30 · dimanche | 456 | 1013.19 | 5270 | 2945 | +79 % | ⚠️ à confirmer — ok · hotel a 675 $/nuit pour 2 en pic d'aout — c'est lui qui fait exploser le package, pas le vol |
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-08-30 · dimanche | 166 | — | — | 2790 | — | gap hotel · Booking: WellClub Resort complet sur ces dates (hotel_names_no_availability). Vol OK a 166 $ — c'est l'hotel qui bloque |
| Londres (LHR) | Croft Court Hotel | —  | — | 185.02 | — | 3885 | — | gap vol · Kiwi renvoie 0 vol direct TLV-LHR le dimanche ET le lundi, alors que El Al/BA operent la ligne en direct — probable trou de couverture Kiwi sur LHR, pas une absence reelle de vol direct. A investiguer avant de conclure |

## Lecture

- Un écart supérieur à 15 % vs le prix publié sur couponkasher.co.il n'est **jamais** publié automatiquement : il doit être confirmé par Jacques.
- Un vol est retenu uniquement s'il est **direct** (0 escale) et hors samedi. Pas de vol direct le dimanche → repli sur le lundi, signalé dans la colonne Départ.
- Le prix hôtel vient de Booking.com par **nom d'hôtel exact** : si le nom retourné diffère du partenaire attendu, la ligne est marquée à confirmer.
