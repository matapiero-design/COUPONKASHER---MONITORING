# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-07-28 03:35 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS) × S1-S3, dimanche, vols directs, 3 nuits
- **Statut connecteur Kiwi.com** : opérationnel (21/21 recherches réussies)

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 02/08/2026 | Dimanche | 625 | 2026-07-28 | OK |
| Prague | PRG | S2 | 09/08/2026 | Dimanche | 927 | 2026-07-28 | OK |
| Prague | PRG | S3 | 16/08/2026 | Dimanche | 951 | 2026-07-28 | OK |
| Vienne | VIE | S1 | 02/08/2026 | Dimanche | 549 | 2026-07-28 | OK |
| Vienne | VIE | S2 | 09/08/2026 | Dimanche | 899 | 2026-07-28 | OK |
| Vienne | VIE | S3 | 16/08/2026 | Dimanche | 824 | 2026-07-28 | OK |
| Rome | FCO | S1 | 02/08/2026 | Dimanche | 467 | 2026-07-28 | OK |
| Rome | FCO | S2 | 09/08/2026 | Dimanche | 382 | 2026-07-28 | OK |
| Rome | FCO | S3 | 16/08/2026 | Dimanche | 399 | 2026-07-28 | OK |
| Paphos | PFO | S1 | 02/08/2026 | Dimanche | 310 | 2026-07-28 | OK |
| Paphos | PFO | S2 | 09/08/2026 | Dimanche | 310 | 2026-07-28 | OK |
| Paphos | PFO | S3 | 16/08/2026 | Dimanche | 385 | 2026-07-28 | OK |
| Athènes | ATH | S1 | 02/08/2026 | Dimanche | 276 | 2026-07-28 | OK |
| Athènes | ATH | S2 | 09/08/2026 | Dimanche | 303 | 2026-07-28 | OK |
| Athènes | ATH | S3 | 16/08/2026 | Dimanche | 358 | 2026-07-28 | OK |
| Budapest | BUD | S1 | 02/08/2026 | Dimanche | 484 | 2026-07-28 | OK |
| Budapest | BUD | S2 | 09/08/2026 | Dimanche | 371 | 2026-07-28 | OK |
| Budapest | BUD | S3 | 16/08/2026 | Dimanche | 392 | 2026-07-28 | OK |
| Tbilissi | TBS | S1 | 02/08/2026 | Dimanche | 481 | 2026-07-28 | OK |
| Tbilissi | TBS | S2 | 09/08/2026 | Dimanche | 576 | 2026-07-28 | OK |
| Tbilissi | TBS | S3 | 16/08/2026 | Dimanche | 646 | 2026-07-28 | OK |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire du dimanche)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-07-28 03:35 | PRG, VIE, FCO, PFO, ATH, BUD, TBS — S1-S3 (7 dest. × 3 sem. = 21 recherches, 21/21 réussies) | Aucun gap (vol direct trouvé dimanche pour toutes les combinaisons). PRG augmente fortement avec l'éloignement (625→927→951$, +52%) — à surveiller, pas de comparaison historique possible (premier run). TBS ne figure pas dans la liste Groupe A/B de référence du skill `dashboard-suivi-prix-sejours-casher` — à confirmer avec Jacques si nouvelle destination active. Portée limitée aux 7 destinations demandées (hors AMS, LHR, CDG du Groupe A standard). | Opérationnel |
