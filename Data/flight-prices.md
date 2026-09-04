# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-04 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 06/09/2026 → retour mercredi 09/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S2 | 06/09/2026 | Dimanche | 108 | 2026-09-04 | ⚠️ Baisse vs run précédent (159$→108$, -32%) |
| Paphos | PFO | S2 | 06/09/2026 | Dimanche | 138 | 2026-09-04 | ⚠️ Baisse vs run précédent (176$→138$, -22%) |
| Budapest | BUD | S2 | 06/09/2026 | Dimanche | 235 | 2026-09-04 | Stable vs run précédent (248$→235$, -5%) |
| Rome (Fiumicino) | FCO | S2 | 06/09/2026 | Dimanche | 234 | 2026-09-04 | ⚠️ Forte baisse vs run précédent (358$→234$, -35%) |
| Tbilissi | TBS | S2 | 06/09/2026 | Dimanche | 400 | 2026-09-04 | ⚠️ Baisse vs run précédent (587$→400$, -32%) — seulement 8 options directes trouvées (vs 15 sur les autres destinations) |
| Vienne | VIE | S2 | 06/09/2026 | Dimanche | 342 | 2026-09-04 | Stable vs run précédent (363$→342$, -6%) |
| Prague | PRG | S2 | 06/09/2026 | Dimanche | 316 | 2026-09-04 | ⚠️ Baisse vs run précédent (430$→316$, -27%) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-04 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse généralisée sur les 7 destinations vs le run du 2026-08-25 (de -5 % pour Budapest à -35 % pour Rome), malgré un délai de réservation beaucoup plus court cette fois (2 jours avant le départ du 06/09, contre 5 jours avant le 30/08 lors du run précédent). Ceci contredit l'explication retenue le 25/08 (date de départ plus éloignée → tarifs de dernière minute évités) : le délai s'est raccourci et les prix ont quand même baissé. L'explication la plus probable est désormais saisonnière — le 30/08 était encore en pic de vacances d'été européennes, le 06/09 est post-rentrée scolaire dans plusieurs pays sources, donc la demande baisse sur l'ensemble des lignes directes TLV, indépendamment du délai de réservation. Cohérent avec la note de `Data/package-prices.md` sur Prague (hôtel à 1100$ en S2 contre 2026$ en S1, "le +79 % de S1 était bien le pic d'août, pas un prix structurel"). TBS reste l'exception structurelle avec seulement 8 options directes trouvées ce run (contre 15 pour les autres destinations, 4 lors du run du 20/08) — cohérent avec une offre directe TLV-TBS plus restreinte (Israir + Arkia sur cette fenêtre), pas une anomalie de données. À confirmer sur les prochains runs pour distinguer effet saisonnier de fond vs volatilité ponctuelle. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
