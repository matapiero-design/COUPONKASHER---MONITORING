# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-19 (run automatisé)
- **Portée du dernier run** : Groupe restreint (PRG, VIE, FCO, PFO, ATH, BUD, TBS) — vols directs (0 escale), aller-retour 3 nuits, départ dimanche par défaut — S1 à S3
- **Statut connecteur Kiwi.com** : OK (connecteur disponible et utilisé pour ce run)

## Prix vols directs — PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Date retour | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 23/08/2026 | 26/08/2026 | Dimanche | — | 2026-08-19 | ⚠️ Aucun vol direct ce dimanche (voir anomalies) |
| Prague | PRG | S2 | 30/08/2026 | 02/09/2026 | Dimanche | 465 | 2026-08-19 | OK |
| Prague | PRG | S3 | 06/09/2026 | 09/09/2026 | Dimanche | 412 | 2026-08-19 | OK |
| Vienne | VIE | S1 | 23/08/2026 | 26/08/2026 | Dimanche | 1417 | 2026-08-19 | ⚠️ Prix anormalement élevé (voir anomalies) |
| Vienne | VIE | S2 | 30/08/2026 | 02/09/2026 | Dimanche | 455 | 2026-08-19 | OK |
| Vienne | VIE | S3 | 06/09/2026 | 09/09/2026 | Dimanche | 412 | 2026-08-19 | OK |
| Rome | FCO | S1 | 23/08/2026 | 26/08/2026 | Dimanche | 603 | 2026-08-19 | OK |
| Rome | FCO | S2 | 30/08/2026 | 02/09/2026 | Dimanche | 322 | 2026-08-19 | OK |
| Rome | FCO | S3 | 06/09/2026 | 09/09/2026 | Dimanche | 170 | 2026-08-19 | OK |
| Paphos | PFO | S1 | 23/08/2026 | 26/08/2026 | Dimanche | 472 | 2026-08-19 | OK |
| Paphos | PFO | S2 | 30/08/2026 | 02/09/2026 | Dimanche | 175 | 2026-08-19 | OK |
| Paphos | PFO | S3 | 06/09/2026 | 09/09/2026 | Dimanche | 171 | 2026-08-19 | OK |
| Athènes | ATH | S1 | 23/08/2026 | 26/08/2026 | Dimanche | 363 | 2026-08-19 | OK |
| Athènes | ATH | S2 | 30/08/2026 | 02/09/2026 | Dimanche | 202 | 2026-08-19 | OK |
| Athènes | ATH | S3 | 06/09/2026 | 09/09/2026 | Dimanche | 169 | 2026-08-19 | OK |
| Budapest | BUD | S1 | 23/08/2026 | 26/08/2026 | Dimanche | 471 | 2026-08-19 | OK |
| Budapest | BUD | S2 | 30/08/2026 | 02/09/2026 | Dimanche | 211 | 2026-08-19 | OK |
| Budapest | BUD | S3 | 06/09/2026 | 09/09/2026 | Dimanche | 218 | 2026-08-19 | OK |
| Tbilissi | TBS | S1 | 23/08/2026 | 26/08/2026 | Dimanche | 852 | 2026-08-19 | OK |
| Tbilissi | TBS | S2 | 30/08/2026 | 02/09/2026 | Dimanche | 548 | 2026-08-19 | OK |
| Tbilissi | TBS | S3 | 06/09/2026 | 09/09/2026 | Dimanche | 368 | 2026-08-19 | OK |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Anomalies de prix — run du 2026-08-19

- **PRG (Prague), S1 (dimanche 23/08/2026)** : aucun vol direct trouvé pour un départ dimanche cette semaine-là (0 résultat sur `TLV → PRG`, 0 escale, aller-retour). Vérification en élargissant la recherche (±3 jours, un-way) : des vols directs TLV-PRG existent bien cette semaine (Arkia IZ281/283, El Al LY2523, Smartwings QS1287, Israir 6H761/763), mais aucun n'est programmé le dimanche 23/08 précisément — gap ponctuel de programmation, pas une panne du connecteur. Dès S2 (30/08), un vol direct dominical redevient disponible à 465 $.
- **VIE (Vienne), S1 (dimanche 23/08/2026) : 1417 $** — plus de 3× le prix des semaines suivantes (455 $ en S2, 412 $ en S3). Cause probable : l'option la moins chère habituelle (Blue Bird Airways BZ316, 14h00) n'apparaît pas dans les résultats du 23/08, laissant Austrian Airlines (OS84/OS80) comme seules options directes ce jour-là, nettement plus chères. À surveiller lors du prochain run — si le vol Blue Bird réapparaît pour cette date, il s'agissait d'un problème d'inventaire temporaire plutôt que d'une hausse structurelle.
- Aucune autre anomalie notable — les prix FCO, PFO, ATH, BUD, TBS suivent une décroissance cohérente à mesure que la date de recherche s'éloigne (effet last-minute habituel), sans écart suspect.

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-19 (run manuel/scheduled) | PRG, VIE, FCO, PFO, ATH, BUD, TBS — S1 à S3 (7 destinations × 3 semaines) | PRG S1 : aucun vol direct dominical cette semaine (gap de programmation, confirmé). VIE S1 : prix anormal (1417 $ vs ~410-455 $ les semaines suivantes) — vol Blue Bird BZ316 absent des résultats ce jour-là. | OK |
