# Prix package séjour casher — CouponKasher

Généré par `pipeline/pricing.py` à partir du run vol (Kiwi.com) + hôtel (Booking.com).
Ne pas éditer à la main — le prochain run écrase ce fichier.

- **Run** : 2026-08-25 (premier run package vol+hotel — validation de bout en bout du branchement Kiwi.com + Booking.com)
- **Schéma** : 3 nuits / 4 jours, depart dimanche -> retour mercredi (repli lundi -> jeudi si pas de direct le dimanche). Fenetre S1-S8 : S1 30/08, S2 06/09, S3 13/09, S4 20/09, S5 27/09, S6 04/10, S7 11/10, S8 18/10.
- **Taux appliqué** : 1 USD = 3.05 ILS · marge 15 % · formule `(vol + hôtel/pers) ÷ 0.85 × 3.05`
- **Généré le** : 2026-08-26 14:11 UTC

> **Calendrier** — Roch Hachana 5787 : vendredi 11/09 au soir -> dimanche 13/09 au soir. Le depart dominical de S3 (13/09) tombe en plein Yom Tov : repli lundi 14/09. Yom Kippour : dimanche 20/09 au soir -> lundi 21/09 au soir. Le depart de S4 tombe a l'entree de Kippour et le lundi est Kippour lui-meme : S4 est inexploitable, ni dimanche ni lundi. Souccot : 25/09 au soir -> 02/10 au soir, Sim'hat Torah en Israel jusqu'au 03/10 au soir. S5 (27/09) est en 'hol hamoed : vendable mais en pic de demande israelienne. S6 a S8 (04/10, 11/10, 18/10) sont le creux post-fetes — c'est la que les prix s'effondrent.

## À publier — meilleur prix par destination

| Destination | Meilleur ₪ | Semaine | Publié ₪ | Écart | Décision |
|---|---|---|---|---|---|
| Tel Aviv (—) | 1160 | S8 | — | — | ⛔ cacherout à trancher — ne pas publier |
| Budapest (BUD) | 1390 | S8 | 1390 | +0 % | publiable |
| Naples (NAP) | 1450 | S7 | — | — | ⛔ cacherout à trancher — ne pas publier |
| Kinneret (—) | 1540 | S8 | — | — | ⛔ cacherout à trancher — ne pas publier |
| Mitzpé Ramon (—) | 1580 | S10 | — | — | ⛔ cacherout à trancher — ne pas publier |
| Paphos (PFO) | 1590 | S8 | 1590 | +0 % | publiable |
| Nahariya (—) | 1600 | S8 | — | — | ⛔ cacherout à trancher — ne pas publier |
| Hadera (—) | 1660 | S8 | — | — | ⛔ cacherout à trancher — ne pas publier |
| Chalkida (ATH) | 1800 | S8 | 1800 | +0 % | publiable |
| Modiin (—) | 1810 | S8 | — | — | ⛔ cacherout à trancher — ne pas publier |
| Amsterdam (AMS) | 1900 | S1 | 1900 | +0 % | publiable |
| Shavei Zion (—) | 1910 | S8 | — | — | pas de prix affiché sur le site |
| Jérusalem (—) | 1970 | S8 | — | — | ⛔ cacherout à trancher — ne pas publier |
| Tbilissi (TBS) | 2000 | S8 | 2000 | +0 % | publiable |
| Paphos (PFO) | 2240 | S6 | 2240 | +0 % | publiable |
| Vienne (VIE) | 2520 | S1 | 2520 | +0 % | publiable |
| Budva (TIV) | 2580 | S8 | 2580 | +0 % | publiable |
| Londres (LON) | 2660 | S6 | 2660 | +0 % | publiable |
| Prague (PRG) | 3260 | S2 | 3260 | +0 % | publiable |
| Neve Ativ (—) | 3500 | S8 | — | — | pas de prix affiché sur le site |
| Venise (VCE) | 3990 | S1 | — | — | ⛔ cacherout à trancher — ne pas publier |

