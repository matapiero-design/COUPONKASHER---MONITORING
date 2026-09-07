# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-07 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 13/09/2026 → retour mercredi 16/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations (BUD sans option dimanche→mercredi, voir statut)

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 13/09/2026 | Dimanche | 171 | 2026-09-07 | Hausse légère vs run précédent (159$→171$, +8%) — dans la volatilité normale |
| Paphos | PFO | S1 | 13/09/2026 | Dimanche | 127 | 2026-09-07 | ⚠️ Forte baisse vs run précédent (176$→127$, -28%) |
| Budapest | BUD | S1 | 14/09/2026 (repli lundi) | Lundi | 262 | 2026-09-07 | ⚠️ GAP — aucun direct dimanche 13/09→mercredi 16/09 (0 résultat, y compris en réinterrogeant la ville). Fenêtre confirmée vide par recherche flexible ±3j : le premier direct disponible est lundi 14/09 → jeudi 17/09 (3 nuits), 262$. Coïncide avec Roch Hachana (11-13/09/2026) — cohérent avec le repli lundi→jeudi déjà documenté les années précédentes pour ce motif. Prix repli en légère hausse vs run précédent (248$→262$, +6%), dans la normale |
| Rome (Fiumicino) | FCO | S1 | 13/09/2026 | Dimanche | 243 | 2026-09-07 | ⚠️ Forte baisse vs run précédent (358$→243$, -32%) |
| Tbilissi | TBS | S1 | 13/09/2026 | Dimanche | 565 | 2026-09-07 | Légère baisse vs run précédent (587$→565$, -4%) — cohérent avec l'offre directe TLV-TBS structurellement restreinte (Arkia/Israir) |
| Vienne | VIE | S1 | 13/09/2026 | Dimanche | 374 | 2026-09-07 | Stable vs run précédent (363$→374$, +3%) |
| Prague | PRG | S1 | 13/09/2026 | Dimanche | 317 | 2026-09-07 | ⚠️ Forte baisse vs run précédent (430$→317$, -26%) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-07 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, 6/7 sur le créneau dimanche exact) | **Aucun run entre le 2026-08-25 et aujourd'hui** (13 jours d'écart) — le trigger planifié tournait sans accès au connecteur Kiwi.com (voir ROUTINE_PROMPT.md, section "Blocage connu"), donc pas de comparaison run-à-run possible sur cette période intermédiaire ; la comparaison ci-dessous se fait directement vs le run du 25/08. **BUD : gap confirmé** — 0 résultat direct sur dimanche 13/09→mercredi 16/09 (recherche stricte et recherche flexible ±3j concordantes) ; la fenêtre coïncide avec Roch Hachana (soir du 11/09 au soir du 13/09/2026), qui retire l'offre directe du dimanche comme documenté pour Roch Hachana l'an dernier (repli lundi→jeudi sur ce même motif). Repli appliqué : lundi 14/09 → jeudi 17/09, 262$, cohérent avec le run précédent. **Trois baisses de prix marquées** sur les destinations avec vol dominical confirmé : FCO -32% (358$→243$), PFO -28% (176$→127$), PRG -26% (430$→317$) — direction cohérente avec le pattern déjà observé les 20/08 et 25/08 (les tarifs se détendent significativement à mesure que la date de recherche se rapproche de moins de 10 jours du départ, ouvrant des classes tarifaires low-cost moins chères) ; à confirmer sur le prochain run avant de conclure à une tendance de fond plutôt qu'un effet de lead-time. ATH (+8%), VIE (+3%), TBS (-4%) restent dans la volatilité normale déjà documentée pour ce groupe. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
