# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-27 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 30/08/2026 → retour mercredi 02/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour 6/7 destinations. TBS : 0 itinéraire direct trouvé pour le couple exact 30/08→02/09 (voir anomalie ci-dessous) ; le connecteur répond normalement (des vols directs existent sur d'autres dates de la même semaine)

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
| Athènes | ATH | S1 | 30/08/2026 | Dimanche | 159 | 2026-08-27 | Stable vs run précédent (159$→159$, 0%) — 15 options directes |
| Paphos | PFO | S1 | 30/08/2026 | Dimanche | 155 | 2026-08-27 | Légère baisse vs run précédent (176$→155$, -12%) — 15 options directes |
| Budapest | BUD | S1 | 30/08/2026 | Dimanche | 236 | 2026-08-27 | Légère baisse vs run précédent (248$→236$, -5%) — 15 options directes |
| Rome (Fiumicino) | FCO | S1 | 30/08/2026 | Dimanche | 415 | 2026-08-27 | Hausse vs run précédent (358$→415$, +16%) — 15 options directes, à surveiller mais pas alarmant |
| Tbilissi | TBS | S1 | 30/08/2026 | Dimanche | **N/A** | 2026-08-27 | 🚨 ANOMALIE — 0 itinéraire direct A/R trouvé pour le couple exact 30/08→02/09 (587$/4 options le run précédent). Des vols directs TLV-TBS existent bien cette semaine-là (Israir/El Al/Arkia, ~30/08 au 03/09) mais aucune paire directe aller+retour ne tombe exactement sur 30/08→02/09 — la correspondance retour directe du mercredi 02/09 est absente. Alternative directe la plus proche trouvée : dép. 30/08 22:30 (Israir) / retour 03/09 00:35 (4 nuits) à 525$, ou dép. 31/08 / retour 03/09 (3 nuits) à 543$. À reverifier demain pour voir si c'est une fenêtre d'horaires qui se comble ou une réduction durable de fréquence directe. |
| Vienne | VIE | S1 | 30/08/2026 | Dimanche | 341 | 2026-08-27 | Légère baisse vs run précédent (363$→341$, -6%) — 15 options directes |
| Prague | PRG | S1 | 30/08/2026 | Dimanche | 433 | 2026-08-27 | Stable vs run précédent (430$→433$, +0.7%) — 15 options directes |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-27 03:33 | PRG, VIE, FCO, PFO, ATH, BUD (6/6 avec prix) ; TBS (0 itinéraire direct pour le couple exact de dates) | Les prix se stabilisent nettement par rapport aux run précédents : mouvements de -12% à +16% seulement (ATH stable, PFO -12%, BUD -5%, VIE -6%, PRG +0.7%, FCO +16%), cohérent avec l'hypothèse de la veille (le run initial du 20/08 souffrait d'un effet dernière-minute, désormais résorbé). Seule exception notable : FCO +16% (358$→415$), à surveiller sans être alarmant à ce stade. **Anomalie principale du jour : TBS.** Aucun itinéraire direct A/R trouvé pour le couple exact départ dimanche 30/08 / retour mercredi 02/09, alors que le run précédent avait trouvé 4 options directes à 587$. Vérification complémentaire : des vols directs TLV-TBS existent bien cette semaine (Israir 6H895/6H897, El Al LY5109, Arkia IZ1417 à l'aller ; Israir 6H896/6H900, Arkia IZ418, El Al LY5418 au retour), mais aucune combinaison directe aller+retour ne tombe pile sur 30/08→02/09 — la rotation retour directe du mercredi 02/09 semble absente ce jour-là précisément. Alternative directe la plus proche : dép. 30/08 soir / retour 03/09 (4 nuits) à 525$, ou dép. 31/08 / retour 03/09 (3 nuits) à 543$. Cette route reste structurellement la plus fragile du groupe (Israir/El Al/Arkia uniquement, faible fréquence) — à reconfirmer sur le run de demain pour distinguer un simple trou d'horaire ponctuel d'une réduction de fréquence plus durable. | OK (TBS : réponse connecteur normale, 0 résultat pour la contrainte exacte de dates — pas une panne) |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