## Détail S1

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-08-30 · dimanche | 236 | 250.14 | 1740 | ok · nom Booking retourne = 'Hotel & Residence, Palace Quarter' alors que la reference dit 'Hotel & Apartments' — a confirmer par Jacques |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-08-30 · dimanche | 401 | 128.62 | 1900 | ok · vol Blue Bird A/R, 0 escale |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-08-30 · dimanche | 160 | 377.84 | 1920 | ok · vol Israir aller / Blue Bird retour, 0 escale |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-08-30 · dimanche | 364 | 340.68 | 2520 | ok · vol Blue Bird A/R, 0 escale |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-08-31 · lundi (repli) | 543 | 285.99 | 2970 | ok · aucun vol direct le dimanche 30/08 — repli lundi applique, hotel re-interroge sur les memes dates decalees |
| Paphos (PFO) | Paphos Hills Resort & Spa by Brown Hotels | 2026-08-30 · dimanche | 166 | 809.03 | 3490 | ok · hotel a 270 $/nuit pour 2 en pic d'aout |
| Londres (LON) | Croft Court Hotel | 2026-08-30 · dimanche | 829 | 185.02 | 3630 | ok · Arkia TLV-STN A/R, 0 escale. Kiwi ne renvoie AUCUN direct sur LHR : les directs TLV-Londres passent par Stansted, Luton et Gatwick. Interroger la ville et non LHR, sinon faux gap. Croft Court est a Golders Green, donc STN/LTN conviennent |
| Budva (TIV) | Hotel Harmonia by Dukley | 2026-08-30 · dimanche | 515 | 559.97 | 3850 | ok · Israir TLV-TIV A/R, 0 escale. Le direct est sur Tivat, pas Podgorica (TGD) |
| Venise (VCE) | Rimon Place Kosher | 2026-08-30 · dimanche | 687 | 426.55 | 3990 | certification a trancher · El Al A/R 0 escale, hotel dispo. Prix NON publie : statut cacherout contradictoire entre le master portfolio (Tier 3) et la reference promo (mehadrin) |
| Prague (PRG) | Kosher Hotel King David Prague | 2026-08-30 · dimanche | 456 | 1013.19 | 5270 | ok · hotel a 675 $/nuit pour 2 en pic d'aout — c'est lui qui fait exploser le package, pas le vol |
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-08-30 · dimanche | 166 | — | — | gap hotel · Booking: WellClub Resort complet sur ces dates (hotel_names_no_availability). Vol OK a 166 $ — c'est l'hotel qui bloque |
| Paphos (PFO) | Greek Village Hotel | 2026-08-30 · dimanche | 166 | — | — | gap hotel · Booking: aucune disponibilite sur ces dates (hotel_names_no_availability) |
| Rome (FCO) | NEMAN Maison | 2026-08-30 · dimanche | 359 | — | — | gap hotel · Wizz Air A/R 0 escale. NEMAN Maison est hors Booking.com : prix hotel a fournir par Jacques |
| Berlin (BER) | King David Garden | 2026-08-30 · dimanche | 326 | — | — | non vendable — cacherout douteuse · Israir/Blue Bird en direct a 326 $. King David Garden est hors Booking et n'a jamais ete approuve |
| Lac de Garde (BGY) | Olympic Kosher Sirmione / Villa Maria (KosherGarda) | 2026-08-30 · dimanche | 316 | — | — | non vendable — saisonnier · Blue Bird direct TLV-Bergame a 316 $, Sirmione a ~80 km. Hotels hors Booking |

## Détail S1-S8

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Vérone (VRN) | — | — | — | — | — | aucun vol direct · zero resultat sur VRN et zero en interrogeant la ville, sur les huit semaines. Aucun hotel identifie par ailleurs |
| Marbella (AGP) | Marvella Hotel | — | — | — | — | aucun vol direct · zero resultat sur AGP et sur Malaga, sur les huit semaines. Le 'pas de direct structurel' de la reference est confirme |
| Lublin (WAW/LUZ) | Hotel Ilan (reference promo) / Hotel Olive (site) — DIVERGENCE a trancher | — | — | — | — | aucun vol direct · aucun direct TLV-Lublin. Divergence a trancher entre Hotel Ilan (reference promo) et Hotel Olive (site) |

