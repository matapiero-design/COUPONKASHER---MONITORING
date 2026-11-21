# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-11-21 (run automatisé, vol seul)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol seul (pas de vérification hôtel/package sur ce run), départ dimanche 29/11/2026 par défaut, 3 nuits
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour toutes destinations
- **Statut connecteur Booking.com** : non interrogé sur ce run (vérification vol uniquement)

## Contrôle ponctuel — run 2026-11-21 (vol seul, 7 destinations)

Run automatisé quotidien, vol uniquement (pas de vérification hôtel/package). Portée restreinte
aux 7 destinations historiques (PRG, VIE, FCO, PFO, ATH, BUD, TBS) — hors Groupe A étendu actuel
(AMS, LON, MNE non inclus ici). Premier contrôle depuis le run du 2026-09-15 (interruption de
~2 mois). Fenêtre interrogée : départ dimanche 29/11/2026 → retour mercredi 02/12/2026 (3 nuits),
soit environ 8 jours avant départ — un délai de réservation bien plus court que les runs
précédents (souvent 1 à 8 semaines à l'avance), ce qui rend la comparaison directe avec les
tarifs S1-S8 ci-dessous approximative (dynamique tarifaire différente selon le délai de
réservation).

| Destination | Aéroport | Prix vol A/R ($) | Compagnies | Statut |
|---|---|---|---|---|
| Rome | FCO | 141 | Wizz Air Malta A/R | ✅ dimanche→mercredi |
| Chalkida | ATH | 163 | Blue Bird (aller) / Wizz Air Malta (retour) | ✅ dimanche→mercredi |
| Budapest | BUD | 210 | Wizz Air A/R | ⚠️ +48% vs dernier relevé comparable (142$, S8 09/15) — voir anomalies |
| Tbilissi | TBS | 214 | Israir (aller) / El Al (retour) | ✅ dimanche→mercredi |
| Prague | PRG | 339 | Smartwings A/R | ✅ dimanche→mercredi |
| Vienne | VIE | 378 | Austrian (aller) / Blue Bird (retour) | ⚠️ +20% vs dernier relevé comparable (316$, S8 09/15) |
| Paphos (WellClub) | PFO | — | — | ⛔ aucun direct dimanche 29/11 — **repli lundi 30/11 → jeudi 03/12 : 147$** (El Al aller / Arkia retour) |

**Anomalies de prix signalées (écart > 15 % vs dernier relevé comparable, règle du 26/08/2026 —
alerte, pas de blocage)** :
- **Budapest (BUD) : 210$ vs 142$ au run S8 du 09/15 (+48 %)** — écart le plus marqué du run,
  à surveiller sur les prochains jours pour distinguer un effet de délai de réservation court
  (8 jours vs plusieurs semaines pour S8) d'une hausse structurelle.
- Vienne (VIE) : 378$ vs 316$ au run S8 du 09/15 (+20 %).
- Chalkida (ATH) : 163$ vs 140$ au run S8 du 09/15 (+16 %) — juste au-dessus du seuil.
- Prague (PRG) et Tbilissi (TBS) restent dans une fourchette cohérente avec les derniers relevés
  (339$ vs 309$, +10 % ; 214$ vs 210$, +2 %) — pas d'alerte.

**Gap vol signalé** : Paphos (PFO) — zéro résultat direct pour un départ dimanche 29/11/2026
(contrairement aux runs précédents où le dimanche était systématiquement disponible sur cette
ligne). Repli lundi appliqué conformément à la règle du schéma 3 nuits/4 jours : vol direct
confirmé lundi 30/11 → jeudi 03/12 à 147$. À surveiller si ce gap du dimanche est ponctuel
(aléa de planning compagnie) ou récurrent sur les prochains runs.

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
| 2026-11-21 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) — run vol seul, pas d'hôtel/package. Départ dimanche 29/11/2026 → retour mercredi 02/12/2026 (3 nuits), ~8 jours avant départ (délai de réservation court, contrairement aux runs précédents). Premier run depuis le 2026-09-15 (~2 mois d'interruption). | **Gap vol** : PFO aucun direct dimanche 29/11 — repli lundi 30/11 → jeudi 03/12 à 147$ (El Al/Arkia). **Écarts > 15 % vs dernier relevé comparable (S8, run 09/15)** : Budapest +48 % (210$ vs 142$, le plus marqué), Vienne +20 % (378$ vs 316$), Chalkida +16 % (163$ vs 140$) — à confirmer sur les prochains runs quotidiens pour distinguer effet du délai de réservation court vs tendance de fond. Prague (+10 %) et Tbilissi (+2 %) dans une fourchette normale. | OK |
| 2026-09-15 03:32 | PRG, VIE, AMS, PFO (WellClub + Brown Hills), ATH, BUD, TBS, LON, MNE (10 dest. Groupe A — Venise bloquée cacherout contestée). S1-S8 complet (run manuel, 3 semaines sans run) | **Haggim 5787** : S1 (retour 23/09 = RH j2) et S3/S4 partiellement bloquées — CORRECTION calendrier Israël : S3 (retour 07/10 = Hol HaMoed) et S4 (retour 14/10 = post-Shimini Atzeret) VALIDES pour clientèle israélienne. S2 (retour 30/09 = Erev YK) : à valider par Jacques. **Gaps vol** : TBS aucun direct S1-S4 (premier direct S5 18/10) ; AMS pas de direct dimanche S3, S4, S6, S7 ; MNE uniquement S3 + S5. **Gap hôtel** : Brown Hills Paphos pas de dispo S5, disponible S6 (761,48$ total). **Écarts > 15 %** : Prague (meilleur 2690₪ vs publié 3260₪, -17%), Vienne (meilleur 1930₪ vs publié 2520₪, -23%), Amsterdam (meilleur 2610₪ vs publié 1900₪, +37%) — les 3 nécessitent arbitrage Jacques avant publication. **Trigger** : trig_01AC9Z8TrgTpLToieNmSJ6G4 sans connecteurs (blocage API connu) — run manuel via session interactive avec Kiwi.com + Booking.com. Action requise : recréer la routine depuis claude.ai/routines avec les 2 connecteurs. | OK (manuel) |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
