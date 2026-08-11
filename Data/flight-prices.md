# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-11 03:34 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vols directs A/R 3 nuits, S1 uniquement (portée définie par le prompt reçu — pas de S2-S3 ni S4-S8 dans ce run)
- **Statut connecteur Kiwi.com** : disponible et utilisé (contrairement à la limitation documentée plus bas pour le trigger API — le connecteur était bien attaché à cette session)

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 17/08/2026 → 20/08/2026 | Lundi (gap dimanche) | 843 | 2026-08-11 | ⚠️ Aucun vol direct dimanche 16/08 disponible sur cette route — décalé lundi. Prix nettement au-dessus du groupe (~2x FCO/BUD) |
| Vienne | VIE | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 596 | 2026-08-11 | OK |
| Rome | FCO | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 366 | 2026-08-11 | OK |
| Paphos | PFO | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 397 | 2026-08-11 | OK |
| Athènes | ATH | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 479 | 2026-08-11 | OK |
| Budapest | BUD | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 483 | 2026-08-11 | OK |
| Tbilissi | TBS | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 734 | 2026-08-11 | ⚠️ Prix élevé pour la distance — capacité directe limitée (1 vol/jour Arkia/Israir), à surveiller |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — S4-S8 non couvert : run du 2026-08-11 n'est pas un dimanche, et hors de la portée du prompt reçu)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-11 03:34 UTC | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, A/R 3 nuits) | **Gap PRG** : aucun vol direct TLV→PRG le dimanche 16/08 (route opérée seulement lun/mer/jeu/ven/sam sur cette période) → décalé au lundi 17/08, retour 20/08, prix 843 $. **Anomalie prix PRG** : 843 $ soit ~1.4-2.3x le prix des autres destinations du groupe (366-596 $) — écart plausible (décalage de date + capacité directe réduite sur cette route) mais à re-vérifier au prochain run pour confirmer que ce n'est pas une erreur de tarification. **TBS** : 734 $, second prix le plus élevé du groupe, cohérent avec une capacité directe limitée (un seul vol quotidien Arkia/Israir), pas d'action requise mais à surveiller dans la durée. Premier run réel de ce fichier — pas d'historique antérieur pour comparaison de tendance. | OK — connecteur Kiwi.com disponible et utilisé pour les 7 destinations (recherches directes + recherches de secours flexibles pour PRG/TBS) |