## Détail S10

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Mitzpé Ramon (—) | Jacob Mitzpe Ramon | 2026-11-01 · dimanche | — | 1350.01 | 1580 | cacherout non documentee · prix Booking en ILS pour 2 adultes, 3 nuits. Sejour domestique : aucun vol. Aucune disponibilite en S8 (18/10) : releve reporte au 01/11, hors fenetre S1-S8. Fiche Booking servie sous l'ancien slug adama-by-tzukim, adresse et nom affiche conformes (4 Har Boker St, Mitzpe Ramon). Badges du site : מדבר |

## Détail S2

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-09-06 · dimanche | 171 | 384.5 | 1990 | ok · l'hotel complet en S1 est disponible en S2 |
| Paphos (PFO) | Paphos Hills Resort & Spa by Brown Hotels | 2026-09-06 · dimanche | 171 | 615.09 | 2820 | ok · 1230 $ contre 1618 $ en S1 — meme effet de pic d'aout que Prague |
| Prague (PRG) | Kosher Hotel King David Prague | 2026-09-06 · dimanche | 359 | 550.05 | 3260 | ok · TUS Airways A/R 0 escale. Hotel a 1100 $ contre 2026 $ une semaine plus tot : le +79 % de S1 etait bien le pic d'aout, pas un prix structurel |
| Paphos (PFO) | Greek Village Hotel | 2026-09-06 · dimanche | 171 | — | — | faux match Booking · PIEGE REPRODUCTIBLE : Booking repond 'Filerimos Village Hotel' a Ialyssos (Rhodes, GRECE) meme avec destination='Paphos, Cyprus' en contexte. Teste deux fois, meme reponse. L'hotel n'est pas atteignable par le connecteur : prix a fournir par Jacques |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-09-06 · dimanche | — | 136.82 | — | gap vol · aucun direct TLV-AMS sous 450 $ en S2 (401 $ en S1) et hotel plus cher (274 $ contre 257 $) : S1 reste le meilleur prix de la fenetre pour cette destination |

## Détail S3

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budva (TIV) | Hotel Harmonia by Dukley | 2026-09-14 · lundi (repli Roch Hachana) | 401 | 450.91 | 3050 | ok · encore en saison balneaire : 902 $ contre 749 $ en S8 |
| Prague (PRG) | Kosher Hotel King David Prague | 2026-09-14 · lundi (repli Roch Hachana) | 359 | 672.16 | 3700 | ok · hotel a 1344 $ contre 1100 $ en S2 : S2 reste le meilleur pour Prague |

## Détail S5

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-09-27 · dimanche | — | — | — | gap hotel · complet — 'hol hamoed Souccot |
| Paphos (PFO) | Brown Hills | 2026-09-27 · dimanche | — | — | — | gap hotel · complet — 'hol hamoed Souccot |
| Tbilissi (TBS) | Cron Palace | 2026-09-27 · dimanche | — | — | — | gap hotel · complet — 'hol hamoed Souccot |
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-09-27 · dimanche | — | 234.0 | — | gap vol · hotel disponible a 468 $ mais aucun vol direct sous 236 $ cette semaine-la |

