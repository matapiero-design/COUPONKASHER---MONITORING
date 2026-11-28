# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-11-28 (run ad hoc, vol seul — pas le run quotidien package vol+hôtel décrit dans `ROUTINE_PROMPT.md`)
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol seul (pas de connecteur Booking.com dans ce run), au départ de TLV, 0 escale, A/R 3 nuits. Deux dates testées : dimanche 29/11 (J+1, dernière minute) et dimanche 06/12 (J+8, référence) — voir section ci-dessous et le journal.
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour toutes destinations sauf PFO en direct dimanche (voir anomalies)
- **Statut connecteur Booking.com** : non interrogé dans ce run (hors périmètre de la demande — vol seul)

## Run du 2026-11-28 — vol seul, 7 destinations

Run ad hoc (hors cadence quotidienne package vol+hôtel) : vérification Kiwi.com, TLV au départ,
0 escale strict, aller-retour 3 nuits, 1 adulte, USD. Deux fenêtres testées pour distinguer un
effet dernière-minute d'une tendance de fond (voir anomalies ci-dessous).

### Dimanche 29/11/2026 → mercredi 02/12/2026 (J+1, dernière minute)

| Destination | Aéroport | Prix vol A/R ($) | Compagnies (aller/retour) | Statut |
|---|---|---|---|---|
| Rome | FCO | 156 | Wizz Air Malta / Wizz Air Malta | ✅ meilleur prix du run |
| Tbilissi | TBS | 215 | El Al / El Al | ✅ |
| Chalkida | ATH | 184 | Israir / Wizz Air Malta | ✅ |
| Prague | PRG | 340 | Smartwings / TUS Airways | ✅ |
| Vienne | VIE | 399 | Austrian / Blue Bird | ✅ |
| Budapest | BUD | 464 | Wizz Air / Wizz Air | ⚠️ voir anomalie — +227 % vs dernier relevé (S8, 08/11 : 142 $) |
| Paphos (PFO) | PFO | — | — | ⛔ aucun direct dimanche 29/11 — voir repli ci-dessous |

### Dimanche 06/12/2026 → mercredi 09/12/2026 (J+8, référence)

| Destination | Aéroport | Prix vol A/R ($) | Compagnies (aller/retour) | Statut |
|---|---|---|---|---|
| Rome | FCO | 269 | Wizz Air Malta / Wizz Air Malta | ✅ |
| Budapest | BUD | 381 | Wizz Air / Wizz Air | ✅ |
| Vienne | VIE | 570 | Blue Bird / Blue Bird | ✅ |
| Prague | PRG | 587 | Smartwings / Smartwings | ✅ |
| Chalkida | ATH | 407 | Blue Bird / El Al | ✅ |
| Tbilissi | TBS | 681 | Israir / El Al | ⚠️ voir anomalie |
| Paphos (PFO) | PFO | — | — | ⛔ aucun direct dimanche 06/12 non plus — voir repli ci-dessous |

### Paphos (PFO) — pas de direct dimanche sur les deux dates testées

Zéro résultat sur le code PFO en direct pour le dimanche 29/11 **et** pour le dimanche 06/12
(recherche confirmée, pas un gap de données — El Al et Arkia opèrent TLV-PFO mais pas le dimanche
sur cette fenêtre). Repli lundi testé (±3 jours autour du 29/11, 3 nuits) :

| Repli | Prix A/R ($) | Compagnies | Statut |
|---|---|---|---|
| Lundi 30/11 → jeudi 03/12 | 249 | El Al / Arkia | ✅ repli standard (lundi→jeudi) |
| Mardi 01/12 → vendredi 04/12 | 145 | El Al / El Al | ℹ️ meilleur prix trouvé sur la fenêtre, mais retour vendredi — à valider contre la règle d'atterrissage vendredi (11h hiver) : arrivée TLV 09h00, conforme |

### Anomalies constatées — à signaler à Jacques

- **Budapest** : 464 $ (29/11) et 381 $ (06/12), contre 142 $ au dernier relevé comparable (S8,
  départ 08/11/2026). Écart de +169 % à +227 % — nettement au-dessus du seuil de 15 %. Présent sur
  les deux dates testées : écart structurel probable, pas un artefact de date unique.
- **Vienne** : 399 $ (29/11) et 570 $ (06/12) contre 316 $ au dernier relevé (S8). Écart de +26 % à
  +80 %, au-dessus du seuil sur les deux dates.
- **Chalkida (ATH)** : 184 $ (29/11) et 407 $ (06/12) contre 140 $ au dernier relevé (S8). Écart de
  +31 % à +191 %.
