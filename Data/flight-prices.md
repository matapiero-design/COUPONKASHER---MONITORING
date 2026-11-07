# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-11-07 (run vols seuls, routine planifiée)
- **Portée du dernier run** : vols seuls, 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), 1 adulte, A/R direct, départ dim. 08/11 → retour mer. 11/11, USD. Pas d'hôtel, pas de package (`pricing.py` non lancé).
- **Statut connecteur Kiwi.com** : OK — résultats reçus pour 6/7 destinations (PFO : 0 résultat)
- **Statut connecteur Booking.com** : non utilisé dans ce run (vols seuls)

## Run 2026-11-07 — vols directs A/R, dimanche 08/11 → mercredi 11/11 (USD, 1 adulte)

Prix = meilleur A/R direct (0 escale aller et retour) retourné par Kiwi.com. Aucun samedi, aucun vendredi. Comparaison avec la ligne S8 (même départ 08/11) du run du 2026-09-15.

| Destination | Aéroport | Meilleur A/R ($) | Vols (aller / retour) | Options directes | S8 du 15/09 ($) | Écart | Statut |
|---|---|---|---|---|---|---|---|
| Athènes (Chalkida) | ATH | 153 | Wizz W48401 12:50 / W48402 09:50 | 15 | 140 | +9 % | ✅ |
| Rome | FCO | 156 | Wizz W46044 19:35 / W46041 05:45 | 15 | — | — | ✅ pas d'historique comparable |
| Tbilissi | TBS | 242 | El Al LY5117 06:25 / Israir 6H898 03:50 | 13 | 210 | +15 % | ✅ retour 03:50 (très tôt) |
| Budapest | BUD | 246 | Wizz W62328 19:30 / W62327 14:20 | 15 | 142 | **+73 %** | ⚠️ anomalie |
| Vienne | VIE | 311 | Blue Bird BZ316 10:30 / BZ317 14:45 | 12 | 316 | -2 % | ✅ |
| Prague | PRG | 317 | Smartwings QS1285 18:25 / TUS U8461 14:50 | 15 | 309 | +3 % | ✅ |
| Paphos | PFO | — | — | 0 | S4 170 / S5 151 | — | ⛔ gap vol |

**Anomalies**
- **Budapest : +73 %** (246 $ contre 142 $). Les 15 options sont à 246-283 $ : ce n'est pas un vol isolé, tout le créneau a monté. Probable effet de la demande de dernière minute à 1 jour du départ (voir les runs d'août). À confirmer sur les prochains runs avant toute décision de publication.
- **Paphos : aucun vol direct** sur dim. 08/11 → mer. 11/11, ni via le nom de ville « Paphos », ni en repli lundi 09/11 → jeudi 12/11. Même gap que S6 (25/10) et S7 (01/11) : trois semaines de suite sans direct dimanche. Le produit Paphos n'est pas vendable sur ces dates.
- **Tbilissi** : le retour le moins cher part mercredi à 03:50 (arrivée 04:30), donc en pratique la nuit de mardi à mercredi. À valider par Jacques avant de le vendre.
- Rome (FCO) est interrogée à la demande du prompt de la routine ; elle ne figure plus dans le Groupe A du dernier run manuel. À vérifier dans `pipeline/destinations.json`.
- Les prix ci-dessus sont des **prix de vol seuls**. Rien n'a été écrit dans `site/`.

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
| 2026-11-07 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7 dest., vols seuls, dim. 08/11 → mer. 11/11) | **Gap vol** : PFO aucun direct (aussi en repli lundi et par nom de ville), 3e semaine consécutive. **Anomalie** : BUD +73 % vs S8 du 15/09 (246 $ contre 142 $). TBS +15 %, ATH +9 %, PRG +3 %, VIE -2 % : dans la norme. FCO sans historique comparable. | OK (6/7) |
| 2026-09-15 03:32 | PRG, VIE, AMS, PFO (WellClub + Brown Hills), ATH, BUD, TBS, LON, MNE (10 dest. Groupe A — Venise bloquée cacherout contestée). S1-S8 complet (run manuel, 3 semaines sans run) | **Haggim 5787** : S1 (retour 23/09 = RH j2) et S3/S4 partiellement bloquées — CORRECTION calendrier Israël : S3 (retour 07/10 = Hol HaMoed) et S4 (retour 14/10 = post-Shimini Atzeret) VALIDES pour clientèle israélienne. S2 (retour 30/09 = Erev YK) : à valider par Jacques. **Gaps vol** : TBS aucun direct S1-S4 (premier direct S5 18/10) ; AMS pas de direct dimanche S3, S4, S6, S7 ; MNE uniquement S3 + S5. **Gap hôtel** : Brown Hills Paphos pas de dispo S5, disponible S6 (761,48$ total). **Écarts > 15 %** : Prague (meilleur 2690₪ vs publié 3260₪, -17%), Vienne (meilleur 1930₪ vs publié 2520₪, -23%), Amsterdam (meilleur 2610₪ vs publié 1900₪, +37%) — les 3 nécessitent arbitrage Jacques avant publication. **Trigger** : trig_01AC9Z8TrgTpLToieNmSJ6G4 sans connecteurs (blocage API connu) — run manuel via session interactive avec Kiwi.com + Booking.com. Action requise : recréer la routine depuis claude.ai/routines avec les 2 connecteurs. | OK (manuel) |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