## Détail S6

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-10-04 · dimanche | 178 | 260.03 | 1570 | ok · moins bon que S8 |
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-10-04 · dimanche | 170 | 329.25 | 1790 | ok · moins bon que S8 |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-10-04 · dimanche | 152 | 467.49 | 2220 | ok · vol Israir 152 $ (le moins cher de la fenetre) mais hotel a 935 $ contre 756 $ en S1 : le package reste moins bon qu'en S1 |
| Paphos (PFO) | Paphos Hills Resort & Spa by Brown Hotels | 2026-10-04 · dimanche | 170 | 455.11 | 2240 | ok · MEILLEUR de la fenetre pour cet hotel : l'hotel n'est pas disponible en S8 et coute plus cher en S7 |
| Londres (LON) | Croft Court Hotel | 2026-10-04 · dimanche | 437 | 306.75 | 2660 | ok · Wizz UK 437 $ contre 829 $ en S1. Aller sur Gatwick, retour sur Luton : deux aeroports differents, a valider avec le client |
| Tbilissi (TBS) | Cron Palace | 2026-10-04 · dimanche | 329 | — | — | gap hotel · hotel complet |
| Budva (TIV) | Harmonia by Dukley | 2026-10-04 · dimanche | 445 | — | — | gap hotel · hotel complet |

## Détail S7

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Naples (NAP) | Hotel Cristina | 2026-10-12 · lundi | 148 | 256.73 | 1450 | non vendable — certif en attente · chiffrable de bout en bout, et parmi les moins chers du portfolio. Mais l'hotel n'est pas casher : seul un restaurant glatt mehadrin est a proximite. Best Western JFK au meme endroit a 519 $ |
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-10-11 · dimanche | 142 | 310.73 | 1620 | ok · vol au plus bas mais hotel a 621 $ : moins bon que S8 |
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-10-11 · dimanche | 151 | 329.25 | 1720 | ok · vol El Al 151 $ et hotel 658 $ : meilleur package de toute la fenetre |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-10-11 · dimanche | 155 | 379.69 | 1910 | ok · moins bon que S8 |
| Paphos (PFO) | Paphos Hills Resort & Spa by Brown Hotels | 2026-10-11 · dimanche | 151 | 507.62 | 2360 | ok · troisieme baisse consecutive : 1618 $ en S1, 1230 $ en S2, 1015 $ en S7 |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-10-12 · lundi | 389 | 310.11 | 2500 | ok · moins bon que S8 sur les deux postes |
| Budva (TIV) | Harmonia by Dukley | 2026-10-11 · dimanche | 392 | — | — | gap hotel · hotel complet |

## Détail S8

