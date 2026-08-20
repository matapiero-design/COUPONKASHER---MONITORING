# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-20 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 23/08/2026 → retour mercredi 26/08/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 23/08/2026 | Dimanche | 364 | 2026-08-20 | OK |
| Paphos | PFO | S1 | 23/08/2026 | Dimanche | 493 | 2026-08-20 | OK |
| Budapest | BUD | S1 | 23/08/2026 | Dimanche | 566 | 2026-08-20 | OK |
| Rome (Fiumicino) | FCO | S1 | 23/08/2026 | Dimanche | 561 | 2026-08-20 | OK |
| Tbilissi | TBS | S1 | 23/08/2026 | Dimanche | 806 | 2026-08-20 | OK |
| Vienne | VIE | S1 | 23/08/2026 | Dimanche | 1284 | 2026-08-20 | ⚠️ Prix élevé vs cluster ATH/FCO/BUD/PFO |
| Prague | PRG | S1 | 23/08/2026 | Dimanche | 1723 | 2026-08-20 | ⚠️ Anomalie — 1 seule option directe trouvée, prix ~3x le reste du groupe |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
