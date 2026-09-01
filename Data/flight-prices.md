# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-01 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 06/09/2026 → retour mercredi 09/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 06/09/2026 | Dimanche | 131 | 2026-09-01 | ⚠️ Baisse vs run précédent (159$→131$, -18%) |
| Paphos | PFO | S1 | 06/09/2026 | Dimanche | 155 | 2026-09-01 | ⚠️ Baisse vs run précédent (176$→155$, -12%) |
| Budapest | BUD | S1 | 06/09/2026 | Dimanche | 218 | 2026-09-01 | ⚠️ Baisse vs run précédent (248$→218$, -12%) |
| Rome (Fiumicino) | FCO | S1 | 06/09/2026 | Dimanche | 232 | 2026-09-01 | ⚠️ Forte baisse vs run précédent (358$→232$, -35%) |
| Vienne | VIE | S1 | 06/09/2026 | Dimanche | 337 | 2026-09-01 | ⚠️ Baisse vs run précédent (363$→337$, -7%) |
| Tbilissi | TBS | S1 | 06/09/2026 | Dimanche | 374 | 2026-09-01 | ⚠️ Forte baisse vs run précédent (587$→374$, -36%) — 8 options directes trouvées (vs 14-15 sur les autres destinations), en hausse par rapport aux 4 options du run du 25/08 |
| Prague | PRG | S1 | 06/09/2026 | Dimanche | 377 | 2026-09-01 | ⚠️ Baisse vs run précédent (430$→377$, -12%) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-01 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse généralisée sur les 7 destinations vs le run du 2026-08-25 (de -7% pour VIE à -36% pour TBS). Deux écarts dépassent nettement le seuil de vigilance de 15 % : Rome/FCO (358$→232$, -35%, porté par un nouveau plancher Wizz Air Malta à 232$) et Tbilissi (587$→374$, -36%, sur une option Israir). Les cinq autres destinations reculent de façon plus modérée (-7% à -18%), cohérent avec un simple rapprochement de la date de recherche vers le départ (5 jours d'avance dans les deux runs, méthodologie inchangée) plutôt qu'avec un changement structurel. TBS reste la route la plus contrainte : 8 options directes trouvées (vs 14-15 pour les autres destinations), en amélioration par rapport aux 4 options du run précédent, mais toujours porté par les seuls transporteurs Israir/El Al identifiés précédemment — cohérent avec une offre directe TLV-TBS structurellement plus restreinte, pas une anomalie de données. À confirmer sur les prochains runs, en particulier la baisse FCO et TBS qui dépasse la volatilité habituelle observée sur les autres destinations. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
