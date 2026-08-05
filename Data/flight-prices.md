# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-05 (run automatisé)
- **Portée du dernier run** : PRG, VIE, FCO, PFO, ATH, BUD, TBS — TLV, vols directs (0 escale), aller-retour 3 nuits, dimanche par défaut, S1-S3. TBS (Tbilisi) est une destination hors liste Groupe A/B du skill `dashboard-suivi-prix-sejours-casher` — ajoutée sur demande explicite du prompt de routine, à faire valider par Jacques. S4-S8 non traité (run hors dimanche).
- **Statut connecteur Kiwi.com** : disponible et opérationnel — 21/21 recherches directes réussies (1 gap ponctuel : PRG dimanche S2, comblé par le lundi de repli)

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 2026-08-09 | Dimanche | 761 | 2026-08-05 | OK |
| Prague | PRG | S2 | 2026-08-17 | **Lundi** | 934 | 2026-08-05 | Alt. lundi — pas de vol direct dimanche 16/08 (gap) |
| Prague | PRG | S3 | 2026-08-23 | Dimanche | 971 | 2026-08-05 | OK — hausse continue S1→S3 (+28%) |
| Vienne | VIE | S1 | 2026-08-09 | Dimanche | 725 | 2026-08-05 | OK |
| Vienne | VIE | S2 | 2026-08-16 | Dimanche | 721 | 2026-08-05 | OK |
| Vienne | VIE | S3 | 2026-08-23 | Dimanche | 1197 | 2026-08-05 | ⚠️ Anomalie — bond de +66% vs S2 |
| Rome | FCO | S1 | 2026-08-09 | Dimanche | 381 | 2026-08-05 | OK |
| Rome | FCO | S2 | 2026-08-16 | Dimanche | 341 | 2026-08-05 | OK |
| Rome | FCO | S3 | 2026-08-23 | Dimanche | 399 | 2026-08-05 | OK |
| Paphos | PFO | S1 | 2026-08-09 | Dimanche | 245 | 2026-08-05 | OK |
| Paphos | PFO | S2 | 2026-08-16 | Dimanche | 385 | 2026-08-05 | OK |
| Paphos | PFO | S3 | 2026-08-23 | Dimanche | 520 | 2026-08-05 | ⚠️ Anomalie — dépasse le seuil historique <400$, +112% vs S1 |
| Athènes/Chalkida | ATH | S1 | 2026-08-09 | Dimanche | 342 | 2026-08-05 | OK |
| Athènes/Chalkida | ATH | S2 | 2026-08-16 | Dimanche | 442 | 2026-08-05 | ⚠️ Dépasse le seuil historique <400$ |
| Athènes/Chalkida | ATH | S3 | 2026-08-23 | Dimanche | 377 | 2026-08-05 | OK — retour sous le seuil |
| Budapest | BUD | S1 | 2026-08-09 | Dimanche | 342 | 2026-08-05 | OK |
| Budapest | BUD | S2 | 2026-08-16 | Dimanche | 371 | 2026-08-05 | OK |
| Budapest | BUD | S3 | 2026-08-23 | Dimanche | 436 | 2026-08-05 | OK — hausse continue S1→S3 (+27%) |
| Tbilissi | TBS | S1 | 2026-08-09 | Dimanche | 671 | 2026-08-05 | OK (hors historique — nouvelle destination) |
| Tbilissi | TBS | S2 | 2026-08-16 | Dimanche | 730 | 2026-08-05 | OK (hors historique — nouvelle destination) |
| Tbilissi | TBS | S3 | 2026-08-23 | Dimanche | 537 | 2026-08-05 | OK (hors historique — nouvelle destination) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(non traité ce run — S4-S8 réservé au run dominical hebdomadaire ; dernier run un mercredi)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-05 | PRG, VIE, FCO, PFO, ATH, BUD, TBS × S1-S3 (21 recherches) | Gap : PRG dimanche S2 (comblé lundi 17/08, +23% vs S1). Anomalies prix : VIE S3 +66% vs S2 ; PFO S3 dépasse 400$ (520$, +112% vs S1) ; ATH S2 dépasse 400$ (442$). Tendances haussières S1→S3 sur PRG et BUD. TBS ajouté hors liste Groupe A/B du skill — à valider avec Jacques. | Disponible, 21/21 recherches réussies |
