# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-10 (run automatisé)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits. Départ dimanche par défaut, mais le dimanche 13/09/2026 (S3) est le 2ème jour de Roch Hachana — repli sur lundi 14/09/2026 → retour jeudi 17/09/2026, conformément à la règle déjà actée dans `ROUTINE_PROMPT.md` ("Roch Hachana retire le départ dominical de S3 (repli lundi 14/09)").
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Paphos | PFO | S3 | 14/09/2026 | Lundi (repli, RH le 13/09) | 142 | 2026-09-10 | ⚠️ Baisse vs run précédent (176$→142$, -19%) |
| Athènes | ATH | S3 | 14/09/2026 | Lundi (repli, RH le 13/09) | 164 | 2026-09-10 | Stable vs run précédent (159$→164$, +3%) |
| Budapest | BUD | S3 | 14/09/2026 | Lundi (repli, RH le 13/09) | 270 | 2026-09-10 | Stable vs run précédent (248$→270$, +9%) |
| Prague | PRG | S3 | 14/09/2026 | Lundi (repli, RH le 13/09) | 304 | 2026-09-10 | ⚠️ Baisse vs run précédent (430$→304$, -29%) |
| Vienne | VIE | S3 | 14/09/2026 | Lundi (repli, RH le 13/09) | 317 | 2026-09-10 | ⚠️ Baisse vs run précédent (363$→317$, -13%) |
| Rome (Fiumicino) | FCO | S3 | 14/09/2026 | Lundi (repli, RH le 13/09) | 351 | 2026-09-10 | Stable vs run précédent (358$→351$, -2%) |
| Tbilissi | TBS | S3 | 14/09/2026 | Lundi (repli, RH le 13/09) | 631 | 2026-09-10 | Hausse vs run précédent (587$→631$, +7%) — seulement 4 options directes trouvées (vs 15 sur les autres destinations), cohérent avec l'offre directe TLV-TBS structurellement restreinte (Israir/Arkia/El Al) déjà notée précédemment |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-10 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Départ dominical 13/09 (S3) écarté car 2ème jour de Roch Hachana — repli lundi 14/09 → jeudi 17/09, conformément à la règle actée le 26/08 dans `ROUTINE_PROMPT.md`. Mouvements de prix par rapport au run du 2026-08-25 (dates comparées non identiques : S1 30/08 vs S3 14/09, ~2 semaines d'écart, donc à lire comme tendance de marché plutôt que variation stricte à date égale) : baisses notables sur Prague (430$→304$, -29%) et Vienne (363$→317$, -13%) et Paphos (176$→142$, -19%) ; Athènes, Budapest, Rome quasi stables (±10%) ; Tbilissi en légère hausse (587$→631$, +7%), toujours avec seulement 4 options directes (Israir/Arkia/El Al) contre 15 pour les autres destinations — conforme au constat structurel déjà documenté, pas une anomalie de données. Aucune baisse ou hausse jugée aberrante (>50%) cette fois-ci. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
