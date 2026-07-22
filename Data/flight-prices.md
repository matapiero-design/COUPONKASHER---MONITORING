# Prix vols TLV

Fichier a completer automatiquement par la routine.

## Méthodologie

- **Origine** : Tel Aviv (TLV)
- **Destinations suivies** : PRG (Prague), VIE (Vienne), FCO (Rome), PFO (Paphos), ATH (Athènes), BUD (Budapest), TBS (Tbilissi)
- **Vols directs uniquement** (0 escale), aller-retour, 3 nuits sur place
- **Départ par défaut** : dimanche (le dimanche le plus proche à venir au moment de la vérification)
- **Devise** : USD
- **Source** : connecteur Kiwi.com
- **Passager** : 1 adulte

## Historique des prix (le moins cher, vol direct, 3 nuits)

### PRG — Prague

| Date de vérification | Aller (dép. TLV) | Retour (dép. PRG) | Prix (USD) | Compagnies |
|---|---|---|---|---|
| 2026-07-22 | 26/07/2026 05:35 | 29/07/2026 18:55 | 662 | QS1287 / U8461 |

### VIE — Vienne

| Date de vérification | Aller (dép. TLV) | Retour (dép. VIE) | Prix (USD) | Compagnies |
|---|---|---|---|---|
| 2026-07-22 | 26/07/2026 14:00 | 29/07/2026 18:45 | 634 | BZ316 / BZ317 |

### FCO — Rome

| Date de vérification | Aller (dép. TLV) | Retour (dép. FCO) | Prix (USD) | Compagnies |
|---|---|---|---|---|
| 2026-07-22 | 26/07/2026 16:40 | 29/07/2026 05:30 | 993 | 6H381 / W46041 |

### PFO — Paphos

| Date de vérification | Aller (dép. TLV) | Retour (dép. PFO) | Prix (USD) | Compagnies |
|---|---|---|---|---|
| 2026-07-22 | 26/07/2026 17:00 | 29/07/2026 23:50 | 299 | 6H591 / 6H594 |

### ATH — Athènes

| Date de vérification | Aller (dép. TLV) | Retour (dép. ATH) | Prix (USD) | Compagnies |
|---|---|---|---|---|
| 2026-07-22 | 26/07/2026 18:30 | 29/07/2026 09:55 | 210 | BZ706 / W47512 |

### BUD — Budapest

| Date de vérification | Aller (dép. TLV) | Retour (dép. BUD) | Prix (USD) | Compagnies |
|---|---|---|---|---|
| 2026-07-22 | 26/07/2026 16:35 | 29/07/2026 05:00 | 429 | IZ291 / W62505 |

### TBS — Tbilissi

| Date de vérification | Aller (dép. TLV) | Retour (dép. TBS) | Prix (USD) | Compagnies |
|---|---|---|---|---|
| 2026-07-22 | 26/07/2026 21:30 | 29/07/2026 03:35 | 574 | 6H895 / 6H894 |

## Anomalies et remarques du 2026-07-22

- **TBS (Tbilissi)** : une seule paire de vols directs existe dans les deux sens sur cette route (6H895 aller / 6H894 ou IZ1418 retour). L'aller est un vol de nuit (dép. 21h30, arrivée 01h05 le lendemain), donc le séjour "3 nuits" réel sur place est plus proche de 2 nuits pleines. Le filtre strict "3 nuits + 0 escale" du connecteur ne renvoie aucun résultat pour cette combinaison — le prix ci-dessus (574 USD) a été récupéré via une recherche sans filtre de nuits puis vérifié manuellement comme 100% direct dans les deux sens. À surveiller si la fréquence des vols directs TLV-TBS change.
- **FCO (Rome)** est la destination la plus chère du lot (993 USD), largement au-dessus des autres capitales européennes (VIE 634, PRG 662, BUD 429) — écart notable à re-vérifier lors de la prochaine passe pour confirmer que ce n'est pas une anomalie de tarification ponctuelle.
- **ATH (Athènes)** reste la destination la moins chère (210 USD), cohérent avec la proximité géographique.
- Aucun historique antérieur n'existait dans ce fichier avant le 2026-07-22 (fichier de suivi initialisé ce jour — un bug de nommage de fichier a également été corrigé : le fichier portait par erreur son propre titre Markdown comme nom de fichier).
