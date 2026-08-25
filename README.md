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
