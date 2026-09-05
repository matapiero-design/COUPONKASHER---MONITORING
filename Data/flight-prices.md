# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-05 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 06/09/2026 → retour mercredi 09/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations
- **Note sur ce run** : recherche effectuée la veille du départ testé (05/09 pour un départ le 06/09) — fenêtre de réservation nettement plus courte que le run du 25/08 (qui testait 5 jours d'avance). Comparer les prix ci-dessous au run précédent revient donc en partie à comparer deux fenêtres de réservation différentes, pas seulement deux dates différentes. À garder en tête pour la lecture des écarts.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 06/09/2026 | Dimanche | 108 | 2026-09-05 | ⚠️ Forte baisse vs run précédent (159$→108$, -32%) — 15 options directes |
| Paphos | PFO | S1 | 06/09/2026 | Dimanche | 139 | 2026-09-05 | ⚠️ Baisse vs run précédent (176$→139$, -21%) — 15 options directes |
| Budapest | BUD | S1 | 06/09/2026 | Dimanche | 261 | 2026-09-05 | Hausse légère vs run précédent (248$→261$, +5%) — 15 options directes |
| Rome (Fiumicino) | FCO | S1 | 06/09/2026 | Dimanche | 222 | 2026-09-05 | ⚠️ Forte baisse vs run précédent (358$→222$, -38%) — 15 options directes |
| Tbilissi | TBS | S1 | 06/09/2026 | Dimanche | 391 | 2026-09-05 | ⚠️ Forte baisse vs run précédent (587$→391$, -33%) — seulement 8 options directes trouvées (vs 15 sur les autres destinations), cohérent avec l'offre directe TLV-TBS structurellement plus restreinte (Israir, Arkia, El Al) |
| Vienne | VIE | S1 | 06/09/2026 | Dimanche | 342 | 2026-09-05 | Baisse vs run précédent (363$→342$, -6%) — 15 options directes |
| Prague | PRG | S1 | 06/09/2026 | Dimanche | 309 | 2026-09-05 | ⚠️ Forte baisse vs run précédent (430$→309$, -28%) — 15 options directes |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-05 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Premier run depuis le 25/08 (11 jours sans mise à jour — voir ROUTINE_PROMPT.md, blocage connecteur sur le trigger automatique non résolu ; ce run a été déclenché manuellement/hors trigger). Baisse marquée sur 5 destinations sur 7 vs le run du 25/08 : ATH -32% (159$→108$), PFO -21% (176$→139$), FCO -38% (358$→222$), TBS -33% (587$→391$), PRG -28% (430$→309$). VIE en léger repli (-6%, 363$→342$). Seul BUD monte légèrement (+5%, 248$→261$). Point de vigilance méthodologique : ce run teste un départ à J+1 (06/09 recherché le 05/09), contre J+5 pour le run du 25/08 (30/08 recherché le 25/08) — une fenêtre de réservation plus courte se traduit d'ordinaire par des tarifs plus élevés (moins de classes tarifaires basses disponibles), pas plus bas. Voir une majorité de baisses malgré une réservation plus tardive va à l'encontre de ce schéma et pourrait signaler un dégagement de sièges invendus sur des vols de milieu de semaine plutôt qu'une vraie tendance de marché — à confirmer sur les prochains runs quotidiens avant de considérer ces niveaux comme la nouvelle base. TBS confirme sa restriction structurelle (8 options directes vs 15 pour les autres destinations, cohérent avec les runs précédents). Aucune anomalie de type gap de données (toutes les destinations ont retourné des résultats directs multiples). | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
