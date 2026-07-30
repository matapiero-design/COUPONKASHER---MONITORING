# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-07-30 03:36 UTC
- **Portée du dernier run** : Destinations PRG, VIE, FCO, PFO, ATH, BUD, TBS (au départ de TLV) — vols directs, aller-retour, 3 nuits, dimanche par défaut — S1-S3 uniquement (run non-dominical, S4-S8 non exécuté)
- **Statut connecteur Kiwi.com** : OK (une erreur transitoire 502 sur TLV→FCO S2, résolue au retry immédiat — aucune donnée manquante)

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 2026-08-02 | Dimanche | 564 | 2026-07-30 | OK |
| Vienne | VIE | S1 | 2026-08-02 | Dimanche | 1156 | 2026-07-30 | ⚠️ prix élevé (voir anomalies) |
| Rome | FCO | S1 | 2026-08-02 | Dimanche | 671 | 2026-07-30 | ⚠️ voir anomalies (écart vs S2/S3) |
| Paphos | PFO | S1 | 2026-08-02 | Dimanche | 335 | 2026-07-30 | OK |
| Athènes | ATH | S1 | 2026-08-02 | Dimanche | 297 | 2026-07-30 | OK |
| Budapest | BUD | S1 | 2026-08-02 | Dimanche | 537 | 2026-07-30 | ⚠️ voir anomalies (écart vs S2/S3) |
| Tbilissi | TBS | S1 | 2026-08-02 | Dimanche | 515 | 2026-07-30 | OK |
| Prague | PRG | S2 | 2026-08-09 | Dimanche | 1167 | 2026-07-30 | ⚠️ hausse forte vs S1 (voir anomalies) |
| Vienne | VIE | S2 | 2026-08-09 | Dimanche | 884 | 2026-07-30 | ⚠️ prix élevé (voir anomalies) |
| Rome | FCO | S2 | 2026-08-09 | Dimanche | 371 | 2026-07-30 | OK |
| Paphos | PFO | S2 | 2026-08-09 | Dimanche | 308 | 2026-07-30 | OK |
| Athènes | ATH | S2 | 2026-08-09 | Dimanche | 292 | 2026-07-30 | OK |
| Budapest | BUD | S2 | 2026-08-09 | Dimanche | 362 | 2026-07-30 | OK |
| Tbilissi | TBS | S2 | 2026-08-09 | Dimanche | 626 | 2026-07-30 | OK |
| Prague | PRG | S3 | 2026-08-16 | Dimanche | 968 | 2026-07-30 | ⚠️ reste élevé vs S1 (voir anomalies) |
| Vienne | VIE | S3 | 2026-08-16 | Dimanche | 826 | 2026-07-30 | ⚠️ prix élevé (voir anomalies) |
| Rome | FCO | S3 | 2026-08-16 | Dimanche | 372 | 2026-07-30 | OK |
| Paphos | PFO | S3 | 2026-08-16 | Dimanche | 383 | 2026-07-30 | OK |
| Athènes | ATH | S3 | 2026-08-16 | Dimanche | 452 | 2026-07-30 | OK |
| Budapest | BUD | S3 | 2026-08-16 | Dimanche | 391 | 2026-07-30 | OK |
| Tbilissi | TBS | S3 | 2026-08-16 | Dimanche | 593 | 2026-07-30 | OK |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — run non-dominical, S4-S8 vérifié uniquement le dimanche)_ | | | | | | | |

## Anomalies de prix détectées (run du 2026-07-30)

Ce fichier n'a pas encore d'historique multi-jours (premier run réel) : les anomalies ci-dessous sont donc des écarts internes au run (entre semaines S1/S2/S3), pas des écarts vs un historique confirmé. À recroiser avec les prochains runs quotidiens.

- **Prague (PRG)** : 564 $ (S1) → 1167 $ (S2, +107 %) → 968 $ (S3). Saut S1→S2 très marqué. Vol S1 le moins cher passe par TUS Airways/Arkia en retour ; en S2-S3 les mêmes compagnies sont disponibles mais à des tarifs bien plus élevés — possible tension de charge sur la période S2 (semaine du 9 août) à surveiller.
- **Vienne (VIE)** : 1156 $ (S1) → 884 $ (S2) → 826 $ (S3). Nettement plus cher que les autres capitales comparables (Prague, Budapest, Rome, toutes < 700 $ en S2-S3) sur les trois semaines — pas d'option Wizz Air/low-cost direct TLV-VIE disponible dans les résultats, seulement Austrian Airlines/Blue Bird/El Al/Arkia. Écart structurel à confirmer, pas un pic ponctuel.
- **Rome (FCO)** : 671 $ (S1) → 371 $ (S2) → 372 $ (S3). Écart de -45 % entre S1 et S2. La cause identifiée : l'option la moins chère en S2/S3 est un aller-retour Wizz Air Malta (W46044/W46041, ~19h40 aller / 05h30 retour) absent des résultats S1 sur ce créneau horaire — à confirmer que ce n'est pas un vol supprimé/complet pour le 2 août.
- **Budapest (BUD)** : 537 $ (S1) vs 362 $ (S2) et 391 $ (S3). Écart moins prononcé mais dans la même direction (S1 plus cher que S2-S3).
- **Athènes (ATH)** : plus cher en S3 (452 $) qu'en S1-S2 (~295 $) — écart à re-vérifier au prochain run, ATH/PFO restent globalement les moins chères du lot.

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-07-30 03:36 | PRG, VIE, FCO, PFO, ATH, BUD, TBS × S1-S3 (21 recherches, dimanche, 3 nuits, vols directs uniquement) | Aucun gap (vol direct trouvé partout). Anomalies de prix notées ci-dessus : PRG (saut S1→S2), VIE (prix élevé constant), FCO (écart S1 vs S2-S3), BUD (S1 plus cher) | OK — 1 erreur transitoire Cloudflare 502 sur TLV→FCO S2, résolue au retry immédiat |
