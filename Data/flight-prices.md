# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-06 03:34 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ lundi 14/09/2026 → retour jeudi 17/09/2026 (repli depuis dimanche 13/09 : Roch Hachana 5787 tombe vendredi 11/09 au soir → dimanche 13/09 au soir, le départ dominical par défaut est donc en plein Yom Tov)
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 159 | 2026-09-06 | ✅ Stable vs run précédent (159$→159$, 0%) — 15 options directes |
| Paphos | PFO | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 170 | 2026-09-06 | ✅ Stable vs run précédent (176$→170$, -3%) — 15 options directes |
| Budapest | BUD | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 263 | 2026-09-06 | ↗️ Hausse vs run précédent (248$→263$, +6%) — 15 options directes |
| Rome (Fiumicino) | FCO | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 324 | 2026-09-06 | ↘️ Baisse vs run précédent (358$→324$, -9%) — 15 options directes |
| Tbilissi | TBS | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 674 | 2026-09-06 | ⚠️ Hausse vs run précédent (587$→674$, +15%) — seulement 4 options directes trouvées (vs 15 sur les autres destinations), comme à chaque run précédent : offre TLV-TBS structurellement restreinte (Israir + El Al uniquement), pas une anomalie de données mais à surveiller car proche du seuil d'alerte de 15 % |
| Vienne | VIE | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 337 | 2026-09-06 | ↘️ Baisse vs run précédent (363$→337$, -7%) — 15 options directes |
| Prague | PRG | S3 | 14/09/2026 | Lundi (repli Roch Hachana) | 338 | 2026-09-06 | ↘️ Baisse vs run précédent (430$→338$, -21%) — 15 options directes |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-06 03:34 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Premier run depuis le 2026-08-25 (12 jours d'écart — ce fichier n'avait pas suivi le passage du pipeline au prix package vol+hôtel, voir `Data/package-prices.md`). Départ testé décalé au **lundi 14/09** (repli) : le dimanche 13/09 par défaut tombe en plein Roch Hachana (5787, vendredi 11/09 soir → dimanche 13/09 soir), donc écarté conformément à la règle métier du skill `dashboard-suivi-prix-sejours-casher` (jamais de vol en Yom Tov). Comparaison aux 7 valeurs du run du 2026-08-25 : baisses sur PRG (-21%), VIE (-7%), FCO (-9%) et PFO (-3%), quasi-stable sur ATH (0%), légère hausse sur BUD (+6%). **Tbilissi (TBS) : +15% (587$→674$)** — juste sous/au seuil d'alerte de 15 % retenu par le pipeline package ; seulement 4 options directes trouvées comme à chaque run précédent (contre 15 pour les 6 autres destinations), cohérent avec l'offre TLV-TBS structurellement restreinte (Israir + El Al) plutôt qu'une anomalie de données, mais à confirmer sur le prochain run avant de conclure à une tendance de fond. Aucune autre destination au-delà du seuil. Note de méthode : le run précédent testait un départ dimanche à 5 jours d'avance, celui-ci un départ lundi à 8 jours d'avance — l'écart de calendrier et le changement de jour de semaine limitent la comparabilité stricte, comme observé sur les runs antérieurs (effet date/dernière-minute déjà documenté). | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
