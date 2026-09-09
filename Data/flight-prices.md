# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-09 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 13/09/2026 → retour mercredi 16/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations. Dimanche 13/09 tombe pendant Roch Hachana (11-13/09) mais des vols directs restent disponibles ce jour-là sur les 7 destinations — pas de repli lundi nécessaire cette fois.

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
| Rome (Fiumicino) | FCO | S3 | 13/09/2026 | Dimanche | 234 | 2026-09-09 | Baisse vs S1 30/08 (358$→234$, -35%) |
| Paphos | PFO | S3 | 13/09/2026 | Dimanche | 127 | 2026-09-09 | Baisse vs S1 30/08 (176$→127$, -28%) |
| Athènes | ATH | S3 | 13/09/2026 | Dimanche | 149 | 2026-09-09 | Stable vs S1 30/08 (159$→149$, -6%) |
| Prague | PRG | S3 | 13/09/2026 | Dimanche | 317 | 2026-09-09 | Baisse vs S1 30/08 (430$→317$, -26%) |
| Vienne | VIE | S3 | 13/09/2026 | Dimanche | 375 | 2026-09-09 | Stable vs S1 30/08 (363$→375$, +3%) |
| Tbilissi | TBS | S3 | 13/09/2026 | Dimanche | 523 | 2026-09-09 | Baisse vs S1 30/08 (587$→523$, -11%) — 12 options directes trouvées (vs 15 sur les autres destinations, hors Budapest à 10) |
| Budapest | BUD | S3 | 13/09/2026 | Dimanche | 661 | 2026-09-09 | 🔴 ANOMALIE — forte hausse vs S1 30/08 (248$→661$, +167%). Seulement 10 options directes trouvées (vs 12-15 ailleurs), toutes ≥ 661$ (Wizz Air/Israir). À confirmer sur le run suivant : ne pas exclure un effet Roch Hachana + rentrée scolaire hongroise sur cette date précise plutôt qu'une tendance de fond. |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-09 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) — S3, départ dimanche 13/09/2026, retour mercredi 16/09/2026 | Vols directs disponibles pour les 7 destinations malgré Roch Hachana (11-13/09) le jour même du départ — pas de repli lundi nécessaire. Six destinations sur sept baissent ou restent stables vs le relevé S1 du 30/08 (ATH -6%, VIE +3%, TBS -11%, PRG -26%, PFO -28%, FCO -35%). **Budapest (BUD) est une anomalie nette : 248$ (30/08) → 661$ (13/09), +167%**, avec seulement 10 options directes trouvées contre 12-15 pour les autres destinations, toutes déjà ≥ 661$ sans option basse — ce n'est pas un effet d'arrondi sur une seule offre. Piste la plus probable : Roch Hachana tombe précisément sur la date de départ testée, ce qui peut réduire la disponibilité low-cost Wizz Air sur cette ligne (moins d'A/R proposés autour d'une fête) plutôt qu'une hausse structurelle du prix Budapest. À confirmer sur le prochain run avant d'ajuster tout prix package publié sur cette destination — ne pas trancher sur un seul point de données. Note : comparaison faite contre le S1 (30/08) faute de relevé S2 (06/09) intermédiaire dans l'historique de ce fichier — deux semaines et demie d'écart, donc une partie du mouvement peut aussi tenir au calendrier plutôt qu'au marché. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
