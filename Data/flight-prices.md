# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-14 03:34 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 20/09/2026 → retour mercredi 23/09/2026 (sauf TBS, voir Statut : pas de direct dimanche → repli lundi 21/09 → jeudi 24/09)
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations
- **Trou de suivi signalé** : aucun run entre le 2026-08-25 et le 2026-09-14 (20 jours) — le connecteur était bien disponible aujourd'hui, cause du trou non déterminée depuis cette session (voir `ROUTINE_PROMPT.md`, section connecteurs non attachés à la Routine, pour un blocage connu de même nature).

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 20/09/2026 | Dimanche | 295 | 2026-09-14 | ⚠️ Forte hausse vs dernier run (159$→295$, +86%) |
| Paphos | PFO | S1 | 20/09/2026 | Dimanche | 210 | 2026-09-14 | ⚠️ Hausse vs dernier run (176$→210$, +19%) |
| Budapest | BUD | S1 | 20/09/2026 | Dimanche | 370 | 2026-09-14 | ⚠️ Forte hausse vs dernier run (248$→370$, +49%) |
| Rome (Fiumicino) | FCO | S1 | 20/09/2026 | Dimanche | 418 | 2026-09-14 | ⚠️ Hausse vs dernier run (358$→418$, +17%) |
| Tbilissi | TBS | S1 | 21/09/2026 | Lundi (repli) | 719 | 2026-09-14 | ⚠️ Hausse vs dernier run (587$→719$, +22%) — **aucun vol direct trouvé au départ dimanche 20/09** (0 résultat sur TBS et sur la ville « Tbilisi » ; confirmé par un balayage 18-27/09 : les directs TLV→TBS existent tous les autres jours de la semaine, sauf le dimanche). Repli lundi 21/09 → jeudi 24/09 appliqué, 4 options directes trouvées (Israir/Arkia/El Al) |
| Vienne | VIE | S1 | 20/09/2026 | Dimanche | 465 | 2026-09-14 | ⚠️ Forte hausse vs dernier run (363$→465$, +28%) |
| Prague | PRG | S1 | 20/09/2026 | Dimanche | 583 | 2026-09-14 | ⚠️ Forte hausse vs dernier run (430$→583$, +36%) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-14 03:34 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Reprise après un trou de 20 jours sans run (dernier run le 2026-08-25). Hausse de prix généralisée sur les 7 destinations vs le run du 2026-08-25 (de +17% pour FCO à +86% pour ATH) — mouvement inverse et de même ampleur que la forte baisse généralisée notée le 2026-08-25, sans cause structurelle identifiée à ce stade (l'horizon de réservation est comparable : 6 jours d'avance aujourd'hui contre 5 jours le 25/08). Aucune destination ne se distingue par une anomalie isolée cette fois — la hausse touche l'ensemble du groupe, donc probablement un effet de marché/saisonnalité plutôt qu'un problème de données ; à confirmer sur les prochains runs. Gap structurel découvert sur TBS : aucun vol direct TLV→TBS au départ un dimanche (0 résultat sur le code TBS et sur la ville, confirmé par un balayage 18-27/09/2026 qui montre des directs tous les autres jours). Repli lundi→jeudi appliqué comme prévu par la procédure ; à surveiller si ce trou dominical est permanent ou ponctuel à cette date précise. | OK |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
