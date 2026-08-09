# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-09 (UTC)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct
  (0 escale) aller-retour 3 nuits, au départ de TLV, départ dimanche par défaut — relevé pour le
  dimanche 16/08/2026 → mercredi 19/08/2026
- **Statut connecteur Kiwi.com** : ✅ Disponible et fonctionnel — la limitation documentée dans
  `ROUTINE_PROMPT.md` (connecteur non attaché via l'API `create_trigger`) ne s'est pas manifestée
  sur ce run ; les 7 recherches ont abouti normalement. À reconfirmer sur les prochains runs avant
  de considérer le problème définitivement résolu.

## Prix vols directs — dernier relevé (dimanche 16/08/2026 → mercredi 19/08/2026, 3 nuits)

| Destination | Aéroport | Date départ | Date retour | Prix A/R le moins cher ($) | Compagnie(s) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | 16/08/2026 | 19/08/2026 | 1244 | Arkia | 2026-08-09 | ⚠️ Anomalie — voir note |
| Vienne | VIE | 16/08/2026 | 19/08/2026 | 690 | Blue Bird Airways / Arkia | 2026-08-09 | OK |
| Rome (Fiumicino) | FCO | 16/08/2026 | 19/08/2026 | 366 | Wizz Air Malta | 2026-08-09 | OK |
| Paphos | PFO | 16/08/2026 | 19/08/2026 | 364 | El Al / TUS Airways | 2026-08-09 | OK |
| Athènes | ATH | 16/08/2026 | 19/08/2026 | 456 | Israir / Arkia | 2026-08-09 | OK |
| Budapest | BUD | 16/08/2026 | 19/08/2026 | 384 | Wizz Air | 2026-08-09 | OK |
| Tbilissi | TBS | 16/08/2026 | 19/08/2026 | 585 | Arkia / Israir | 2026-08-09 | OK |

### ⚠️ Anomalie détectée ce run

**Prague (PRG) : 1244 $** — plus de 3× le prix de Budapest (384 $) et près de 2× celui de Vienne
(690 $), pour une distance et une durée de vol comparables. Toutes les options directes
disponibles pour cette date (Arkia IZ281/IZ284, ou Smartwings QS1287 à l'aller combiné à
TUS Airways/Arkia au retour) sont chères — aucune alternative directe sous 1000 $ trouvée.
Hypothèses : capacité limitée sur cette route pour cette date précise, ou effet saisonnier
(mi-août). À reconfirmer sur les prochains runs quotidiens pour voir si le prix se normalise.

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-09 (run initial) | PRG, VIE, FCO, PFO, ATH, BUD, TBS — dimanche 16/08/2026, A/R 3 nuits | PRG anormalement cher (1244 $, voir note ci-dessus) | ✅ Disponible — voir note sur la limitation précédemment documentée |
