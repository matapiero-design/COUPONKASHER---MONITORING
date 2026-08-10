# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-10 (premier run automatisé effectué)
- **Portée du dernier run** : S1-S3 uniquement (aujourd'hui = lundi heure d'Israël, donc S4-S8 ignoré comme prévu). 7 destinations traitées : PRG, VIE, FCO, PFO, ATH, BUD, TBS — départ dimanche, aller-retour 3 nuits, vols directs uniquement (0 escale). ⚠️ Cette liste de 7 diffère de la liste "Groupe A" du skill `dashboard-suivi-prix-sejours-casher` (9 destinations : PRG, VIE, AMS, FCO, PFO, ATH, LHR, CDG, BUD) — AMS/LHR/CDG non couverts ici, TBS ajouté alors qu'absent du skill. À faire valider par Jacques : soit la portée de la routine a été volontairement resserrée sur ces 7 destinations, soit la liste doit être alignée sur le skill.
- **Statut connecteur Kiwi.com** : OK — disponible dès le départ de la session, 21 recherches (7 destinations × 3 semaines) toutes réussies, aucun gap technique.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 16/08/2026 | Dimanche | 1201 | 2026-08-10 | ⚠️ Anomalie prix — voir note |
| Prague | PRG | S2 | 23/08/2026 | Dimanche | 938 | 2026-08-10 | OK |
| Prague | PRG | S3 | 30/08/2026 | Dimanche | 490 | 2026-08-10 | OK |
| Vienne | VIE | S1 | 16/08/2026 | Dimanche | 595 | 2026-08-10 | OK |
| Vienne | VIE | S2 | 23/08/2026 | Dimanche | 1229 | 2026-08-10 | ⚠️ Anomalie prix — voir note |
| Vienne | VIE | S3 | 30/08/2026 | Dimanche | 443 | 2026-08-10 | OK |
| Rome | FCO | S1 | 16/08/2026 | Dimanche | 354 | 2026-08-10 | OK |
| Rome | FCO | S2 | 23/08/2026 | Dimanche | 387 | 2026-08-10 | OK |
| Rome | FCO | S3 | 30/08/2026 | Dimanche | 169 | 2026-08-10 | OK |
| Paphos | PFO | S1 | 16/08/2026 | Dimanche | 393 | 2026-08-10 | OK |
| Paphos | PFO | S2 | 23/08/2026 | Dimanche | 470 | 2026-08-10 | OK |
| Paphos | PFO | S3 | 30/08/2026 | Dimanche | 154 | 2026-08-10 | OK |
| Chalkida (aéroport Athènes) | ATH | S1 | 16/08/2026 | Dimanche | 477 | 2026-08-10 | OK |
| Chalkida (aéroport Athènes) | ATH | S2 | 23/08/2026 | Dimanche | 419 | 2026-08-10 | OK |
| Chalkida (aéroport Athènes) | ATH | S3 | 30/08/2026 | Dimanche | 169 | 2026-08-10 | OK |
| Budapest | BUD | S1 | 16/08/2026 | Dimanche | 520 | 2026-08-10 | OK |
| Budapest | BUD | S2 | 23/08/2026 | Dimanche | 480 | 2026-08-10 | OK |
| Budapest | BUD | S3 | 30/08/2026 | Dimanche | 218 | 2026-08-10 | OK |
| Tbilisi | TBS | S1 | 16/08/2026 | Dimanche | 671 | 2026-08-10 | OK |
| Tbilisi | TBS | S2 | 23/08/2026 | Dimanche | 649 | 2026-08-10 | OK |
| Tbilisi | TBS | S3 | 30/08/2026 | Dimanche | 387 | 2026-08-10 | OK |

**Notes sur les anomalies détectées (run du 2026-08-10) :**
- **Prague (PRG) S1 — 1201 $** : plus de 2× le prix S2 (938 $) et 2,5× le prix S3 (490 $), et nettement au-dessus de toutes les autres destinations la même semaine (354 $–671 $ ailleurs en S1). Le résultat le moins cher pour S1 utilise Arkia (IZ281/IZ284) — pas d'option Wizz Air/Smartwings moins chère visible ce jour précis, alors qu'elle existe en S2-S3. À surveiller le prochain run : si le prix reste élevé, probable tension de capacité sur ce vol précis plutôt qu'une variation normale.
- **Vienne (VIE) S2 — 1229 $** : plus du double du prix S1 (595 $) et de S3 (443 $) sur la même route. Les options les moins chères pour cette semaine (Blue Bird Airways, habituellement la moins chère sur VIE) n'apparaissent pas dans les résultats Kiwi pour ce couple de dates précis — seules des options Austrian Airlines plus chères ressortent. À revérifier au prochain run pour confirmer si c'est un pic réel ou un gap temporaire de disponibilité sur le connecteur.
- **Tendance générale S1→S3** : baisse marquée des prix sur toutes les destinations entre S1 (mi-août, pleine saison) et S3 (fin août/rentrée scolaire israélienne) — cohérent avec la fin de la haute saison estivale, pas une anomalie.
- Aucun gap "pas de vol direct" rencontré sur les 21 recherches — tous les départs dimanche demandés avaient une option directe.
- Aucun vol du vendredi concerné dans cette fenêtre (départs dimanche, retours dimanche/mercredi) — contrainte Shabbat non applicable à ce run.

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — run hebdomadaire dimanche pas encore effectué ; aujourd'hui 2026-08-10 est un lundi)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-08-10 (run automatisé, portée S1-S3) | PRG, VIE, FCO, PFO, ATH, BUD, TBS × S1-S3 (21 recherches) | 2 anomalies de prix (PRG S1 = 1201 $, VIE S2 = 1229 $, voir notes ci-dessus) ; écart de portée entre la liste de 7 destinations transmise par la routine et la liste "Groupe A" (9) du skill — à valider par Jacques ; aucun gap de vol direct | OK — connecteur disponible, 21/21 recherches réussies |
