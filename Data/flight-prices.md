# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-07-31 (premier run automatisé réussi — connecteur Kiwi.com opérationnel)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS) au départ de TLV — vols directs uniquement (0 escale), aller-retour 3 nuits, départ dimanche par défaut — semaines S1-S3 (S4-S8 non traité, run non-dominical)
- **Statut connecteur Kiwi.com** : Opérationnel — la limitation documentée le 28/07/2026 (connecteur non attaché sur le trigger créé par API) semble résolue ; le connecteur a répondu normalement sur les 7 destinations de ce run.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 02/08/2026 | Dimanche | 565 | 2026-07-31 | OK |
| Prague | PRG | S2 | 09/08/2026 | Dimanche | 556 | 2026-07-31 | OK |
| Prague | PRG | S3 | 16/08/2026 | Dimanche | 977 | 2026-07-31 | ⚠ Anomalie — voir note |
| Vienne | VIE | S1 | 02/08/2026 | Dimanche | 1122 | 2026-07-31 | OK (route structurellement chère) |
| Vienne | VIE | S2 | 09/08/2026 | Dimanche | 957 | 2026-07-31 | OK |
| Vienne | VIE | S3 | 16/08/2026 | Dimanche | 882 | 2026-07-31 | OK |
| Rome | FCO | S1 | 02/08/2026 | Dimanche | 722 | 2026-07-31 | ⚠ Anomalie — voir note |
| Rome | FCO | S2 | 09/08/2026 | Dimanche | 381 | 2026-07-31 | OK |
| Rome | FCO | S3 | 16/08/2026 | Dimanche | 359 | 2026-07-31 | OK |
| Paphos | PFO | S1 | 02/08/2026 | Dimanche | 354 | 2026-07-31 | OK |
| Paphos | PFO | S2 | 09/08/2026 | Dimanche | 299 | 2026-07-31 | OK |
| Paphos | PFO | S3 | 16/08/2026 | Dimanche | 383 | 2026-07-31 | OK |
| Athènes (Chalkida) | ATH | S1 | 02/08/2026 | Dimanche | 266 | 2026-07-31 | OK |
| Athènes (Chalkida) | ATH | S2 | 09/08/2026 | Dimanche | 284 | 2026-07-31 | OK |
| Athènes (Chalkida) | ATH | S3 | 16/08/2026 | Dimanche | 454 | 2026-07-31 | À surveiller (+~65% vs S1/S2) |
| Budapest | BUD | S1 | 02/08/2026 | Dimanche | 483 | 2026-07-31 | OK |
| Budapest | BUD | S2 | 09/08/2026 | Dimanche | 354 | 2026-07-31 | OK |
| Budapest | BUD | S3 | 16/08/2026 | Dimanche | 337 | 2026-07-31 | OK |
| Tbilissi | TBS | S1 | 02/08/2026 | Dimanche | 669 | 2026-07-31 | OK |
| Tbilissi | TBS | S2 | 09/08/2026 | Dimanche | 636 | 2026-07-31 | OK |
| Tbilissi | TBS | S3 | 16/08/2026 | Dimanche | 743 | 2026-07-31 | OK |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — run du 31/07/2026 non-dominical, S4-S8 non traité ce jour)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-07-31 | PRG, VIE, FCO, PFO, ATH, BUD, TBS × S1-S3 (7 destinations × 3 semaines = 21 recherches) | Premier run — pas d'historique antérieur pour comparaison. Deux écarts intra-run confirmés par requête dédiée (pas un artefact de troncature) : **PRG S3** à 977$ contre ~560$ sur S1/S2 (+~75%, seuls des combos plus chers/vols matinaux Smartwings disponibles ce dimanche-là) et **FCO S1** à 722$ contre ~370$ sur S2/S3 (+~90%, probable prime de dernière minute à J+3). **ATH S3** à 454$ contre ~270-285$ sur S1/S2 (+~65%) à surveiller aussi. Aucun gap de disponibilité (vol direct trouvé dimanche pour les 7×3 O&D). | Opérationnel — limitation du 28/07/2026 (connecteur non attaché sur trigger API) non reproduite sur ce run. |
