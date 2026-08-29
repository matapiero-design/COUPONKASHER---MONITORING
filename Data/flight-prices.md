# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-29 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 30/08/2026 → retour mercredi 02/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 30/08/2026 | Dimanche | 129 | 2026-08-29 | Baisse vs run précédent (159$→129$, -19%) |
| Paphos | PFO | S1 | 30/08/2026 | Dimanche | 171 | 2026-08-29 | Stable vs run précédent (176$→171$, -3%) |
| Budapest | BUD | S1 | 30/08/2026 | Dimanche | 281 | 2026-08-29 | Hausse vs run précédent (248$→281$, +13%) |
| Vienne | VIE | S1 | 30/08/2026 | Dimanche | 342 | 2026-08-29 | Baisse vs run précédent (363$→342$, -6%) |
| Tbilissi | TBS | S1 | 30/08/2026 → 02/09/2026 | Dimanche→Mercredi | — | 2026-08-29 | 🚨 ANOMALIE — aucun vol direct A/R sur ce couple de dates : 15 options directes à l'aller (30/08) mais **zéro retour direct TBS→TLV le mercredi 02/09** (confirmé par une recherche dédiée retour-seul). Repli lundi 31/08 → jeudi 03/09 appliqué : 382$ direct (Israir 6H897 / 6H900), à comparer aux 587$ du run précédent (qui portait sur le même couple Dim→Mer, alors faisable). La ligne directe TBS semble avoir perdu sa rotation du mercredi cette semaine — à reconfirmer demain avant de conclure à un changement d'horaire durable |
| Rome (Fiumicino) | FCO | S1 | 30/08/2026 | Dimanche | 389 | 2026-08-29 | Hausse vs run précédent (358$→389$, +9%) |
| Prague | PRG | S1 | 30/08/2026 | Dimanche | 434 | 2026-08-29 | Stable vs run précédent (430$→434$, +1%) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-29 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, 6/7 sur le couple de dates Dim→Mer standard) | TBS est la seule anomalie du run : aucun vol retour direct TBS→TLV le mercredi 02/09/2026 (vérifié par une recherche one-way dédiée, résultat vide), alors que l'aller TLV→TBS du dimanche 30/08 a bien 15 options directes. Le prochain retour direct disponible est le jeudi 03/09 à 00h35 (Israir). Prix retenu par repli lundi 31/08 → jeudi 03/09 : 382$ (-35% vs les 587$ du run du 25/08, mais la comparaison n'est pas homogène — l'ancien prix portait sur le couple Dim→Mer, qui n'existe plus cette semaine). Sur les 6 autres destinations, mouvements de prix ordinaires (-19% à +13%), aucun ne franchit le seuil de 15%. Budapest (+13%, 248$→281$) et Rome (+9%, 358$→389$) sont les hausses les plus notables mais restent sous le seuil. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
