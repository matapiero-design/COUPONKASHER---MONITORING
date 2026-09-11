# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-11 03:35 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits. Départ dimanche par défaut, mais le dimanche 13/09/2026 (S3) tombe en plein Roch Hachana 5787 (vendredi 11/09 soir → dimanche 13/09 soir) — repli lundi 14/09 → jeudi 17/09 appliqué sur 6 destinations, voir anomalie TBS ci-dessous
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations (TBS sur une fenêtre différente, voir Journal des runs)

## Prix vols directs — Groupe A (S3 — run 2026-09-11)

| Destination | Aéroport | Semaine | Date départ | Jour | Date retour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|---|
| Athènes | ATH | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 17/09/2026 | 153 | 2026-09-11 | ↘ Baisse légère vs run précédent (159$→153$, -4%) |
| Paphos | PFO | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 17/09/2026 | 128 | 2026-09-11 | ↘ Baisse (176$→128$, -27%) |
| Budapest | BUD | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 17/09/2026 | 258 | 2026-09-11 | → Stable vs run précédent (248$→258$, +4%) |
| Rome (Fiumicino) | FCO | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 17/09/2026 | 331 | 2026-09-11 | ↘ Baisse (358$→331$, -8%) |
| Vienne | VIE | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 17/09/2026 | 316 | 2026-09-11 | ↘ Baisse (363$→316$, -13%) |
| Prague | PRG | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 17/09/2026 | 304 | 2026-09-11 | ↘ Baisse (430$→304$, -29%) |
| Tbilissi | TBS | S3 | 15/09/2026 | Mardi (voir anomalie) | 18/09/2026 | 692 | 2026-09-11 | ⚠️ Anomalie — voir Journal des runs |

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

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-11 03:35 | PRG, VIE, FCO, PFO, ATH, BUD (6/6 sur 14/09→17/09), TBS (1/1 sur 15/09→18/09) | **TBS — anomalie de disponibilité + de prix.** Aucun vol direct trouvé au départ du lundi 14/09 (0 résultat sur le code TBS et sur la ville « Tbilisi », requêtes 0 escale) : élargissement de la fenêtre confirmant que le direct TLV-TBS (Arkia/Israir) n'opère pas tous les jours — direct confirmé uniquement dimanche 13/09, mardi 15/09, jeudi 17/09, samedi 19/09 sur la période testée. Le dimanche 13/09 tombe en Roch Hachana (à éviter) et aucun direct n'existe le lundi 14/09 ni le mercredi 16/09 : repli retenu sur mardi 15/09 → vendredi 18/09 (3 nuits, direct confirmé aller et retour, atterrissage retour 03:45-11:50 selon l'option — largement avant Chabbat). Prix obtenu 692$, soit +18% vs le dernier prix TBS connu (587$ au 25/08, sur des dates différentes) — cohérent avec l'historique de cette route (offre directe restreinte, Israir + Arkia/El Al uniquement) plutôt qu'une anomalie de données, mais l'écart de fenêtre (mar→ven au lieu de dim→mer) casse la comparabilité stricte avec les runs précédents : à fiabiliser sur les prochains runs quotidiens une fois Roch Hachana passé. — Sur les 6 autres destinations (14/09 lundi → 17/09 jeudi, repli Roch Hachana appliqué uniformément) : baisses de prix généralisées et cohérentes vs le run du 25/08 (-4% ATH à -29% PRG), aucune ne dépasse le seuil d'anomalie observé lors des runs précédents (>50%) — mouvement de marché normal, pas de gap de données. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
