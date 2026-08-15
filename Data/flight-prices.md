# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-15 03:33 UTC (run manuel de vérification, premier run avec le connecteur Kiwi.com opérationnel)
- **Portée du dernier run** : PRG, VIE, FCO, PFO, ATH, BUD, TBS — vols directs (0 escale), aller-retour, 3 nuits, départ dimanche 16/08/2026 (retour mercredi 19/08/2026)
- **Statut connecteur Kiwi.com** : ✅ Disponible et fonctionnel dans cette session

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S33 | 16/08/2026 | Dimanche | 1335 | 2026-08-15 | ⚠️ Prix élevé (voir anomalies) |
| Vienne | VIE | S33 | 16/08/2026 | Dimanche | 755 | 2026-08-15 | OK |
| Rome (Fiumicino) | FCO | S33 | 16/08/2026 | Dimanche | 410 | 2026-08-15 | OK |
| Paphos | PFO | S33 | 16/08/2026 | Dimanche | 332 | 2026-08-15 | OK |
| Athènes | ATH | S33 | 16/08/2026 | Dimanche | 320 | 2026-08-15 | OK |
| Budapest | BUD | S33 | 16/08/2026 | Dimanche | 562 | 2026-08-15 | OK |
| Tbilissi | TBS | S33 | 16/08/2026 | Dimanche | 950 | 2026-08-15 | OK (route longue, prix cohérent avec la distance) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire S4-S8)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-15 03:33 UTC | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S33, 16/08/2026, 3 nuits, direct only) | Premier run — pas d'historique de comparaison. Anomalie notable : PRG à 1335 $ (2,4x le tarif BUD et 4x ATH) alors que la distance est comparable à VIE/BUD — seulement 2 itinéraires directs trouvés sur cette route (Israir/Arkia à l'aller, Israir/Arkia/Smartwings au retour) contre 8-15 sur les autres destinations, ce qui suggère une capacité directe très limitée sur TLV-PRG plutôt qu'un pic ponctuel. À surveiller sur les prochains runs pour confirmer la tendance. | ✅ Disponible |

