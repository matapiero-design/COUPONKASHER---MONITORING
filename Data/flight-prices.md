# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-28 03:36 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 30/08/2026 → retour mercredi 02/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour 6/7 destinations. TBS : gap confirmé après ré-interrogation (voir Statut ci-dessous), pas un problème connecteur.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 30/08/2026 | Dimanche | 137 | 2026-08-28 | Baisse vs run précédent (159$→137$, -14%) — 15 options directes, Israir moins cher |
| Paphos | PFO | S1 | 30/08/2026 | Dimanche | 149 | 2026-08-28 | ⚠️ Forte baisse vs run précédent (176$→149$, -15%) |
| Budapest | BUD | S1 | 30/08/2026 | Dimanche | 282 | 2026-08-28 | Hausse vs run précédent (248$→282$, +14%) — Wizz Air toujours moins cher |
| Rome (Fiumicino) | FCO | S1 | 30/08/2026 | Dimanche | 389 | 2026-08-28 | Hausse vs run précédent (358$→389$, +9%) |
| Tbilissi | TBS | S1 | 30/08/2026 | Dimanche | — | 2026-08-28 | 🔴 GAP : aucun vol retour direct TBS→TLV le 02/09/2026 (0 résultat, confirmé sur flyTo=TBS, flyTo=Tbilisi, et recherche one-way TBS→TLV dédiée). L'aller TLV→TBS direct existe bien (Israir 6H895/6H891). Le prochain retour direct après le 02/09 est le 03/09 à 00h35 (Israir 6H900, 225$ one-way) — un jour d'écart. Précédemment 587$ le 2026-08-25 avec seulement 4 options RT ; l'offre directe du mercredi semble avoir disparu entre les deux runs. Aucun prix publiable cette fois — à surveiller demain pour voir si le retour du mercredi réapparaît. |
| Vienne | VIE | S1 | 30/08/2026 | Dimanche | 342 | 2026-08-28 | Baisse vs run précédent (363$→342$, -6%) — Blue Bird Airways moins cher |
| Prague | PRG | S1 | 30/08/2026 | Dimanche | 434 | 2026-08-28 | Stable vs run précédent (430$→434$, +1%) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-28 03:36 | PRG, VIE, FCO, PFO, ATH, BUD (6/7) ; TBS relevé mais sans prix publiable | Deux points notables : (1) **PFO** baisse de 15% (176$→149$), au-dessus du seuil de 15% habituellement utilisé pour signaler un écart — à confirmer que ce n'est pas une anomalie ponctuelle. (2) **TBS** : gap complet — plus aucun vol retour direct TBS→TLV le mercredi 02/09/2026 alors que le run du 25/08 avait trouvé 4 options RT à 587$ sur cette même date de retour. Vérifié à trois reprises (flyTo=TBS, flyTo=Tbilisi, recherche one-way TBS→TLV dédiée) : 0 résultat direct à chaque fois, donc pas un problème du connecteur — la ligne directe du mercredi semble avoir disparu de la grille entre les deux runs (le prochain retour direct est le jeudi 03/09 à 00h35, Israir 6H900). Les 5 autres destinations (ATH, BUD, FCO, VIE, PRG) restent dans une fourchette de variation normale (-14% à +14%) après la forte baisse généralisée du run du 25/08 — la période de volatilité de dernière minute semble se stabiliser. | OK (TBS : connecteur opérationnel, gap confirmé réel et non un défaut de données) |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
