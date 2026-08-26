# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-26 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 30/08/2026 → retour mercredi 02/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations (TBS a nécessité une recherche par nuitées plutôt que par date de retour exacte, voir Journal des runs)

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 30/08/2026 | Dimanche | 160 | 2026-08-26 | Stable vs run précédent (159$→160$, +1%) |
| Paphos | PFO | S1 | 30/08/2026 | Dimanche | 155 | 2026-08-26 | ⚠️ Baisse vs run précédent (176$→155$, -12%) |
| Budapest | BUD | S1 | 30/08/2026 | Dimanche | 249 | 2026-08-26 | Stable vs run précédent (248$→249$, +0.4%) |
| Rome (Fiumicino) | FCO | S1 | 30/08/2026 | Dimanche | 416 | 2026-08-26 | ⚠️ Hausse vs run précédent (358$→416$, +16%) |
| Tbilissi | TBS | S1 | 30/08/2026 | Dimanche | 532 | 2026-08-26 | Baisse vs run précédent (587$→532$, -9%) — toujours seulement 4 options directes trouvées (Israir/El Al uniquement), cohérent avec une offre TLV-TBS structurellement restreinte |
| Vienne | VIE | S1 | 30/08/2026 | Dimanche | 364 | 2026-08-26 | Stable vs run précédent (363$→364$, +0.3%) |
| Prague | PRG | S1 | 30/08/2026 | Dimanche | 456 | 2026-08-26 | Hausse modérée vs run précédent (430$→456$, +6%) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-26 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Prix globalement stabilisés vs le run du 2026-08-25 (écarts de -12% à +16%, à comparer aux -27%/-75% du run précédent) — cohérent avec l'hypothèse d'un effet "dernière minute" qui se résorbe à mesure que la date de départ (30/08) reste fixe d'un run à l'autre pendant que la date du run se rapproche. Deux écarts à surveiller sans être alarmants : Rome (FCO) en hausse de +16% (358$→416$, le vol le moins cher hier — Wizz Air/Arkia à 358$ le 25/08 — n'était peut-être plus disponible ou reflétait un prix ponctuel) et Paphos (PFO) en baisse de -12% (176$→155$). Tbilissi (TBS) : la recherche par date de retour exacte (returnDate=02/09) n'a renvoyé aucun résultat direct (resultsCount=0) alors que la recherche équivalente par nuitées (nights_in_dst_from/to=3) a bien renvoyé 4 options directes à partir de 532$ — anomalie de comportement du connecteur sur cette route à surveiller plutôt qu'une vraie absence de vol direct dimanche ; nombre d'options directes toujours limité (4, Israir + El Al uniquement) contre 14-15 pour les autres destinations, cohérent avec les runs précédents. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
