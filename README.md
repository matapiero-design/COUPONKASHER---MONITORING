# CouponKasher — Automatisation des tarifs

Repo support de l'automatisation des prix de séjours casher CouponKasher : vol direct TLV via
**Kiwi.com**, hôtel casher partenaire via **Booking.com**, prix package calculé, puis publié sur
couponkasher.co.il quand Jacques le décide.

## Le principe : calculer ≠ publier

Deux étages strictement séparés, pour qu'un prix de marché qui bouge ne se retrouve jamais sur le
site sans validation :

| Étage | Où | Qui écrit | Effet |
|---|---|---|---|
| **Calculer** | `Data/` | la Routine quotidienne, automatiquement | aucun impact client |
| **Publier** | `site/` | Jacques (ou Claude sur sa demande explicite) | change le prix affiché |

Le run quotidien ne touche jamais à `site/`. Il calcule, compare aux prix publiés, et signale les
écarts supérieurs à 15 % — c'est Jacques qui tranche.

## Contenu

- `ROUTINE_PROMPT.md` — le prompt exact envoyé par la Routine à chaque déclenchement, et les
  paramètres de cadence/cible.
- `pipeline/destinations.json` — source unique des O&D : clé hébraïque du site, code IATA, nom
  d'hôtel exact tel que Booking.com le résout, mention de cacherout.
- `pipeline/pricing.py` — calcul du prix package et génération des fichiers `Data/package-prices.*`.
  Taux et marge y sont écrits en dur, en un seul endroit.
- `Data/runs/run-<date>.json` — le relevé brut d'un run (vol + hôtel, par destination).
- `Data/package-prices.md` / `.json` — prix package du dernier run, avec écarts vs le site.
- `Data/flight-prices.md` — historique vol seul + journal des runs.
- `site/index.html` — la page du site, dont les prix sont lus depuis `prices.json`.
- `site/prices.json` — **les prix effectivement publiés**. Un seul endroit à modifier pour changer
  un tarif affiché.
- `pipeline/export_xlsx.py` — produit `Data/CouponKasher_grille_S1-S8.xlsx`, le classeur consultable
  (grille, relevés bruts, paramètres, prix en ligne, calendrier). À relancer après chaque run.

## Formule

```text
prix par personne (₪) = (vol A/R $ + hôtel 3 nuits par personne $) ÷ 0.85 × 3.05
```

`0.85` = 15 % de marge intégrée. `3.05` = taux USD/ILS fixe du business — **jamais** le taux du
jour, et jamais modifié sans demande explicite de Jacques. Arrondi à la dizaine de shekels
inférieure.

Le taux ne vit qu'à **un seul endroit** : la constante `TAUX_USD_ILS` de `pipeline/pricing.py`.
Personne ne recalcule un prix à la main — ni la Routine, ni une session de devis. Le `3.65` qui
figure encore dans le skill `dashboard-suivi-prix-sejours-casher` est périmé et doit y être
corrigé : il datait d'un dollar bien plus fort, et c'est lui qui explique que les prix publiés
aujourd'hui sur le site soient trop hauts d'environ 16 %.

Le prix Booking.com est le total du séjour pour 2 adultes : le prix par personne est ce total ÷ 2.

## Le site

`site/index.html` ne contient plus de tarif décidé dans le HTML : chaque bloc prix porte un
attribut `data-price-city` et la page lit `prices.json` au chargement. Les valeurs écrites dans le
HTML restent en repli — si `prices.json` est absent ou illisible, la page affiche les anciens prix
au lieu de casser.

Publier un nouveau tarif = modifier `site/prices.json`, puis déposer `index.html` + `prices.json`
sur Netlify (projet `spiffy-swan-239d90`) par drag-and-drop. Le déploiement reste manuel : aucun
connecteur Netlify n'est configuré à ce jour.

## État de la grille au 25/08/2026

10 des 13 destinations tarifées sur le site sont à jour au taux 3.05, chiffrées en live
(vol Kiwi.com + hôtel Booking.com) sur la fenêtre S1 (30/08 → 02/09) et S2 (06/09 → 09/09).

Trois restent en attente d'une décision qui n'appartient pas au pipeline :

Quatre destinations sont **en attente** (`statut: en-attente` dans `site/prices.json`) : leur carte
affiche `לפי בקשה` au lieu d'un prix, plutôt que de laisser en ligne un tarif hérité du taux 3.65.

| Destination | Blocage | Ce qu'il faut |
|---|---|---|
| Venise | cacherout contradictoire — Tier 3 au master portfolio, mehadrin à la référence promo | trancher le statut de Rimon Place |
| Rome | NEMAN Maison absent de Booking.com (vol vérifié à 132 $) | le tarif 3 nuits, de la main de Jacques |
| Paphos Greek Village | Booking répond un hôtel de Rhodes sur ce nom | le tarif 3 nuits, de la main de Jacques |
| Paris | Aida Opera est en liste d'exclusion (pas mehadrin) | retirer la carte ou changer d'hôtel |

