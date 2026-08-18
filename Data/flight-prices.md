# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-18 (run automatisé)
- **Portée du dernier run** : PRG, VIE, FCO, PFO, ATH, BUD, TBS — vols directs (0 escale), A/R 3 nuits, départ dimanche par défaut — S1 à S3 (Kiwi.com)
- **Statut connecteur Kiwi.com** : OK — connecteur disponible et interrogé avec succès pour ce run

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Date retour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 23/08/2026 | Dimanche | — | — | 2026-08-18 | ⚠️ Pas de vol direct dimanche — voir repli lundi ci-dessous |
| Prague (repli) | PRG | S1 | 24/08/2026 | Lundi | 27/08/2026 | 827 | 2026-08-18 | Alternative (jour différent) |
| Prague | PRG | S2 | 30/08/2026 | Dimanche | 02/09/2026 | 465 | 2026-08-18 | OK |
| Prague | PRG | S3 | 06/09/2026 | Dimanche | 09/09/2026 | 413 | 2026-08-18 | OK |
| Vienne | VIE | S1 | 23/08/2026 | Dimanche | 26/08/2026 | 1351 | 2026-08-18 | ⚠️ Anomalie de prix (voir note) |
| Vienne | VIE | S2 | 30/08/2026 | Dimanche | 02/09/2026 | 455 | 2026-08-18 | OK |
| Vienne | VIE | S3 | 06/09/2026 | Dimanche | 09/09/2026 | 412 | 2026-08-18 | OK |
| Rome | FCO | S1 | 23/08/2026 | Dimanche | 26/08/2026 | 684 | 2026-08-18 | OK |
| Rome | FCO | S2 | 30/08/2026 | Dimanche | 02/09/2026 | 304 | 2026-08-18 | OK |
| Rome | FCO | S3 | 06/09/2026 | Dimanche | 09/09/2026 | 174 | 2026-08-18 | OK |
| Paphos | PFO | S1 | 23/08/2026 | Dimanche | 26/08/2026 | 459 | 2026-08-18 | OK |
| Paphos | PFO | S2 | 30/08/2026 | Dimanche | 02/09/2026 | 176 | 2026-08-18 | OK |
| Paphos | PFO | S3 | 06/09/2026 | Dimanche | 09/09/2026 | 171 | 2026-08-18 | OK |
| Athènes | ATH | S1 | 23/08/2026 | Dimanche | 26/08/2026 | 399 | 2026-08-18 | OK |
| Athènes | ATH | S2 | 30/08/2026 | Dimanche | 02/09/2026 | 203 | 2026-08-18 | OK |
| Athènes | ATH | S3 | 06/09/2026 | Dimanche | 09/09/2026 | 168 | 2026-08-18 | OK |
| Budapest | BUD | S1 | 23/08/2026 | Dimanche | 26/08/2026 | 472 | 2026-08-18 | OK |
| Budapest | BUD | S2 | 30/08/2026 | Dimanche | 02/09/2026 | 218 | 2026-08-18 | OK |
| Budapest | BUD | S3 | 06/09/2026 | Dimanche | 09/09/2026 | 199 | 2026-08-18 | OK |
| Tbilissi | TBS | S1 | 23/08/2026 | Dimanche | 26/08/2026 | 879 | 2026-08-18 | ⚠️ Prix nettement au-dessus de S2/S3 (voir note) |
| Tbilissi | TBS | S2 | 30/08/2026 | Dimanche | 02/09/2026 | 450 | 2026-08-18 | OK |
| Tbilissi | TBS | S3 | 06/09/2026 | Dimanche | 09/09/2026 | 380 | 2026-08-18 | OK |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(non traité ce run — S4-S8 vérifié uniquement le dimanche ; prochain run dominical à programmer)_ | | | | | | | |

## Anomalies de prix signalées (run du 2026-08-18)

- **PRG — S1 (dimanche 23/08)** : aucun vol direct trouvé. Repli lundi 24/08 vérifié conformément à la règle du skill (jamais de repli samedi) : vol direct disponible à 827 $, nettement plus cher que S2 (465 $) et S3 (413 $) sur la même route. À surveiller — pourrait indiquer une faible disponibilité de sièges directs ce dimanche précis plutôt qu'une hausse structurelle.
- **VIE — S1 (dimanche 23/08)** : 1351 $, soit ~3x le prix de S2 (455 $) et S3 (412 $) sur la même route TLV-VIE. Écart largement hors norme même pour du court terme — à vérifier avant toute utilisation commerciale de ce prix (devis, promo). Un événement local à Vienne ce week-end (congrès, forte demande) est une explication possible mais non confirmée.
- **TBS — S1 (dimanche 23/08)** : 879 $, environ le double de S2 (450 $) et de S3 (380 $). Écart moins extrême que VIE mais toujours notable — probablement lié à la faible fréquence des vols directs TLV-TBS (offre limitée à court terme).
- **Tendance générale** : sur les 7 destinations, S1 est systématiquement plus cher que S2/S3 (comportement normal de prix court-terme), mais l'écart est disproportionné pour VIE et TBS comparé aux 5 autres destinations — à recouper avec un second run avant de considérer ces prix comme fiables pour un devis.

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-18 (run initial) | PRG, VIE, FCO, PFO, ATH, BUD, TBS — S1 à S3 (21 recherches) | Gap PRG S1 dimanche (repli lundi trouvé, 827 $) ; anomalies de prix VIE S1 (1351 $, ~3x S2/S3) et TBS S1 (879 $, ~2x S2/S3) — voir section Anomalies ci-dessus | OK — connecteur Kiwi.com disponible et fonctionnel pour l'ensemble du run |
