# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-02 (heure de génération du run)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 06/09/2026 → retour mercredi 09/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 06/09/2026 | Dimanche | 137 | 2026-09-02 | ⚠️ Baisse vs run précédent (159$→137$, -14%) — 15 options directes |
| Paphos | PFO | S1 | 06/09/2026 | Dimanche | 159 | 2026-09-02 | Baisse vs run précédent (176$→159$, -10%) — 15 options directes |
| Budapest | BUD | S1 | 06/09/2026 | Dimanche | 234 | 2026-09-02 | Baisse vs run précédent (248$→234$, -6%) — 15 options directes |
| Rome (Fiumicino) | FCO | S1 | 06/09/2026 | Dimanche | 233 | 2026-09-02 | ⚠️ Forte baisse vs run précédent (358$→233$, -35%) — 15 options directes, dont Wizz Air direct désormais moins chère que l'aller-retour Arkia/Israir |
| Tbilissi | TBS | S1 | 06/09/2026 | Dimanche | 405 | 2026-09-02 | ⚠️ Forte baisse vs run précédent (587$→405$, -31%) — 8 options directes trouvées (vs 4 le run précédent), Israir/Arkia/El Al |
| Vienne | VIE | S1 | 06/09/2026 | Dimanche | 361 | 2026-09-02 | Stable vs run précédent (363$→361$, -1%) — 15 options directes |
| Prague | PRG | S1 | 06/09/2026 | Dimanche | 392 | 2026-09-02 | Baisse vs run précédent (430$→392$, -9%) — 15 options directes |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-02 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse généralisée mais plus modérée que le run du 2026-08-25, avec deux mouvements sortant du lot : FCO -35% (358$→233$, Wizz Air direct désormais la moins chère dans les deux sens) et TBS -31% (587$→405$, et le nombre d'options directes remonte de 4 à 8 — Arkia (IZ417/IZ1418) apparaît en plus d'Israir et El Al, cohérent avec une meilleure disponibilité tarifaire plutôt qu'une anomalie de données). Les cinq autres destinations bougent de -1% (VIE) à -14% (ATH), dans la fourchette de volatilité normale déjà observée. Aucun gap : les 7 destinations ont renvoyé des résultats directs des deux côtés (15 options sur 6 destinations, 8 sur TBS). Rien à signaler comme anomalie de données — TBS reste structurellement la route la plus chère et la moins desservie du groupe, comme noté depuis le premier run. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
