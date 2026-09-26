# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-26 (heure de la session, UTC non horodaté par l'outil)
- **Portée du dernier run** : vérification ponctuelle vol seul (sans hôtel), 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), départ dimanche 27/09/2026 → retour mercredi 30/09/2026 (3 nuits), 0 escale strict, 1 adulte, USD
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus (gaps PFO/TBS confirmés réels, voir ci-dessous)
- **Statut connecteur Booking.com** : non interrogé sur ce run (vol seul)

## Vérification ponctuelle — run 2026-09-26 (S2 : départ 27/09 → retour 30/09)

⚠️ **Fenêtre de réservation très courte** : ce run a été déclenché un samedi 26/09 pour un départ le
lendemain dimanche 27/09 — J-1. Les prix ci-dessous sont donc des tarifs de dernière minute et ne
sont **pas directement comparables** aux relevés S1-S8 du run du 15/09 (faits plusieurs semaines à
l'avance). Voir le run du 2026-08-20 vs 2026-08-25 dans le Journal : un délai d'achat plus court
gonfle mécaniquement les prix sur toutes les destinations, indépendamment de toute anomalie réelle.

⚠️ **Retour 30/09 = Erev Yom Kippour** — déjà signalé sur le run du 15/09 (S2), à valider par Jacques
avant toute vente sur cette semaine précise.

| Destination | Aéroport | Meilleur prix A/R ($) | Options directes | Statut |
|---|---|---|---|---|
| Prague | PRG | 980 | 3 | ⚠️ prix élevé — voir anomalie ci-dessous |
| Vienne | VIE | 699 | 15 | ⚠️ +23 % vs S2 du run 15/09 (567$) |
| Rome | FCO | 629 | 15 | ℹ️ première donnée FCO dans ce fichier, pas de comparatif |
| Paphos (WellClub/Brown Hills) | PFO | — | 0 | ⛔ aucun direct dimanche 27/09 — confirmé par requête élargie (voir anomalie) |
| Chalkida | ATH | 433 | 15 | ⚠️ très supérieur à la fourchette S3-S8 (140-175$) |
| Budapest | BUD | 506 | 15 | ⚠️ supérieur à la fourchette S3-S8 (149-383$) |
| Tbilissi | TBS | — | 0 | ⛔ aucun direct dimanche 27/09 — confirmé par requête élargie (voir anomalie) |

### Anomalies signalées

1. **PRG à 980$** — seulement 3 options directes trouvées (vs 15 pour VIE/FCO/ATH/BUD la même
   semaine), cohérent avec une offre TLV-PRG structurellement plus restreinte en delai court
   (cf. précédent du 2026-08-20 où PRG n'avait qu'une seule option à 1723$). Probablement un effet
   cumulé délai-court + semaine de fêtes, pas une erreur de données — à confirmer sur un prochain
   run avec plus d'avance.
2. **VIE +23 % vs le même S2 relevé le 15/09** (699$ vs 567$) — écart notable sur la même semaine
   calendaire, à surveiller (délai d'achat différent entre les deux runs, donc pas forcément un
   vrai mouvement de prix).
3. **ATH (Chalkida) et BUD nettement au-dessus de leur fourchette habituelle** — probablement la
   combinaison délai-court + semaine d'Erev Yom Kippour (forte demande sur les vols autour des
   fêtes), pas un défaut de connecteur : les deux routes ont renvoyé 15 options chacune (pas de
   signe de données incomplètes).
4. **PFO et TBS sans aucun direct dimanche 27/09** — vérifié par une recherche élargie (27/09-03/10,
   toujours 3 nuits, 0 escale) : le premier direct PFO disponible sur cette fenêtre est le
   03/10 (samedi), le premier direct TBS le 01/10 (jeudi). Aucun report possible sur lundi/mardi
   pour rester sur un format 3 nuits sans sortir de la semaine Erev YK. Gap réel de calendrier de
   vols, pas un problème de requête — cohérent avec les gaps déjà documentés pour PFO (S2, run du
   15/09) et TBS (S1-S4, run du 15/09).

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
| 2026-09-26 (run vol seul, session cloud) | PRG, VIE, FCO, PFO, ATH, BUD, TBS (5/7 avec résultat, 2 gaps) — vol seul, pas de vérification hôtel. Départ dimanche 27/09 → retour mercredi 30/09 (3 nuits), 0 escale strict. **Fenêtre de réservation J-1** (run un samedi pour un départ le lendemain) : prix non comparables directement aux runs antérieurs faits plusieurs semaines à l'avance — voir précédent d'échelle 2026-08-20 vs 2026-08-25. | **Gaps vol confirmés (recherche élargie 27/09-03/10)** : PFO aucun direct dimanche, premier direct 03/10 (samedi) ; TBS aucun direct dimanche, premier direct 01/10 (jeudi). Cohérent avec les gaps déjà documentés pour ces deux routes sur S1-S4/S2 dans le run du 15/09. **Écarts vs relevés antérieurs (%informatifs, pas d'alerte formule 15% — vol seul, pas de package)** : PRG 980$ (seulement 3 options directes, très supérieur aux fenêtres S3-S8 à 309-580$) ; VIE 699$ (+23% vs le même S2 du 15/09 à 567$) ; ATH 433$ et BUD 506$ (nettement au-dessus de leur fourchette S3-S8 respective 140-175$ et 149-383$). Explication la plus probable pour les 4 : cumul délai-court (J-1) + semaine Erev Yom Kippour (forte demande fêtes), pas un défaut de données — les 4 routes ont chacune renvoyé un nombre d'options normal (3 à 15). **Rappel calendrier** : retour 30/09 = Erev Yom Kippour, déjà signalé le 15/09, à valider par Jacques avant toute vente sur cette semaine. FCO (Rome) 629$ : première donnée FCO consignée dans ce fichier, pas de comparatif possible. | OK |
| 2026-09-15 03:32 | PRG, VIE, AMS, PFO (WellClub + Brown Hills), ATH, BUD, TBS, LON, MNE (10 dest. Groupe A — Venise bloquée cacherout contestée). S1-S8 complet (run manuel, 3 semaines sans run) | **Haggim 5787** : S1 (retour 23/09 = RH j2) et S3/S4 partiellement bloquées — CORRECTION calendrier Israël : S3 (retour 07/10 = Hol HaMoed) et S4 (retour 14/10 = post-Shimini Atzeret) VALIDES pour clientèle israélienne. S2 (retour 30/09 = Erev YK) : à valider par Jacques. **Gaps vol** : TBS aucun direct S1-S4 (premier direct S5 18/10) ; AMS pas de direct dimanche S3, S4, S6, S7 ; MNE uniquement S3 + S5. **Gap hôtel** : Brown Hills Paphos pas de dispo S5, disponible S6 (761,48$ total). **Écarts > 15 %** : Prague (meilleur 2690₪ vs publié 3260₪, -17%), Vienne (meilleur 1930₪ vs publié 2520₪, -23%), Amsterdam (meilleur 2610₪ vs publié 1900₪, +37%) — les 3 nécessitent arbitrage Jacques avant publication. **Trigger** : trig_01AC9Z8TrgTpLToieNmSJ6G4 sans connecteurs (blocage API connu) — run manuel via session interactive avec Kiwi.com + Booking.com. Action requise : recréer la routine depuis claude.ai/routines avec les 2 connecteurs. | OK (manuel) |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
