# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-13 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vols directs uniquement, aller-retour 3 nuits, départ dimanche par défaut (S1 — semaine du 16/08/2026)
- **Statut connecteur Kiwi.com** : OK — connecteur attaché et fonctionnel sur cette session

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 17/08/2026 | Lundi | 811 | 2026-08-13 | ⚠️ Gap dimanche — aucun vol direct dimanche 16/08, reporté au lundi 17/08 (voir Journal) |
| Vienne | VIE | S1 | 16/08/2026 | Dimanche | 635 | 2026-08-13 | OK |
| Rome (Fiumicino) | FCO | S1 | 16/08/2026 | Dimanche | 413 | 2026-08-13 | OK |
| Paphos | PFO | S1 | 16/08/2026 | Dimanche | 365 | 2026-08-13 | OK |
| Athènes | ATH | S1 | 16/08/2026 | Dimanche | 441 | 2026-08-13 | OK |
| Budapest | BUD | S1 | 16/08/2026 | Dimanche | 394 | 2026-08-13 | OK |
| Tbilissi | TBS | S1 | 16/08/2026 | Dimanche | 839 | 2026-08-13 | ⚠️ Prix élevé / faible offre directe (voir Journal) |
| _S2 (semaine du 23/08) et S3 (semaine du 30/08)_ | | | | | | | _non vérifiées ce run — portée du run limitée à S1 (voir prompt reçu)_ |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — run du jour n'est pas un dimanche, section non traitée)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-13 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, direct, A/R 3 nuits, USD) | **PRG** : 0 vol direct trouvé dimanche 16/08 (TLV→PRG A/R 3 nuits) — reporté au lundi 17/08→20/08, prix 811 $ (Arkia IZ283/IZ282), le plus cher des 7 destinations alors que Vienne (distance comparable) est à 635 $ — à surveiller. **TBS** : 839 $, nettement au-dessus des autres destinations (365-635 $) et seulement 4 itinéraires directs trouvés contre 15 pour la plupart des autres — offre directe limitée (Israir/Arkia uniquement), pas une erreur mais un point de vigilance prix. Aucune autre anomalie notable ; PFO le moins cher (365 $), cohérent avec un vol court-courrier vers Chypre. | OK |
