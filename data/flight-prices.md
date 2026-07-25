# Prix vols TLV

Fichier mis a jour automatiquement par la routine de suivi quotidien des prix de vols.

## Parametres de recherche (par defaut)

- Origine : TLV (Tel Aviv)
- Vols directs uniquement (0 escale), aller-retour, 3 nuits sur place
- Jour de depart : dimanche (par defaut)
- Source : connecteur Kiwi.com
- Devise : USD (prix le plus bas trouve, tous transporteurs)

Note : le fichier precedent (`Data/flight-prices.md# Prix vols TLV...`) avait ete cree avec un nom de fichier corrompu (le contenu semble avoir ete colle dans le champ "nom de fichier" lors de la creation via l'interface GitHub) et ne contenait aucune donnee de prix. Il a ete supprime et remplace par ce fichier a l'emplacement correct `data/flight-prices.md`, conformement a la consigne de la routine.

## Historique des prix (USD, vol direct le moins cher, aller-retour 3 nuits)

| Date de verification | Depart demande | Retour | PRG | VIE | FCO | PFO | ATH | BUD | TBS |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-25 | dim 2026-08-02 | mer 2026-08-05 | 615 | 603 | 491 | 265 | 299 | 545 | 535 |

## Detail du run du 2026-07-25

| Destination | Prix (USD) | Vol aller | Vol retour |
|---|---|---|---|
| PRG (Prague) | 615 | QS1287 TLV→PRG 02/08 05:35→08:45 | U8461 PRG→TLV 05/08 18:55→23:40 |
| VIE (Vienne) | 603 | BZ316 TLV→VIE 02/08 14:00→16:45 | BZ317 VIE→TLV 05/08 18:45→23:10 |
| FCO (Rome) | 491 | 6H381 TLV→FCO 02/08 16:40→19:25 | W46041 FCO→TLV 05/08 05:30→10:00 |
| PFO (Paphos) | 265 | U8158 TLV→PFO 02/08 19:45→20:50 | LY5140 PFO→TLV 05/08 09:40→10:50 |
| ATH (Athenes) | 299 | IZ1215 TLV→ATH 02/08 22:30→00:40 | 6H952 ATH→TLV 06/08 02:15→04:15 |
| BUD (Budapest) | 545 | BZ442 TLV→BUD 02/08 15:30→18:05 | W62505 BUD→TLV 05/08 05:00→09:15 |
| TBS (Tbilissi) | 535 | 6H891 TLV→TBS 02/08 19:40→23:20 | 6H782 TBS→TLV 05/08 03:15→04:55 |

## Anomalies signalees

Aucune anomalie detectee lors de ce run — il s'agit du premier releve exploitable pour ce fichier (l'historique precedent est illisible/absent, voir note ci-dessus), il n'y a donc pas encore de base de comparaison pour juger d'un ecart de prix. Points a surveiller a partir du prochain run :

- **PRG** ressort comme la destination la plus chere du lot ($615) malgre une distance/duree de vol comparable a VIE et BUD — a confirmer si ce n'est pas ponctuel (charge dimanche 02/08).
- **PFO** ($265) et **ATH** ($299) sont coherents avec des tarifs bas-cout habituels sur ces routes courtes.
- Aucun vol direct manquant : les 7 destinations avaient une option 0-escale disponible pour le dimanche 02/08/2026.
