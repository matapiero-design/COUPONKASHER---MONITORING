# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-30 03:32 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 06/09/2026 → retour mercredi 09/09/2026 (S2 — voir note ci-dessous sur le changement de semaine testée)
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

> **Note sur la fenêtre testée** : le run du 25/08 avait vérifié S1 (départ dimanche 30/08/2026).
> Le run d'aujourd'hui tombe précisément le 30/08/2026 — interroger un vol partant "aujourd'hui"
> n'a pas de sens pour un suivi tarifaire prospectif, donc ce run bascule sur **S2** (départ dimanche
> 06/09/2026 → retour mercredi 09/09/2026). Les écarts ci-dessous vs le run précédent combinent donc
> un effet date (S1→S2) et un effet temps (5 jours d'écart entre les deux relevés) — à interpréter
> comme un indicateur de tendance, pas une comparaison strictement à fenêtre égale.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 30/08/2026 | Dimanche | 159 | 2026-08-25 | Historique — voir S2 ci-dessous pour le relevé le plus récent |
| Paphos | PFO | S1 | 30/08/2026 | Dimanche | 176 | 2026-08-25 | Historique — voir S2 ci-dessous pour le relevé le plus récent |
| Budapest | BUD | S1 | 30/08/2026 | Dimanche | 248 | 2026-08-25 | Historique — voir S2 ci-dessous pour le relevé le plus récent |
| Rome (Fiumicino) | FCO | S1 | 30/08/2026 | Dimanche | 358 | 2026-08-25 | Historique — voir S2 ci-dessous pour le relevé le plus récent |
| Tbilissi | TBS | S1 | 30/08/2026 | Dimanche | 587 | 2026-08-25 | Historique — voir S2 ci-dessous pour le relevé le plus récent |
| Vienne | VIE | S1 | 30/08/2026 | Dimanche | 363 | 2026-08-25 | Historique — voir S2 ci-dessous pour le relevé le plus récent |
| Prague | PRG | S1 | 30/08/2026 | Dimanche | 430 | 2026-08-25 | Historique — voir S2 ci-dessous pour le relevé le plus récent |
| Athènes | ATH | S2 | 06/09/2026 | Dimanche | 152 | 2026-08-30 | ⚠️ -4 % vs S1 (159$→152$) — 15 options directes |
| Paphos | PFO | S2 | 06/09/2026 | Dimanche | 152 | 2026-08-30 | ⚠️ -14 % vs S1 (176$→152$) — 15 options directes |
| Budapest | BUD | S2 | 06/09/2026 | Dimanche | 228 | 2026-08-30 | ⚠️ -8 % vs S1 (248$→228$) — 15 options directes |
| Rome (Fiumicino) | FCO | S2 | 06/09/2026 | Dimanche | 243 | 2026-08-30 | ⚠️ Forte baisse vs S1 (358$→243$, -32 %) — 15 options directes, Wizz Air en tête |
| Vienne | VIE | S2 | 06/09/2026 | Dimanche | 361 | 2026-08-30 | -1 % vs S1 (363$→361$) — 15 options directes |
| Tbilissi | TBS | S2 | 06/09/2026 | Dimanche | 393 | 2026-08-30 | ⚠️ Forte baisse vs S1 (587$→393$, -33 %) mais reste le prix le plus élevé du groupe — seulement 8 options directes trouvées (vs 15 sur les autres destinations), cohérent avec l'offre directe TLV-TBS structurellement plus restreinte |
| Prague | PRG | S2 | 06/09/2026 | Dimanche | 402 | 2026-08-30 | -7 % vs S1 (430$→402$) — 15 options directes |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-30 03:32 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Run basculé sur S2 (départ 06/09) au lieu de S1 (départ 30/08 = date du run elle-même, non pertinente pour un suivi prospectif) — voir note en tête de fichier. Baisse généralisée sur les 7 destinations vs le relevé S1 du 25/08 (de -1 % pour VIE à -33 % pour TBS), à lire avec prudence puisque la fenêtre testée a changé en même temps que la date. Deux baisses sortent du lot et méritent un suivi resserré les prochains jours : FCO (358$→243$, -32 %, tirée par Wizz Air) et TBS (587$→393$, -33 %, mais reste la destination la plus chère du groupe avec seulement 8 options directes contre 15 ailleurs — cohérent avec l'offre TLV-TBS structurellement limitée à Arkia/Israir/El Al, pas une anomalie de données). Aucun gap : les 7 destinations ont renvoyé des résultats directs. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
