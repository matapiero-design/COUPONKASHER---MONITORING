# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine de suivi des prix de vols directs
TLV → destinations casher (voir `ROUTINE_PROMPT.md` / `README.md`).
Ne pas éditer manuellement — toute édition manuelle risque d'être écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-14 03:36 UTC
- **Portée du dernier run** : PRG, VIE, FCO, PFO, ATH, BUD, TBS — vol direct (0 escale), aller-retour, 3 nuits, départ dimanche par défaut (16/08/2026)
- **Statut connecteur Kiwi.com** : OK — connecteur actif, résultats reçus pour les 7 destinations (recherche complémentaire faite pour PRG, voir anomalies)

## Prix vols directs — historique (USD)

Une ligne par vérification. Les lignes ne sont jamais supprimées — l'historique s'accumule run après run pour permettre de suivre l'évolution des prix.

| Destination | Aéroport | Date départ | Jour | Date retour | Nuits | Prix A/R ($) | Compagnie aller | Compagnie retour | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|---|---|---|
| Prague | PRG | 16/08/2026 | Dimanche | — | 3 | — | — | — | 2026-08-14 | ⚠️ Aucun vol direct trouvé |
| Prague | PRG | 23/08/2026 | Dimanche | 26/08/2026 | 3 | 1075 | Smartwings QS1287 | Arkia IZ284 | 2026-08-14 | Info (hors dimanche par défaut) |
| Prague | PRG | 30/08/2026 | Dimanche | 02/09/2026 | 3 | 502 | Arkia IZ281 | TUS Airways U8461 | 2026-08-14 | Info (hors dimanche par défaut) |
| Vienne | VIE | 16/08/2026 | Dimanche | 19/08/2026 | 3 | 717 | Blue Bird Airways BZ316 | Arkia IZ424 | 2026-08-14 | OK |
| Rome | FCO | 16/08/2026 | Dimanche | 19/08/2026 | 3 | 463 | Israir 6H381 | Wizz Air Malta W46041 | 2026-08-14 | OK |
| Paphos | PFO | 16/08/2026 | Dimanche | 19/08/2026 | 3 | 321 | TUS Airways U8162 | TUS Airways U8153 | 2026-08-14 | OK |
| Athènes | ATH | 16/08/2026 | Dimanche | 19/08/2026 | 3 | 406 | Israir 6H563 | Wizz Air Malta W47512 | 2026-08-14 | OK |
| Budapest | BUD | 16/08/2026 | Dimanche | 19/08/2026 | 3 | 582 | Israir 6H707 | Wizz Air W62505 | 2026-08-14 | OK |
| Tbilissi | TBS | 16/08/2026 | Dimanche | 20/08/2026 | 3 | 1026 | Arkia IZ417 | Israir 6H900 | 2026-08-14 | OK |

## Anomalies détectées — 2026-08-14

- **PRG (Prague)** : aucun vol direct TLV→PRG trouvé pour le dimanche par défaut (16/08/2026, 3 nuits) — probablement plus de disponibilité sur le vol direct à si court délai (2 jours). Recherche élargie faite par sécurité :
  - 23/08 (dimanche) → **1075 $** (Smartwings tôt le matin + retour Arkia 3 jours après, un seul résultat direct)
  - 30/08 (dimanche) → **502 $** (dans la norme des autres destinations du groupe)
  - Écart de +114 % entre le 23/08 et le 30/08 sur la même route : ressemble à un vol quasi complet / faible dispo sur le 23/08 plutôt qu'à un vrai mouvement de marché. **À revérifier au prochain run** — pas de prix fiable à afficher pour le dimanche par défaut cette semaine.
- **TBS (Tbilissi)** : ressort nettement au-dessus du reste du groupe (1026 $ contre 321–717 $ pour les 6 autres destinations). Cohérent avec une offre directe limitée sur cette route (essentiellement Arkia/Israir, peu de résultats renvoyés — 4 itinéraires seulement contre 8-15 pour les autres). Pas un pic ponctuel détecté, mais un niveau structurellement élevé à garder en tête pour la comparaison des runs suivants.
- Aucune référence historique disponible avant ce run (premier run réel de ce fichier) : pas de comparaison jour-sur-jour possible pour VIE, FCO, PFO, ATH, BUD.

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-14 03:36 UTC | PRG, VIE, FCO, PFO, ATH, BUD, TBS | PRG : aucun direct le 16/08 (dimanche par défaut), voir détail ; TBS : prix nettement plus élevé que le reste du groupe (offre limitée) | OK |
