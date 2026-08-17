# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-17 (run automatisé)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS) — vols directs
  uniquement, aller-retour 3 nuits, départ dimanche par défaut, semaine S1 (23/08/2026)
- **Statut connecteur Kiwi.com** : ✅ opérationnel (connecteur MCP disponible et utilisé pour
  toutes les recherches de ce run)

## Prix vols directs — S1 (dimanche 23/08/2026 → mercredi 26/08/2026, 3 nuits)

| Destination | Aéroport | Date départ | Date retour | Prix A/R ($) | Compagnie (aller / retour) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | — | — | — | — | 2026-08-17 | ⚠️ Pas de vol direct disponible dimanche 23/08 ni lundi 24/08 (repli testé). Prochain direct trouvé : dimanche 30/08 (S2) à 483 $ — voir anomalies. |
| Vienne | VIE | 2026-08-23 | 2026-08-26 | 1206 | Austrian Airlines (OS80, 15h30→18h15) / Blue Bird Airways (BZ317, 18h45→23h10) | 2026-08-17 | ✅ Vérifié — prix anormalement élevé, voir anomalies |
| Rome | FCO | 2026-08-23 | 2026-08-26 | 580 | Wizz Air Malta (W46044, 19h40→22h30) / Wizz Air Malta (W46041, 05h30→10h00) | 2026-08-17 | ✅ Vérifié |
| Paphos | PFO | 2026-08-23 | 2026-08-26 | 439 | TUS Airways (U8162, 04h25→05h30) / TUS Airways (U8159, 11h05→12h10) | 2026-08-17 | ✅ Vérifié |
| Athènes (Chalkida) | ATH | 2026-08-23 | 2026-08-26 | 395 | Israir (6H563, 21h25→23h40) / Wizz Air Malta (W47512, 09h55→12h00) | 2026-08-17 | ✅ Vérifié |
| Budapest | BUD | 2026-08-23 | 2026-08-26 | 418 | Blue Bird Airways (BZ442, 15h30→18h05) / Wizz Air (W62505, 05h00→09h15) | 2026-08-17 | ✅ Vérifié |
| Tbilissi | TBS | 2026-08-23 | 2026-08-26 | 825 | Israir (6H895, 21h30→01h05+1) / Israir (6H782, 03h15→04h55) | 2026-08-17 | ✅ Vérifié — prix élevé, voir anomalies |

Note de portée : cette liste de 7 destinations est celle explicitement demandée pour ce run
(diffère du Groupe A standard du skill `dashboard-suivi-prix-sejours-casher`, qui inclut aussi
AMS/LHR/CDG et n'inclut pas TBS — non traitées aujourd'hui, non vérifiées dans ce run).

## Prix vols directs — S4-S8 (run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — S4-S8 non demandé dans le run d'aujourd'hui)_ | | | | | | | |

## Anomalies signalées — run du 2026-08-17

- **Prague (PRG) — gap** : aucun vol direct TLV↔PRG disponible ni dimanche 23/08 ni lundi 24/08
  (jour de repli testé conformément à la règle). Le connecteur Kiwi.com renvoie bien des
  itinéraires directs sur cette route, mais pas avant le week-end suivant : premier direct
  disponible = dimanche 30/08 → mercredi 02/09 (S2) à 483 $ (Smartwings QS1287 aller / TUS Airways
  U8461 retour). À reconfirmer lors du prochain run S1 ; si le trou persiste plusieurs jours de
  suite, le signaler à Jacques comme gap structurel plutôt que ponctuel.
- **Vienne (VIE) — prix élevé** : 1206 $ pour un aller-retour direct 3 nuits, très au-dessus des
  autres destinations couvertes aujourd'hui (Budapest 418 $, Athènes 395 $, Rome 580 $) alors que
  la distance/durée de vol est comparable. Vérifié deux fois (avec et sans filtre jour strict),
  résultat stable — ne semble pas être une erreur de requête. Sans historique antérieur pour
  confirmer une tendance, à surveiller sur les prochains runs avant de conclure à une anomalie
  ponctuelle vs. un niveau de prix structurellement plus élevé sur cette route en cette période
  (fin août = encore haute saison estivale).
- **Tbilissi (TBS) — prix élevé** : 825 $, nettement au-dessus des autres destinations. Route hors
  Groupe A standard (pas de baseline historique dans ce fichier) — à traiter comme référence de
  premier relevé plutôt que comme anomalie confirmée, mais à signaler à Jacques car le tarif est
  proche du double des autres destinations de la liste.
- Aucun vol Vendredi impliqué dans cette fenêtre (départ dimanche, retour mercredi) → contrainte
  d'atterrissage Shabbat non applicable à ce run.
- Aucun vol Samedi proposé ou retenu, conformément à la règle d'exclusion totale du Samedi.

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-17 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, 23/08→26/08) | Gap : PRG (pas de direct S1, alternative S2 à 483$). Anomalies prix : VIE (1206$), TBS (825$) — voir section Anomalies | ✅ opérationnel |
