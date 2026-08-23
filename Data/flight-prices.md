# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-23 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 30/08/2026 → retour mercredi 02/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Paphos | PFO | S1 | 30/08/2026 | Dimanche | 176 | 2026-08-23 | OK (↓ de 493$ le 2026-08-20) |
| Athènes | ATH | S1 | 30/08/2026 | Dimanche | 181 | 2026-08-23 | OK (↓ de 364$ le 2026-08-20) |
| Budapest | BUD | S1 | 30/08/2026 | Dimanche | 248 | 2026-08-23 | OK (↓ de 566$ le 2026-08-20) |
| Rome (Fiumicino) | FCO | S1 | 30/08/2026 | Dimanche | 303 | 2026-08-23 | OK (↓ de 561$ le 2026-08-20) |
| Vienne | VIE | S1 | 30/08/2026 | Dimanche | 422 | 2026-08-23 | ⚠️ Toujours élevé vs cluster PFO/ATH/BUD/FCO, mais ↓ de 1284$ le 2026-08-20 |
| Prague | PRG | S1 | 30/08/2026 | Dimanche | 439 | 2026-08-23 | ⚠️ Toujours le plus cher du cluster occidental, mais ↓ de 1723$ le 2026-08-20 — nettement plus d'options directes cette fois (15 vs 1) |
| Tbilissi | TBS | S1 | 30/08/2026 | Dimanche | 642 | 2026-08-23 | ⚠️ Constamment ~2-3x le reste du groupe (structurel — seuls El Al/Israir en direct, pas de low-cost), ↓ de 806$ le 2026-08-20 |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-23 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | **Anomalie notable — baisse générale et uniforme de 46% à 75% sur les 7 destinations** par rapport au run du 2026-08-20 (PRG 1723→439, VIE 1284→422, TBS 806→642, BUD 566→248, FCO 561→303, PFO 493→176, ATH 364→181). Explication la plus probable : le run du 2026-08-20 cherchait un vol à J+3 (départ 23/08, dernière minute), alors que ce run cherche un vol à J+7 (départ 30/08) — la prime "dernière minute" sur TLV semble donc très forte (jusqu'à ×3-4 sur certaines routes). À confirmer sur les prochains runs : si l'écart se stabilise à mesure que la fenêtre de réservation reste comparable (J+7 chaque semaine), c'est bien un effet lead-time et non une anomalie de données. PRG a aussi basculé de 1 seule option directe trouvée à 15 — la route TLV-PRG direct semble donc mieux desservie à J+7 qu'à J+3. Classement structurel inchangé : PFO/ATH/BUD/FCO forment un cluster bas (176-303$), VIE/PRG un palier intermédiaire (422-439$), TBS reste la plus chère (642$, seuls El Al/Israir en direct). | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
