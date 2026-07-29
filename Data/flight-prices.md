# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-07-29 (run manuel/ponctuel — hors trigger planifié)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vols directs uniquement, A/R 3 nuits, départ dimanche par défaut
- **Statut connecteur Kiwi.com** : OK — connecteur disponible et interrogé avec succès pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 02/08/2026 | Dimanche | 549 | 2026-07-29 | OK |
| Vienne | VIE | S1 | 02/08/2026 | Dimanche | 552 | 2026-07-29 | OK |
| Rome (Fiumicino) | FCO | S1 | 02/08/2026 | Dimanche | 460 | 2026-07-29 | OK |
| Paphos | PFO | S1 | 02/08/2026 | Dimanche | 354 | 2026-07-29 | OK |
| Athènes | ATH | S1 | 02/08/2026 | Dimanche | 255 | 2026-07-29 | OK |
| Budapest | BUD | S1 | 02/08/2026 | Dimanche | 484 | 2026-07-29 | OK |
| Tbilissi | TBS | S1 | 02/08/2026 | Dimanche | 492 | 2026-07-29 | OK |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire dominical)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-07-29 (run manuel, hors cron) | PRG, VIE, FCO, PFO, ATH, BUD, TBS — 7/7 vols directs A/R 3 nuits trouvés, départ dimanche 02/08/2026, retour 05/08/2026 | Aucune anomalie de prix détectée (pas d'historique antérieur pour comparaison — premier relevé de prix réel du fichier). ATH ressort comme le tarif le plus bas du groupe (255 $), à surveiller si la tendance se confirme. | OK |
