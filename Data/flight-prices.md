# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-11-27 (run vol seul, 7 destinations historiques Groupe A — PRG, VIE, FCO, PFO, ATH, BUD, TBS)
- **Portée du dernier run avant celui-ci** : 10 destinations Groupe A (PRG, VIE, AMS, PFO×2, ATH, BUD, TBS, LON, MNE), package vol+hôtel, S1-S8 complet — run manuel du 2026-09-15 (trigger API sans connecteurs)
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour toutes destinations
- **Statut connecteur Booking.com** : non interrogé sur ce run (vol seul, voir Journal des runs 2026-11-27)

## Prix vols directs — run 2026-11-27 (TLV, aller dimanche 29/11 → retour mercredi 02/12, 3 nuits)

⚠️ **Fenêtre très courte (J-2)** : ce run a été déclenché un vendredi pour un départ le dimanche suivant.
Les tarifs ci-dessous sont des prix de **dernière minute** et ne sont pas comparables terme à terme
aux relevés S1-S8 du 2026-09-15 (réservés 5 à 8 semaines à l'avance) — voir précédent similaire au
run du 2026-08-20 dans le Journal des runs, où le même écart s'était résorbé une fois la réservation
faite avec plus d'avance.

| Destination | Aéroport | Prix vol A/R ($) | Meilleure option | Statut |
|---|---|---|---|---|
| Prague | PRG | 340 | Smartwings (aller) / TUS Airways (retour) | ✅ direct A/R |
| Vienne | VIE | 369 | Austrian Airlines A/R | ⚠️ voir note écart ci-dessous |
| Rome | FCO | 157 | Wizz Air Malta A/R | ✅ direct A/R (vol seul — aucun hôtel casher confirmé actuellement, voir `pipeline/destinations.json` → `hors_booking`) |
| Paphos (WellClub / Brown Hills) | PFO | — | El Al LY5137 ou Israir 6H593 à l'aller (direct, 13h15/13h45) | ⛔ **gap retour** — aucun direct PFO→TLV le 02/12 (confirmé par requête dédiée PFO→TLV ; meilleure option avec escale(s) à 339$) |
| Chalkida | ATH | 183 | Israir (aller) / Wizz Air Malta (retour) | ✅ direct A/R |
| Budapest | BUD | 409 | Wizz Air A/R | ⚠️ voir note écart ci-dessous |
| Tbilissi | TBS | 211 | Israir (aller) / El Al (retour) | ✅ direct A/R |

**Écarts notables vs run 2026-09-15 (S5/S6/S8, hors effet dernière minute à confirmer)** :
- **Budapest** : 409$ vs 142-250$ sur S5/S6/S8 (+64 % à +188 %) — écart le plus marqué du run, à
  surveiller sur le prochain run avec plus de délai avant de conclure à une vraie hausse structurelle.
- **Vienne** : 369$ vs 301-316$ sur S5/S6/S8 (+17 % à +23 %) — dépasse le seuil d'alerte de 15 %,
  mais cohérent avec l'effet dernière minute documenté ci-dessus.
- Prague, Chalkida, Tbilissi : dans la fourchette S1-S8, pas d'anomalie.
- Rome (FCO) : pas de référence récente comparable dans ce fichier (dernier passage par FCO le
  2026-08-25) ; prix vol bas (157$) mais rappel — aucune des 5 options hôtel Rome n'a de certificat
  cacherout confirmé à ce jour (`pipeline/destinations.json`), donc pas de prix vendable.

## Prix vols directs — Groupe A (S1-S8, run 2026-09-15)

### S1 — Départ 20/09/2026 (dimanche) → retour 23/09

⚠️ **BLOQUÉE ROCH HACHANA** — retour 23/09 = RH j2, aéroport Ben Gurion fermé. Tarifs relevés pour information uniquement, non vendables.

| Destination | Aéroport | Prix vol A/R ($) | Statut |
|---|---|---|---|
| Paphos (WellClub) | PFO | 186 | ⛔ retour RH j2 |
| Budapest | BUD | 418 | ⛔ retour RH j2 |
| Vienne | VIE | 486 | ⛔ retour RH j2 |
| Amsterdam | AMS | 805 | ⛔ retour RH j2 |
| Prague | PRG | 579 | ⛔ retour RH j2 |
| Tbilissi | TBS | — | gap vol (aucun direct S1-S4) |
| Chalkida | ATH | — | pas de direct dimanche S1 |
| Londres | LON | — | non interrogé (semaine bloquée) |
| Budva/Montenegro | TIV | — | non interrogé (semaine bloquée) |

### S2 — Départ 27/09/2026 (dimanche) → retour 30/09

⚠️ **EREV YOM KIPPOUR** — retour 30/09 = Erev YK, vols opérationnels mais très serré pour clientèle pratiquante. À valider par Jacques.

| Destination | Aéroport | Prix vol A/R ($) | Statut |
|---|---|---|---|
| Vienne | VIE | 567 | ⚠️ Erev YK |
| Amsterdam | AMS | 805 | ⚠️ Erev YK |
| Londres | LON | 1 144 | ⚠️ Erev YK |
| Prague | PRG | — | aucun résultat S2 dans Kiwi |
| Budapest | BUD | — | aucun résultat S2 |
| Paphos | PFO | — | aucun résultat S2 |
| Chalkida | ATH | — | aucun résultat S2 |

### S3 — Départ 04/10/2026 (dimanche) → retour 07/10

✅ **VALIDE** — retour 07/10 = Hol HaMoed Sukkot (Israël, 2e jour), aéroport Ben Gurion OUVERT.

| Destination | Aéroport | Prix vol A/R ($) | Statut |
|---|---|---|---|
| Chalkida | ATH | 142 | ✅ repli lundi 05/10 (pas de direct dimanche 04/10) |
| Paphos (WellClub) | PFO | 169 | ✅ dimanche |
| Budapest | BUD | 383 | ✅ dimanche |
| Budva/Montenegro | TIV | 346 | ✅ Israir TLV-TIV dimanche |
| Prague | PRG | 525 | ✅ dimanche |
| Londres | LON | 1 048 | ✅ dimanche |
| Amsterdam | AMS | — | gap vol — pas de direct TLV-AMS dimanche 04/10 ni lundi 05/10 |
| Vienne | VIE | — | aucun résultat S3 |
| Tbilissi | TBS | — | gap vol (aucun direct S1-S4) |

### S4 — Départ 11/10/2026 (dimanche) → retour 14/10

✅ **VALIDE** — retour 14/10 = lendemain Shimini Atzeret (13/10 en Israël), aéroport ouvert.

| Destination | Aéroport | Prix vol A/R ($) | Statut |
|---|---|---|---|
| Budapest | BUD | 149 | ✅ meilleur prix Budapest sur la fenêtre |
| Chalkida | ATH | 146 | ✅ |
| Paphos (WellClub) | PFO | 170 | ✅ |
| Vienne | VIE | 301 | ✅ |
| Prague | PRG | 317 | ✅ |
| Londres | LON | 1 297 | ✅ (plus cher que S3/S5, dynamique post-fêtes) |
| Amsterdam | AMS | — | gap vol — pas de direct dimanche S4 |
| Tbilissi | TBS | — | gap vol (aucun direct S1-S4) |
| Budva/Montenegro | TIV | — | pas de direct TLV-TIV S4 |

### S5 — Départ 18/10/2026 (dimanche) → retour 21/10

✅ Première semaine post-haggim pleinement opérationnelle — référence hôtels.

| Destination | Aéroport | Prix vol A/R ($) | Statut |
|---|---|---|---|
| Chalkida | ATH | 146 | ✅ |
| Paphos (WellClub) | PFO | 151 | ✅ meilleur vol Paphos |
| Vienne | VIE | 301 | ✅ |
| Prague | PRG | 321 | ✅ |
| Budapest | BUD | 250 | ✅ |
| Tbilissi | TBS | 305 | ✅ premier direct disponible sur la fenêtre |
| Amsterdam | AMS | 571 | ✅ Blue Bird BZ612 |
| Budva/Montenegro | TIV | 491 | ✅ |
| Londres | LON | 853 | ✅ |
| Paphos (Brown Hills) | PFO | 151 | ✅ vol disponible — gap hôtel Brown Hills S5 |

### S6 — Départ 25/10/2026 (dimanche) → retour 28/10

| Destination | Aéroport | Prix vol A/R ($) | Statut |
|---|---|---|---|
| Tbilissi | TBS | 210 | ✅ meilleur vol Tbilissi |
| Budapest | BUD | 220 | ✅ |
| Chalkida | ATH | 175 | ✅ |
| Vienne | VIE | 311 | ✅ |
| Prague | PRG | 339 | ✅ |
| Londres | LON | 613 | ✅ |
| Paphos (Brown Hills) | PFO | — | gap vol dimanche 25/10 — hôtel Brown Hills disponible S6 à 761,48$ total |
| Amsterdam | AMS | — | gap vol — pas de direct dimanche S6 |
| Budva/Montenegro | TIV | — | pas de direct TLV-TIV S6 |

### S7 — Départ 01/11/2026 (dimanche) → retour 04/11

| Destination | Aéroport | Prix vol A/R ($) | Statut |
|---|---|---|---|
| Tbilissi | TBS | 212 | ✅ |
| Amsterdam | AMS | — | gap vol |
| Autres | — | — | non disponibles sur cette semaine |

### S8 — Départ 08/11/2026 (dimanche) → retour 11/11

| Destination | Aéroport | Prix vol A/R ($) | Statut |
|---|---|---|---|
| Budapest | BUD | 142 | ✅ meilleur prix Budapest fenêtre |
| Chalkida | ATH | 140 | ✅ meilleur prix Chalkida fenêtre |
| Tbilissi | TBS | 210 | ✅ |
| Vienne | VIE | 316 | ✅ |
| Prague | PRG | 309 | ✅ meilleur vol Prague fenêtre |
| Amsterdam | AMS | 690 | ✅ El Al LY337 |
| Londres | LON | 401 | ✅ meilleur vol Londres fenêtre — 1ère fois sous 500$ |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-11-27 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) — vol seul, pas de package hôtel sur ce run. Fenêtre dimanche 29/11 → mercredi 02/12 (3 nuits), recherchée à J-2 (run déclenché un vendredi). | **Gap** : Paphos (PFO) — aucun vol direct retour PFO→TLV le 02/12 (confirmé par requête dédiée sur le segment seul) ; aller direct dispo (El Al LY5137 / Israir 6H593). **Écarts > 15 % vs run 2026-09-15** : Budapest (409$ vs 142-250$ sur S5/S6/S8, +64% à +188%), Vienne (369$ vs 301-316$, +17% à +23%) — à confirmer sur un prochain run avec plus de délai de réservation, l'effet dernière minute (J-2) étant la cause la plus probable plutôt qu'une hausse structurelle (cf. précédent du 2026-08-20 ci-dessous, résorbé le 2026-08-25). Prague, Chalkida, Tbilissi dans la norme S1-S8. Rome (FCO) à 157$ sans point de comparaison récent dans ce fichier — rappel : aucun hôtel Rome n'a de cacherout confirmée actuellement, prix non vendable en l'état. | OK |
| 2026-09-15 03:32 | PRG, VIE, AMS, PFO (WellClub + Brown Hills), ATH, BUD, TBS, LON, MNE (10 dest. Groupe A — Venise bloquée cacherout contestée). S1-S8 complet (run manuel, 3 semaines sans run) | **Haggim 5787** : S1 (retour 23/09 = RH j2) et S3/S4 partiellement bloquées — CORRECTION calendrier Israël : S3 (retour 07/10 = Hol HaMoed) et S4 (retour 14/10 = post-Shimini Atzeret) VALIDES pour clientèle israélienne. S2 (retour 30/09 = Erev YK) : à valider par Jacques. **Gaps vol** : TBS aucun direct S1-S4 (premier direct S5 18/10) ; AMS pas de direct dimanche S3, S4, S6, S7 ; MNE uniquement S3 + S5. **Gap hôtel** : Brown Hills Paphos pas de dispo S5, disponible S6 (761,48$ total). **Écarts > 15 %** : Prague (meilleur 2690₪ vs publié 3260₪, -17%), Vienne (meilleur 1930₪ vs publié 2520₪, -23%), Amsterdam (meilleur 2610₪ vs publié 1900₪, +37%) — les 3 nécessitent arbitrage Jacques avant publication. **Trigger** : trig_01AC9Z8TrgTpLToieNmSJ6G4 sans connecteurs (blocage API connu) — run manuel via session interactive avec Kiwi.com + Booking.com. Action requise : recréer la routine depuis claude.ai/routines avec les 2 connecteurs. | OK (manuel) |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
