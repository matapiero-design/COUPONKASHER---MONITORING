# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-16 (run initial — premières données réelles)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS) × 3 semaines (S1-S3), vols directs uniquement, aller-retour 3 nuits, départ dimanche
- **Statut connecteur Kiwi.com** : OK — connecteur disponible et fonctionnel sur cette session

## Prix vols directs — S1-S3 (run quotidien)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 23/08/2026 | Dimanche | 1066 | 2026-08-16 | ⚠️ ANOMALIE — voir note |
| Prague | PRG | S2 | 30/08/2026 | Dimanche | 521 | 2026-08-16 | OK |
| Prague | PRG | S3 | 06/09/2026 | Dimanche | 412 | 2026-08-16 | OK |
| Vienne | VIE | S1 | 23/08/2026 | Dimanche | 1262 | 2026-08-16 | ⚠️ ANOMALIE — voir note |
| Vienne | VIE | S2 | 30/08/2026 | Dimanche | 455 | 2026-08-16 | OK |
| Vienne | VIE | S3 | 06/09/2026 | Dimanche | 412 | 2026-08-16 | OK |
| Rome | FCO | S1 | 23/08/2026 | Dimanche | 465 | 2026-08-16 | OK |
| Rome | FCO | S2 | 30/08/2026 | Dimanche | 219 | 2026-08-16 | OK |
| Rome | FCO | S3 | 06/09/2026 | Dimanche | 174 | 2026-08-16 | OK |
| Paphos | PFO | S1 | 23/08/2026 | Dimanche | 439 | 2026-08-16 | OK |
| Paphos | PFO | S2 | 30/08/2026 | Dimanche | 176 | 2026-08-16 | OK |
| Paphos | PFO | S3 | 06/09/2026 | Dimanche | 182 | 2026-08-16 | OK |
| Athènes | ATH | S1 | 23/08/2026 | Dimanche | 336 | 2026-08-16 | OK |
| Athènes | ATH | S2 | 30/08/2026 | Dimanche | 177 | 2026-08-16 | OK |
| Athènes | ATH | S3 | 06/09/2026 | Dimanche | 171 | 2026-08-16 | OK |
| Budapest | BUD | S1 | 23/08/2026 | Dimanche | 420 | 2026-08-16 | OK |
| Budapest | BUD | S2 | 30/08/2026 | Dimanche | 229 | 2026-08-16 | OK |
| Budapest | BUD | S3 | 06/09/2026 | Dimanche | 187 | 2026-08-16 | OK |
| Tbilissi | TBS | S1 | 23/08/2026 | Dimanche | 792 | 2026-08-16 | ⚠️ à surveiller — voir note |
| Tbilissi | TBS | S2 | 30/08/2026 | Dimanche | 381 | 2026-08-16 | OK |
| Tbilissi | TBS | S3 | 06/09/2026 | Dimanche | 426 | 2026-08-16 | OK |

*Prix = moins cher vol direct (0 escale), aller-retour, 1 adulte, 3 nuits sur place, trouvé via connecteur Kiwi.com. Devise native de la réponse connecteur déjà en USD (pas de conversion appliquée).*

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(non couvert par ce run — portée limitée à S1-S3 sur demande explicite du prompt du jour)_ | | | | | | | |

## Anomalies de prix signalées (run du 2026-08-16)

- **Prague (PRG) S1 — 23/08** : 1066 $, soit >2x le prix S2 (521 $) et >2.5x le prix S3 (412 $). Un seul résultat direct trouvé sur ce départ (disponibilité très limitée à ~1 semaine du vol), ce qui explique probablement le prix — à confirmer si ce n'est pas un vol quasi complet plutôt qu'une vraie référence de marché.
- **Vienne (VIE) S1 — 23/08** : 1262 $, soit >2.7x le prix S2 (455 $) et le prix S3 (412 $). Même schéma que Prague — seulement 8 résultats directs disponibles sur ce créneau, cherté probablement liée à la proximité de la date de départ plutôt qu'à une hausse durable.
- **Tbilissi (TBS) S1 — 23/08** : 792 $, nettement au-dessus de S2 (381 $) et S3 (426 $). Moins extrême que Prague/Vienne mais à surveiller — Tbilissi reste structurellement plus cher que les autres destinations du lot (moins de concurrence low-cost sur TLV-TBS), donc l'écart S1 pourrait refléter une vraie tension de dernière minute plutôt qu'une anomalie de donnée.
- **Constat général** : pour les 7 destinations, S1 (départ dans ~1 semaine) est systématiquement plus cher que S2/S3 — cohérent avec un effet last-minute, mais l'écart est disproportionné sur PRG/VIE (>2x) comparé à FCO/PFO/ATH/BUD (+50-90%). À recroiser avec un prochain run pour voir si le schéma se confirme.

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-16 (run initial) | PRG, VIE, FCO, PFO, ATH, BUD, TBS × S1-S3 (21 recherches) | Aucun gap (vol direct dimanche disponible partout) — 3 anomalies de prix S1 signalées ci-dessus (PRG, VIE, TBS) | OK |
