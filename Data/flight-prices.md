# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-12 (heure de ce run) UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 13/09/2026 → retour mercredi 16/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations
- **⚠️ Gap de suivi** : aucun run enregistré entre le 2026-08-25 et ce run (18 jours d'écart). Cohérent avec le problème connu documenté dans `ROUTINE_PROMPT.md` (le trigger quotidien automatisé n'a pas accès aux connecteurs Kiwi.com/Booking.com tant que la Routine n'est pas recréée depuis l'UI claude.ai/routines) — à vérifier auprès de Jacques.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 13/09/2026 | Dimanche | 139 | 2026-09-12 | Baisse vs run précédent (159$→139$, -13%) — 15 options directes |
| Paphos | PFO | S1 | 13/09/2026 | Dimanche | 121 | 2026-09-12 | Baisse vs run précédent (176$→121$, -31%) — 15 options directes |
| Budapest | BUD | S1 | 13/09/2026 | Dimanche | 994 | 2026-09-12 | 🚨 ANOMALIE — forte hausse vs run précédent (248$→994$, +301%), confirmée en EUR (856€, conversion cohérente, pas un bug de devise) — 15 options directes toutes dans la fourchette 994-1200$, ce n'est pas une option isolée. Departure très rapprochée (J+1, le run est tombé un samedi) + période Roch Hachana (11-13/09/2026) probable explication : forte demande de sortie d'Israël sur une route à capacité limitée (Wizz Air + Israir uniquement). À confirmer sur le run suivant avant de publier un prix. |
| Rome (Fiumicino) | FCO | S1 | 13/09/2026 | Dimanche | 232 | 2026-09-12 | Baisse vs run précédent (358$→232$, -35%) — 15 options directes |
| Tbilissi | TBS | S1 | 13/09/2026 | Dimanche | 467 | 2026-09-12 | Baisse vs run précédent (587$→467$, -20%) — seulement 8 options directes trouvées (vs 15 sur les autres destinations), cohérent avec l'offre TLV-TBS structurellement plus restreinte notée aux runs précédents |
| Vienne | VIE | S1 | 13/09/2026 | Dimanche | 342 | 2026-09-12 | Baisse vs run précédent (363$→342$, -6%) — 15 options directes |
| Prague | PRG | S1 | 13/09/2026 | Dimanche | 271 | 2026-09-12 | Baisse vs run précédent (430$→271$, -37%) — 13 options directes |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-12 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Aucun run enregistré depuis le 2026-08-25 (18 jours d'écart) — probablement lié au trigger quotidien sans accès connecteur documenté dans `ROUTINE_PROMPT.md`, à confirmer avec Jacques. Départ testé cette fois à J+1 (13/09/2026, le run tombant un samedi) au lieu des 3-5 jours d'avance habituels. Baisse générale sur 6 destinations sur 7 (-6% à -37%), cohérente avec des fenêtres de réservation variables. **Anomalie majeure sur Budapest (BUD) : 248$→994$ (+301%)**, confirmée en EUR (856€), 15 options toutes dans la même fourchette haute (994-1200$) — pas un artefact d'une seule offre. Coïncide avec Roch Hachana (11-13/09/2026), période de forte demande de vols sortants d'Israël, combinée à une route à capacité restreinte (Wizz Air + Israir). Tbilissi (TBS) reste à seulement 8 options directes (vs 15 ailleurs), cohérent avec les runs précédents. Prix non publiés sur le site avant confirmation. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
