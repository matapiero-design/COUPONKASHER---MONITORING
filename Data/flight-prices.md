# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-03 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 06/09/2026 → retour mercredi 09/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations
- **Note** : 9 jours sans run depuis le précédent relevé (2026-08-25) — voir Journal des runs ci-dessous. La comparaison de prix se fait donc vs le run du 25/08, pas vs la veille.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 06/09/2026 | Dimanche | 136 | 2026-09-03 | ⚠️ Baisse vs run précédent (159$→136$, -14%) |
| Paphos | PFO | S1 | 06/09/2026 | Dimanche | 144 | 2026-09-03 | ⚠️ Baisse vs run précédent (176$→144$, -18%) |
| Budapest | BUD | S1 | 06/09/2026 | Dimanche | 233 | 2026-09-03 | Stable vs run précédent (248$→233$, -6%) |
| Rome (Fiumicino) | FCO | S1 | 06/09/2026 | Dimanche | 233 | 2026-09-03 | 🔴 Forte baisse vs run précédent (358$→233$, -35%) |
| Tbilissi | TBS | S1 | 06/09/2026 | Dimanche | 366 | 2026-09-03 | 🔴 Forte baisse vs run précédent (587$→366$, -38%) — 8 options directes trouvées (vs 4 le run précédent, toujours moins que les 15 des autres destinations) |
| Vienne | VIE | S1 | 06/09/2026 | Dimanche | 343 | 2026-09-03 | Stable vs run précédent (363$→343$, -6%) |
| Prague | PRG | S1 | 06/09/2026 | Dimanche | 384 | 2026-09-03 | Baisse vs run précédent (430$→384$, -11%) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-03 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Aucun gap — un résultat direct trouvé pour chacune des 7 destinations. 9 jours se sont écoulés depuis le run du 2026-08-25 (dernier relevé disponible) ; la comparaison ci-dessus se fait donc contre ce run-là. Baisse de prix généralisée sur les 7 destinations (-6% à -38%), cohérente avec le schéma déjà observé les runs précédents : la date de départ testée est plus éloignée (06/09 contre 30/08, soit +7 jours d'avance), ce qui sort les tarifs de dernière minute les plus chers. Deux écarts dépassent le seuil de 15 % et méritent confirmation : Rome/FCO (358$→233$, -35%) et Tbilissi/TBS (587$→366$, -38%). TBS reste la destination la moins bien desservie en direct (8 options ce run, vs 15 pour les 6 autres destinations) mais s'améliore par rapport aux 4 options du run du 25/08 — cohérent avec une offre TLV-TBS structurellement plus restreinte (Israir + Arkia + El Al), pas une anomalie de données. Budapest et Vienne sont restées stables (-6% chacune). À confirmer sur les prochains runs pour distinguer volatilité de dernière minute vs tendance de fond, en particulier pour FCO et TBS. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