Le prix qu'elles affichaient est conservé dans `dernier_prix_affiche_ils`, pour mémoire.

## Pièges rencontrés, et pourquoi ils sont dans le code

- **Un code IATA sans résultat n'est pas un gap.** Kiwi ne renvoie aucun direct sur LHR ni sur TGD,
  alors que les lignes existent sur STN/LTN/LGW et sur TIV. D'où le champ `kiwi_flyTo`.
- **Un nom d'hôtel peut résoudre vers un autre pays.** « Greek Village Hotel » à Paphos renvoie
  « Filerimos Village Hotel » à Rhodes. Le nom retourné se vérifie toujours.
- **Le pic d'août fausse tout.** Prague et Paphos Brown Hills passaient le seuil de 15 % sur la
  seule semaine du 30/08, et rentraient dans les clous une semaine plus tard. D'où le raisonnement
  en « meilleur prix de la fenêtre », qui correspond au « החל ב- » affiché.
- **Une cacherout non tranchée bloque la publication**, quel que soit l'écart.

## Logique métier

Les règles (destinations, contrainte Shabbat, exclusion des vols à escale, exclusion du samedi,
cadence S1-S3 / S4-S8, certification casher Tier 1) sont définies dans le skill
`dashboard-suivi-prix-sejours-casher`. Ce repo automatise son déclenchement et stocke ses résultats.

## Historique des décisions

- **25/08/2026 — taux fixé à 3.05.** Confirmé par Jacques. Le dollar valant ~2.98 ₪ sur le marché,
  3.05 préserve la marge de 15 % avec un léger coussin. Les prix actuellement publiés sur le site
  ayant été construits à 3.65, la quasi-totalité de la grille est appelée à baisser d'environ 16 %
  à la prochaine publication — ce n'est pas une chute de coût, c'est un rattrapage de taux.
- **25/08/2026 — hôtel branché sur Booking.com.** `hotel_names` permet d'interroger le partenaire
  casher par son nom exact, ce que lastminute.com ne savait pas faire. Le prix hôtel n'est plus une
  estimation.
- **25/08/2026 — séparation calculer / publier.** Le run quotidien écrit dans `Data/` et jamais
  dans `site/`.
- **25/08/2026 — publication de la grille.** Budapest, Chalkida, Vienne, Tbilissi, Prague, Londres,
  Monténégro, Paphos WellClub, Paphos Brown Hills et Amsterdam publiés au taux 3.05. Deux écarts
  au-delà du seuil publiés sur instruction explicite de Jacques : Paphos WellClub (-29 %, l'hôtel
  complet fin août se libère en S2) et Amsterdam (-15 %, pur effet de taux — à 3.65 les mêmes coûts
  donnaient exactement le prix affiché).
- **26/08/2026 — règle de publication : le prix le plus bas de la fenêtre.** Décidé par Jacques.
  Le site affiche « החל ב- », donc la valeur publiée est le minimum sur les 8 semaines glissantes,
  quelle que soit la semaine où il tombe. Conséquence assumée : un prix affiché peut correspondre à
  une date à deux mois, pas à la semaine prochaine. Le seuil de 15 % du pipeline ne bloque plus la
  publication — il reste une alerte à regarder, pas un verrou.
- **26/08/2026 — fenêtre S3-S8 balayée.** Roch Hachana retire le départ dominical de S3 (repli lundi
  14/09) et Kippour rend S4 inexploitable, dimanche comme lundi. Le creux post-fêtes (S6-S8) fait
  chuter Tbilissi et le Monténégro de 33 %, Londres de 27 %, Budapest de 20 %.
- **26/08/2026 — fenêtre S1-S8 fermée pour de bon.** 46 relevés. Le côté hôtelier était le point
  faible : il n'était interrogé qu'à la date du vol le moins cher, ce qui suppose à tort que la
  semaine du vol le moins cher est celle du séjour le moins cher. Chalkida prouvait le contraire.
  Après balayage complet, trois minima ont bougé (Paphos WellClub, Chalkida, Paphos Brown Hills).
  Constat structurel : 'hol hamoed Souccot (S5) est massivement **complet** côté hôtels, et le creux
  réel est S6-S8, avec des disponibilités hôtelières trouées — Tbilissi et le Monténégro sont
  complets en S6 et S7, Paphos Brown Hills en S8. La date du meilleur prix est donc dictée autant
  par la disponibilité que par le tarif.
- **26/08/2026 — mise en attente de quatre destinations.** Venise, Rome, Paphos Greek Village et
  Paris passent en `לפי בקשה`. Aucune n'avait de prix vérifiable au taux 3.05 : laisser leur ancien
  tarif en ligne revenait à vendre à un prix faux. Paris est le cas le plus net — la destination
  était vendable alors que son hôtel figure en liste d'exclusion cacherout.
