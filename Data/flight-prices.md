# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-13 (heure de ce run)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 20/09/2026 → retour mercredi 23/09/2026 (TBS : pas de direct dimanche disponible, repli lundi 21/09 → vendredi 25/09, voir Statut)
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations
- **⚠️ Écart de cadence** : aucun run enregistré entre le 2026-08-25 et aujourd'hui (19 jours d'écart) — la comparaison ci-dessous se fait donc contre un relevé vieux de 19 jours, pas contre « hier ». Cohérent avec le blocage connu documenté dans `ROUTINE_PROMPT.md` (trigger API sans connecteurs attachés) : à vérifier auprès de Jacques si la Routine automatisée tourne bien tous les jours.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 20/09/2026 | Dimanche | 273 | 2026-09-13 | ⚠️ Forte hausse vs dernier run (159$→273$, +72%) — écart de 19 jours entre les deux relevés, à confirmer sur le prochain run rapproché |
| Paphos | PFO | S1 | 20/09/2026 | Dimanche | 189 | 2026-09-13 | Légère hausse vs dernier run (176$→189$, +7%) — dans la variance normale |
| Budapest | BUD | S1 | 20/09/2026 | Dimanche | 369 | 2026-09-13 | ⚠️ Forte hausse vs dernier run (248$→369$, +49%) — écart de 19 jours entre les deux relevés, à confirmer sur le prochain run rapproché |
| Rome (Fiumicino) | FCO | S1 | 20/09/2026 | Dimanche | 417 | 2026-09-13 | Hausse vs dernier run (358$→417$, +16%) — juste au-dessus du seuil de 15 % |
| Tbilissi | TBS | S1 | 21/09/2026 (repli lundi) | Lundi | 676 | 2026-09-13 | ⚠️ Aucun vol direct dimanche 20/09 trouvé (0 résultat) — repli lundi appliqué selon la règle métier ; retour vendredi 25/09 (aucune option jeudi dans la fenêtre 3 nuits). Prix en hausse vs dernier run (587$→676$, +15%), non strictement comparable (jour de départ différent) |
| Vienne | VIE | S1 | 20/09/2026 | Dimanche | 410 | 2026-09-13 | Hausse vs dernier run (363$→410$, +13%) — dans la variance normale |
| Prague | PRG | S1 | 20/09/2026 | Dimanche | 582 | 2026-09-13 | ⚠️ Forte hausse vs dernier run (430$→582$, +35%) — écart de 19 jours entre les deux relevés, à confirmer sur le prochain run rapproché |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-13 (run manuel, écarts sur cadence) | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Premier run depuis le 2026-08-25 (19 jours d'écart — aucune donnée intermédiaire, à signaler à Jacques : cohérent avec le blocage de connecteurs sur le trigger automatisé documenté dans `ROUTINE_PROMPT.md`). Hausses generalisées vs ce dernier run : ATH +72% (159$→273$), BUD +49% (248$→369$), PRG +35% (430$→582$), FCO +16% (358$→417$), TBS +15% (587$→676$, non strictement comparable — voir ci-dessous), VIE +13% (363$→410$), PFO +7% (176$→189$). Rien ne permet de distinguer ici une vraie tendance de fond d'un simple effet de fenêtre de recherche différente (5 jours d'avance le 25/08 contre 7 jours d'avance aujourd'hui) vu l'absence de points intermédiaires — à surveiller sur les prochains runs rapprochés. **Anomalie structurelle TBS** : pour la première fois, aucun vol direct TLV-TBS le dimanche 20/09 (0 résultat, contre 4 options directes le run précédent sur un dimanche) ; élargissement de fenêtre confirme qu'aucun direct n'opère ce dimanche-là (repli lundi 21/09 appliqué, seule opérante). Peut être un creux ponctuel de la grille Israir/Arkia sur cette date précise plutôt qu'un arrêt de ligne — à confirmer. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