- **Prague** : 340 $ (29/11) et 587 $ (06/12) contre 309 $ au dernier relevé (S8). +10 % (29/11,
  dans la norme) mais +90 % (06/12).
- **Tbilissi** : 215 $ (29/11, cohérent avec le dernier relevé à 210 $) mais 681 $ (06/12), soit
  +224 %. Grand écart entre les deux dates testées pour cette seule destination — cohérent avec la
  note déjà consignée (TBS : offre directe structurellement restreinte à El Al + Israir, donc plus
  volatile), mais l'ampleur mérite vérification avant publication.
- **Rome (FCO)** : premier relevé vol seul dans ce fichier — pas de valeur antérieure comparable.
  156 $ (29/11) et 269 $ (06/12) semblent cohérents avec le marché (vol Wizz Air direct, cluster de
  prix bas déjà documenté dans `pipeline/destinations.json`).
- **Pattern inhabituel à surveiller** : sur 5 destinations sur 6 comparables (toutes sauf Budapest),
  le vol testé à J+1 (29/11) est moins cher que celui testé à J+8 (06/12) — l'inverse du schéma
  habituel (les tarifs de dernière minute sont normalement plus chers, cf. journal du
  2026-08-20/2026-08-25). Les deux dates sont un dimanche, donc pas un effet jour de semaine.
  Hypothèse la plus probable : ouverture de sièges invendus à prix cassé à J-1 sur les vols
  TLV-Europe, mais non confirmé — à recouper sur un prochain run avant d'en tirer une conclusion
  commerciale.
- **Aucune valeur n'a été écrite dans `site/` ni dans `Data/package-prices.json`** : ce run est vol
  seul, sans hôtel, donc aucun prix package n'est calculable ni publiable depuis ces chiffres.

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
| 2026-11-28 (run ad hoc, vol seul) | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) — deux fenêtres : dimanche 29/11 (J+1) et dimanche 06/12 (J+8), A/R 3 nuits | **Gap vol** : PFO aucun direct dimanche sur les deux fenêtres testées — repli lundi 30/11→jeudi 03/12 à 249 $. **Écarts > 15 % vs dernier relevé (S8, 08/11)** : Budapest (+169 % à +227 %, sur les deux dates — probable écart structurel), Vienne (+26 % à +80 %), Chalkida/ATH (+31 % à +191 %), Tbilissi (+224 % sur la fenêtre J+8 seulement, cohérent avec son offre directe restreinte mais ampleur à vérifier), Prague (+90 % sur J+8 seulement). **Pattern à surveiller** : sur 5 destinations/6, le vol à J+1 est moins cher que celui à J+8 — inverse du schéma habituel de dernière minute ; non expliqué, à recouper sur un prochain run. Rome (FCO) : premier relevé vol seul, pas de comparaison possible. Run vol seul uniquement (pas de connecteur Booking.com dans ce run) — aucun prix package ni publication. | OK (Kiwi.com) — Booking.com non utilisé, hors périmètre |
| 2026-09-15 03:32 | PRG, VIE, AMS, PFO (WellClub + Brown Hills), ATH, BUD, TBS, LON, MNE (10 dest. Groupe A — Venise bloquée cacherout contestée). S1-S8 complet (run manuel, 3 semaines sans run) | **Haggim 5787** : S1 (retour 23/09 = RH j2) et S3/S4 partiellement bloquées — CORRECTION calendrier Israël : S3 (retour 07/10 = Hol HaMoed) et S4 (retour 14/10 = post-Shimini Atzeret) VALIDES pour clientèle israélienne. S2 (retour 30/09 = Erev YK) : à valider par Jacques. **Gaps vol** : TBS aucun direct S1-S4 (premier direct S5 18/10) ; AMS pas de direct dimanche S3, S4, S6, S7 ; MNE uniquement S3 + S5. **Gap hôtel** : Brown Hills Paphos pas de dispo S5, disponible S6 (761,48$ total). **Écarts > 15 %** : Prague (meilleur 2690₪ vs publié 3260₪, -17%), Vienne (meilleur 1930₪ vs publié 2520₪, -23%), Amsterdam (meilleur 2610₪ vs publié 1900₪, +37%) — les 3 nécessitent arbitrage Jacques avant publication. **Trigger** : trig_01AC9Z8TrgTpLToieNmSJ6G4 sans connecteurs (blocage API connu) — run manuel via session interactive avec Kiwi.com + Booking.com. Action requise : recréer la routine depuis claude.ai/routines avec les 2 connecteurs. | OK (manuel) |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
