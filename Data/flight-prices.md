# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-08 (heure de ce run)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ lundi 14/09/2026 → retour jeudi 17/09/2026 (repli depuis dimanche 13/09/2026 — Roch Hachana, voir note ci-dessous)
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 30/08/2026 | Dimanche | 159 | 2026-08-25 | ⚠️ Forte baisse vs run précédent (364$→159$, -56%) |
| Paphos | PFO | S1 | 30/08/2026 | Dimanche | 176 | 2026-08-25 | ⚠️ Forte baisse vs run précédent (493$→176$, -64%) |
| Budapest | BUD | S1 | 30/08/2026 | Dimanche | 248 | 2026-08-25 | ⚠️ Forte baisse vs run précédent (566$→248$, -56%) |
| Rome (Fiumicino) | FCO | S1 | 30/08/2026 | Dimanche | 358 | 2026-08-25 | ⚠️ Forte baisse vs run précédent (561$→358$, -36%) |
| Tbilissi | TBS | S1 | 30/08/2026 | Dimanche | 587 | 2026-08-25 | ⚠️ Baisse vs run précédent (806$→587$, -27%) — seulement 4 options directes trouvées (vs 15 sur les autres destinations) |
| Vienne | VIE | S1 | 30/08/2026 | Dimanche | 363 | 2026-08-25 | ⚠️ Forte baisse vs run précédent (1284$→363$, -72%) — anomalie précédente résolue |
| Prague | PRG | S1 | 30/08/2026 | Dimanche | 430 | 2026-08-25 | ⚠️ Forte baisse vs run précédent (1723$→430$, -75%) — 15 options directes trouvées cette fois (vs 1 seule le run précédent), anomalie précédente résolue |
| Athènes | ATH | S3 | 14/09/2026 | Lundi (repli, Roch Hachana) | 166 | 2026-09-08 | Hausse légère vs run du 25/08 (159$→166$, +4%) — 15 options directes, rien d'anormal |
| Paphos | PFO | S3 | 14/09/2026 | Lundi (repli, Roch Hachana) | 170 | 2026-09-08 | Stable vs run du 25/08 (176$→170$, -3%) — 15 options directes |
| Budapest | BUD | S3 | 14/09/2026 | Lundi (repli, Roch Hachana) | 245 | 2026-09-08 | Stable vs run du 25/08 (248$→245$, -1%) — 15 options directes |
| Rome (Fiumicino) | FCO | S3 | 14/09/2026 | Lundi (repli, Roch Hachana) | 291 | 2026-09-08 | ⚠️ Baisse notable vs run du 25/08 (358$→291$, -19%, > seuil 15%) — 15 options directes, rien d'anormal dans la donnée |
| Tbilissi | TBS | S3 | 14/09/2026 | Lundi (repli, Roch Hachana) | 658 | 2026-09-08 | ⚠️ Hausse vs run du 25/08 (587$→658$, +12%) — seulement 3 options directes trouvées (vs 15 sur les autres destinations, vs 4 le run précédent) — cohérent avec l'offre directe TLV-TBS structurellement restreinte (Israir + El Al), pas une anomalie de données |
| Vienne | VIE | S3 | 14/09/2026 | Lundi (repli, Roch Hachana) | 338 | 2026-09-08 | Baisse vs run du 25/08 (363$→338$, -7%) — 15 options directes |
| Prague | PRG | S3 | 14/09/2026 | Lundi (repli, Roch Hachana) | 303 | 2026-09-08 | ⚠️ Forte baisse vs run du 25/08 (430$→303$, -30%, > seuil 15%) — 15 options directes, rien d'anormal dans la donnée |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-08 (ce run) | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | 14 jours se sont écoulés depuis le run du 2026-08-25 (le trigger quotidien officiel `trig_01AC9Z8TrgTpLToieNmSJ6G4` tourne à vide faute d'accès aux connecteurs — voir `ROUTINE_PROMPT.md`), donc pas de série quotidienne continue pour distinguer volatilité court terme et tendance de fond sur cette période. Fenêtre testée : dimanche 13/09/2026 tombe pendant Roch Hachana (constat déjà noté au run du 26/08 sur cette même semaine, alors identifiée S3) → repli lundi 14/09 → jeudi 17/09, conformément à la règle métier (jamais de vol Shabbat/fête). Deux baisses dépassent le seuil d'alerte de 15 % vs le run du 25/08 : Prague (430$→303$, -30%) et Rome/FCO (358$→291$, -19%) — dans les deux cas 15 options directes trouvées, rien d'anormal dans la donnée elle-même (pas d'option unique ni de compagnie suspecte), à confirmer sur les prochains runs pour distinguer un vrai repli tarifaire d'un effet de fenêtre de réservation plus éloignée (+20 jours vs le run du 25/08, contre +5 jours l'écart précédent). Tbilissi confirme son profil structurel : seulement 3 options directes cette fois (Israir + El Al, en baisse même vs les 4 du run du 20/08), prix en hausse de 12% (587$→658$) — cohérent avec une offre directe restreinte sur cette route, pas un signal de donnée corrompue. Les 5 autres destinations (ATH, PFO, BUD, VIE) restent dans une fourchette de ±7% du run précédent, sans anomalie. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