| Destination | Hôtel | Départ | Vol A/R $ | Hôtel 3 nuits /pers $ | Package ₪ | Statut |
|---|---|---|---|---|---|---|
| Tel Aviv (—) | Jacob Shenkin Hotel | 2026-10-18 · dimanche | — | 993.27 | 1160 | cacherout non documentee · prix Booking en ILS pour 2 adultes, 3 nuits. Sejour domestique : aucun vol. Badges du site : בוטיק, מרכז העיר |
| Budapest (BUD) | Silver Crown Hotel & Residence, Palace Quarter | 2026-10-18 · dimanche | 142 | 246.94 | 1390 | ok · vol Wizz a 142 $ contre 236 $ en S1 |
| Kinneret (—) | Jacob Ohalo Kinneret | 2026-10-18 · dimanche | — | 1309.49 | 1540 | cacherout non documentee · prix Booking en ILS pour 2 adultes, 3 nuits. Sejour domestique : aucun vol. Badges du site : נוף לכנרת |
| Paphos (PFO) | WellClub Resort - Suites & Wellness | 2026-10-18 · dimanche | 151 | 294.6 | 1590 | ok · MEILLEUR de la fenetre : hotel a 589 $, son plus bas |
| Nahariya (—) | Jacob Sea Life Nahariya | 2026-10-18 · dimanche | — | 1365.01 | 1600 | cacherout non documentee · prix Booking en ILS pour 2 adultes, 3 nuits. Sejour domestique : aucun vol. Badges du site : חוף ים, ספא |
| Hadera (—) | Jacob Resort Hadera | 2026-10-18 · dimanche | — | 1417.5 | 1660 | cacherout non documentee · prix Booking en ILS pour 2 adultes, 3 nuits. Sejour domestique : aucun vol. Badges du site : חוף ים, ספא |
| Chalkida (ATH) | Brown Beach Chalkida Resort, a member of Brown Hotels | 2026-10-18 · dimanche | 148 | 354.99 | 1800 | ok · MEILLEUR de la fenetre : vol Wizz a 148 $ et hotel au plus bas de la fenetre |
| Modiin (—) | Jacob Modiin | 2026-10-18 · dimanche | — | 1545.0 | 1810 | cacherout non documentee · prix Booking en ILS pour 2 adultes, 3 nuits. Sejour domestique : aucun vol. Badges du site : עסקי |
| Shavei Zion (—) | Jacob Nea | 2026-10-18 · dimanche | — | 1631.62 | 1910 | ok · prix Booking en ILS pour 2 adultes, 3 nuits. Sejour domestique : aucun vol. Badges du site : כשר, וילות פרטיות |
| Jérusalem (—) | Jacob Harmony | 2026-10-18 · dimanche | — | 1679.99 | 1970 | cacherout non documentee · prix Booking en ILS pour 2 adultes, 3 nuits. Sejour domestique : aucun vol. Badges du site : מלון בוטיק, נחלת שבעה |
| Tbilissi (TBS) | Cron Palace kosher Tbilisi Hotel | 2026-10-18 · dimanche | 291 | 267.04 | 2000 | ok · vol Israir a 291 $ contre 543 $ en S1 — la destination la plus volatile du portfolio |
| Vienne (VIE) | Vayalen Boutique Hotel | 2026-10-18 · dimanche | 426 | 287.22 | 2550 | ok · seul vol direct de la fenetre sous 500 $, mais le package reste au-dessus de S1 |
| Budva (TIV) | Hotel Harmonia by Dukley | 2026-10-18 · dimanche | 345 | 374.59 | 2580 | ok · vol Israir 345 $ contre 515 $ en S1, et l'hotel passe de 1120 $ a 749 $ hors saison balneaire |
| Neve Ativ (—) | Jacob Neve Ativ | 2026-10-18 · dimanche | — | 2975.01 | 3500 | ok · prix Booking en ILS pour 2 adultes, 3 nuits. Sejour domestique : aucun vol. Badges du site : כשר, ספא |
| Rome (FCO) | NEMAN Maison | 2026-10-18 · dimanche | 132 | — | — | gap hotel · vol Wizz a 132 $ contre 359 $ en S1 — le vol le moins cher de tout le portfolio. Hotel NEMAN toujours hors Booking |
| Paphos (PFO) | Brown Hills | 2026-10-18 · dimanche | 151 | — | — | gap hotel · hotel complet alors que le vol est au plus bas |
| Amsterdam (AMS) | ibis budget Amsterdam City South | 2026-10-18 · dimanche | — | 133.91 | — | gap vol · hotel au plus bas (268 $) mais aucun vol direct sous 600 $ : S1 reste le meilleur |
| Eilat (—) | Jacob Eilat | 2026-10-18 · dimanche | — | — | — | gap hotel · aucune disponibilite Booking sur les quatre fenetres testees : 30/08, 18/10, 01/11, 08/11 et 15/11. Le connecteur ne resout que le nom « Jacob Eilat » ; ni « Jacob Hotel Eilat » ni « Jacob Club Eilat » ne matchent. A verifier en direct aupres de la chaine. |

## Lecture

- Un écart supérieur à 15 % vs le prix publié sur couponkasher.co.il n'est **jamais** publié automatiquement : il doit être confirmé par Jacques.
- Le site affiche un prix « à partir de » (החל ב-) : la valeur publiable est donc le meilleur prix de la destination sur la fenêtre, toutes semaines confondues.
- Un vol est retenu uniquement s'il est **direct** (0 escale) et hors samedi. Pas de vol direct le dimanche → repli sur le lundi, signalé dans la colonne Départ.
- Le prix hôtel vient de Booking.com par **nom d'hôtel exact**. Si le nom retourné diffère du partenaire attendu, la ligne est écartée — le connecteur peut répondre par un hôtel homonyme situé dans un autre pays.
