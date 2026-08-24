# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-24 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 30/08/2026 → retour mercredi 02/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour les 7 destinations

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 30/08/2026 | Dimanche | 171 | 2026-08-24 | OK |
| Paphos | PFO | S1 | 30/08/2026 | Dimanche | 176 | 2026-08-24 | OK |
| Tbilissi | TBS | S1 | 30/08/2026 | Dimanche | 206 | 2026-08-24 | OK |
| Budapest | BUD | S1 | 30/08/2026 | Dimanche | 237 | 2026-08-24 | OK |
| Rome (Fiumicino) | FCO | S1 | 30/08/2026 | Dimanche | 303 | 2026-08-24 | OK |
| Vienne | VIE | S1 | 30/08/2026 | Dimanche | 371 | 2026-08-24 | OK |
| Prague | PRG | S1 | 30/08/2026 | Dimanche | 439 | 2026-08-24 | OK — 15 options directes trouvées (vs 1 seule le 2026-08-20), anomalie précédente résolue |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-24 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | ⚠️ Baisse de prix générale et uniforme vs le run du 2026-08-20 : ATH -53% (364→171), PFO -64% (493→176), BUD -58% (566→237), FCO -46% (561→303), TBS -74% (806→206), VIE -71% (1284→371), PRG -75% (1723→439). Toutes les 7 destinations baissent dans une fourchette de -46% à -75%, ce qui pointe vers un effet de fenêtre de réservation plutôt que 7 baisses de marché indépendantes : le run du 20/08 vérifiait un départ à J+3 (23/08, tarifs de dernière minute, capacité restreinte notamment sur EL AL/Arkia), alors que ce run vérifie un départ à J+6 (30/08). Cohérent avec la résolution de l'anomalie PRG signalée le 20/08 (une seule option directe à 1723$) : ce run trouve 15 options directes sur TLV-PRG entre 439$ et 1051$, confirmant que c'était bien un effet de rareté de dernière minute et non un problème structurel de la route. Aucun outlier interne ce run-ci (classement cohérent avec le run précédent : ATH/PFO moins chers, PRG/VIE plus chers). Recommandation : comparer les prix jour après jour à fenêtre de réservation comparable (même nombre de jours avant départ) pour un suivi de tendance fiable — sinon les variations J-3 vs J-6 dominent le signal. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
