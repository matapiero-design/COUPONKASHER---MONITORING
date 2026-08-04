# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 04/08/2026 (run initial effectué)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vols directs (0 escale) A/R, départ dimanche 09/08/2026 → retour mercredi 12/08/2026 (3 nuits), prix en USD
- **Statut connecteur Kiwi.com** : OK — connecteur disponible et interrogé avec succès pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 09/08/2026 | Dimanche | 730 | 04/08/2026 | ⚠️ Prix élevé (peu d'offres directes) |
| Vienne | VIE | S1 | 09/08/2026 | Dimanche | 836 | 04/08/2026 | ⚠️ Prix élevé |
| Rome | FCO | S1 | 09/08/2026 | Dimanche | 366 | 04/08/2026 | OK |
| Paphos | PFO | S1 | 09/08/2026 | Dimanche | 310 | 04/08/2026 | OK |
| Athènes | ATH | S1 | 09/08/2026 | Dimanche | 335 | 04/08/2026 | OK |
| Budapest | BUD | S1 | 09/08/2026 | Dimanche | 333 | 04/08/2026 | OK |
| Tbilissi | TBS | S1 | 09/08/2026 | Dimanche | 625 | 04/08/2026 | ⚠️ Prix élevé (peu d'offres directes) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — portée S4-S8 non couverte par ce run, pas exécuté un dimanche)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-04 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, dimanche 09/08→12/08, 3 nuits, vols directs) | PRG (730$), VIE (836$) et TBS (625$) nettement plus chers que ATH/BUD/FCO/PFO (310-366$) pour un vol A/R 3 nuits comparable. PRG et TBS n'ont que 4 offres directes chacun (vs 15 pour ATH/BUD/FCO/PFO) — probable cause : faible fréquence de vols directs sur ces routes plutôt qu'une vraie hausse de tarif. À surveiller sur les prochains runs pour confirmer la tendance. | OK |
