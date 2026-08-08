# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-08 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vols directs
  uniquement, aller-retour 3 nuits, départ dimanche par défaut — semaine S1 (09/08/2026 →
  12/08/2026) uniquement. Note : TBS (Tbilissi) ne fait pas partie de la liste Groupe A standard du
  skill `dashboard-suivi-prix-sejours-casher` — traité ici sur demande explicite du prompt de ce
  run.
- **Statut connecteur Kiwi.com** : OK — connecteur actif, vol direct trouvé pour 7/7 destinations.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 09/08/2026 | Dimanche | 778 | 2026-08-08 | ⚠️ Prix élevé vs destinations comparables (VIE, BUD) — à surveiller |
| Vienne | VIE | S1 | 09/08/2026 | Dimanche | 643 | 2026-08-08 | OK |
| Rome | FCO | S1 | 09/08/2026 | Dimanche | 494 | 2026-08-08 | OK |
| Paphos | PFO | S1 | 09/08/2026 | Dimanche | 325 | 2026-08-08 | OK |
| Chalkida/Athènes | ATH | S1 | 09/08/2026 | Dimanche | 272 | 2026-08-08 | OK |
| Budapest | BUD | S1 | 09/08/2026 | Dimanche | 579 | 2026-08-08 | OK |
| Tbilissi | TBS | S1 | 09/08/2026 | Dimanche | 697 | 2026-08-08 | OK (hors Groupe A standard) |
| _(S2-S3 non couvertes ce run — hors portée du prompt de ce run)_ | | | | | | | |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-08 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, dép. dimanche 09/08/2026, retour 12/08/2026, 3 nuits, vols directs uniquement) | Aucun gap (vol direct trouvé pour les 7 destinations). Anomalie notée : PRG à 778$ nettement au-dessus de VIE (643$) et BUD (579$) alors que la distance/durée de vol est comparable — à surveiller sur les prochains runs faute d'historique pour confirmer une tendance. | OK |
