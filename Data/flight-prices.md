# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-21 03:33 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche 23/08/2026 → retour mercredi 26/08/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour 6/7 destinations (aucune option directe pour PRG, voir anomalies)

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Athènes | ATH | S1 | 23/08/2026 | Dimanche | 372 | 2026-08-21 | OK |
| Paphos | PFO | S1 | 23/08/2026 | Dimanche | 486 | 2026-08-21 | OK |
| Budapest | BUD | S1 | 23/08/2026 | Dimanche | 565 | 2026-08-21 | OK |
| Rome (Fiumicino) | FCO | S1 | 23/08/2026 | Dimanche | 630 | 2026-08-21 | ⚠️ +12% vs veille (561→630) |
| Tbilissi | TBS | S1 | 23/08/2026 | Dimanche | 1191 | 2026-08-21 | ⚠️ Anomalie — +48% vs veille (806→1191) |
| Vienne | VIE | S1 | 23/08/2026 | Dimanche | 1280 | 2026-08-21 | Stable — élevé mais cohérent (pas de low-cost direct TLV-VIE) |
| Prague | PRG | S1 | 23/08/2026 | Dimanche | — | 2026-08-21 | ⚠️ Anomalie — 0 option directe trouvée (recherche relancée, confirmé), vs 1723$ la veille |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
| 2026-08-21 03:33 | VIE, FCO, PFO, ATH, BUD, TBS (6/7, résultats reçus) — PRG : 0 résultat (requête relancée deux fois, confirmé) | **PRG** : plus aucune option directe A/R disponible pour 23→26/08/2026 (contre 1 option unique à 1723$ la veille) — cohérent avec l'hypothèse "route à très faible fréquence directe" notée hier ; l'unique combinaison Smartwings/El Al a probablement disparu de l'inventaire pour ces dates précises. À vérifier si ça revient demain ou si TLV-PRG direct doit être considéré indisponible sur ce créneau. **TBS** : 1191$ vs 806$ la veille (+48%, +385$) — hausse forte à surveiller, à confirmer sur 2-3 jours avant de conclure à une anomalie de données vs une vraie tension tarifaire (peu d'options directes sur cette route, 3 résultats seulement). **FCO** : 630$ vs 561$ (+12%) — dans la fourchette normale de fluctuation, pas d'alerte. ATH (372$), PFO (486$), BUD (565$), VIE (1280$) : stables, variations <2%. | OK |
