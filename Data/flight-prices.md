# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-22 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 23/08/2026 → retour mercredi 26/08/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations (2/7 sans combinaison A/R directe disponible, voir anomalies)

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 23/08/2026 | Dimanche | 396 | 2026-08-22 | OK |
| Paphos | PFO | S1 | 23/08/2026 | Dimanche | 419 | 2026-08-22 | OK |
| Budapest | BUD | S1 | 23/08/2026 | Dimanche | 564 | 2026-08-22 | OK |
| Rome (Fiumicino) | FCO | S1 | 23/08/2026 | Dimanche | 859 | 2026-08-22 | ⚠️ Hausse forte vs run précédent (561$ → 859$, +53%) |
| Vienne | VIE | S1 | 23/08/2026 | Dimanche | 944 | 2026-08-22 | ⚠️ Baisse forte vs run précédent (1284$ → 944$, -26%) |
| Tbilissi | TBS | S1 | 23/08/2026 | Dimanche | — | 2026-08-22 | ❌ Aucune combinaison A/R directe — vol aller direct dispo (193$), aucun retour direct TBS→TLV le 26/08 |
| Prague | PRG | S1 | 23/08/2026 | Dimanche | — | 2026-08-22 | ❌ Aucune combinaison A/R directe — vol aller direct dispo (370$, Smartwings), aucun retour direct PRG→TLV le 26/08 |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-22 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7 interrogées, 5/7 avec prix A/R direct) | **FCO** : 561$ → 859$ (+53% vs run du 20/08) — hausse notable à surveiller, pas d'explication structurelle identifiée (mêmes compagnies : El Al/Israir aller, Israir retour). **VIE** : 1284$ → 944$ (-26%) — retour à un niveau plus cohérent avec le cluster ATH/FCO/BUD/PFO, probablement la résorption de la anomalie signalée le 20/08. **TBS et PRG** : aucune combinaison aller-retour 100% directe cette semaine — vol aller direct trouvé pour les deux (TBS 193$ via Israir, PRG 370$ via Smartwings) mais **aucun vol retour direct** de PRG ou TBS vers TLV le 26/08/2026 (vérifié isolément, 0 résultat sur le segment retour seul). Pour PRG c'est la confirmation de l'anomalie déjà signalée le 20/08 (alors 1 seule option A/R directe à 1723$, x3 du cluster) — la desserte directe TLV-PRG semble structurellement fragile côté retour milieu de semaine. Pour TBS c'est une dégradation par rapport au 20/08 (qui avait un prix A/R direct de 806$) : à confirmer si c'est ponctuel (pas de vol ce jour précis) ou si la fréquence Israir/LY sur TBS a changé. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
