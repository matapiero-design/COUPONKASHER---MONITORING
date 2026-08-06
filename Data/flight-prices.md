# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-06 (run automatisé)
- **Portée du dernier run** : 7 destinations demandées explicitement (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vols directs uniquement, aller-retour 3 nuits, départ dimanche 09/08/2026 (S1) — retour mercredi 12/08/2026. Ce run ne couvre pas l'ensemble du Groupe A habituel (AMS, LHR, CDG non demandés cette fois) et ajoute TBS (Tbilissi), hors liste de référence des 18 destinations du skill `dashboard-suivi-prix-sejours-casher`.
- **Statut connecteur Kiwi.com** : ✅ disponible et fonctionnel (7/7 recherches réussies, vols directs trouvés sur toutes les destinations)

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 09/08/2026 | Dimanche | 729 | 2026-08-06 | OK |
| Vienne | VIE | S1 | 09/08/2026 | Dimanche | 710 | 2026-08-06 | OK |
| Rome | FCO | S1 | 09/08/2026 | Dimanche | 399 | 2026-08-06 | OK |
| Paphos | PFO | S1 | 09/08/2026 | Dimanche | 245 | 2026-08-06 | OK |
| Athènes (Chalkida) | ATH | S1 | 09/08/2026 | Dimanche | 345 | 2026-08-06 | OK |
| Budapest | BUD | S1 | 09/08/2026 | Dimanche | 411 | 2026-08-06 | OK |
| Tbilissi *(hors liste 18 destinations — ajout ponctuel de ce run)* | TBS | S1 | 09/08/2026 | Dimanche | 717 | 2026-08-06 | OK |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(non traité ce run — portée limitée à S1 sur demande explicite, pas de rotation S4-S8 demandée)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-06 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, dimanche 09/08/2026, 3 nuits, vols directs uniquement) | Aucun gap — vol direct trouvé pour les 7 destinations. Aucune anomalie de prix détectée (pas d'historique antérieur pour comparaison, c'est le premier run avec données réelles sur ce périmètre). À noter : TBS n'appartient pas à la liste de référence des 18 destinations du skill `dashboard-suivi-prix-sejours-casher` — ajouté ponctuellement sur demande de ce run. AMS, LHR (Londres) et CDG (Groupe A habituel) non couverts cette fois, non demandés dans le périmètre de ce run. | ✅ Connecteur Kiwi.com disponible et fonctionnel |
