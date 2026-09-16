# CouponKasher — règles qui ne se devinent pas

Lu automatiquement au démarrage de chaque session. Ne contient que ce qui a déjà
causé une erreur réelle. Le détail du projet est dans `README.md`.

## 1. Le taux est 3,05 — et il y a DEUX formules

```
étranger   prix_ils = floor( (vol_usd + hôtel_$_par_pers) / 0.85 * 3.05 / 10 ) * 10
Israël     prix_ils = floor( (hôtel_ILS_par_pers)         / 0.85        / 10 ) * 10
```

**Ne jamais appliquer le taux à un prix déjà libellé en shekels** : cela le
multiplie par trois. C'est le piège principal de l'offre domestique, et il est
documenté dans `prix_package_ils()`.

Le prix hôtel de Booking est le **total pour 2 personnes** : diviser par 2 avant
d'entrer dans la formule.

La source qui fait foi est `TAUX_USD_ILS` dans `pipeline/pricing.py`. **Lire le
code, pas la documentation.**

Le skill `dashboard-suivi-prix-sejours-casher` a indiqué `3.65` jusqu'au
16/09/2026. Ce taux est périmé depuis le 25/08/2026. Un prix calculé à 3,65 est
**20 % trop cher** — et reste plausible, donc l'erreur ne se voit pas.

## 2. Calculer n'est pas publier

| | Où | Qui écrit |
|---|---|---|
| Calculer | `Data/` | le run, automatiquement |
| Publier | `site/` | Jacques seul, sur demande explicite |

Un run n'écrit **jamais** dans `site/`. Modifier `site/prices.json` change le
prix payé par un client : c'est une décision commerciale, jamais un effet de bord.

Le seuil d'écart de 15 % est une **alerte à signaler**, pas un blocage
(décision du 26/08/2026).

## 3. Déployer, c'est deux fichiers

`site/index.html` **et** `site/prices.json`, toujours ensemble.

Le glisser-déposer Netlify remplace tout le site par ce qu'on y dépose. Déposer
`index.html` seul supprime `prices.json` du serveur : le `fetch` échoue, la page
retombe sur les prix écrits en dur dans le HTML, et le site affiche des tarifs
périmés en ayant l'air parfaitement normal.

Ces valeurs de repli datent du taux 3,65 et **quatre d'entre elles remettent en
vente des destinations retirées** (Paris, Venise, Rome, Greek Village). Paris est
le cas le plus grave : son hôtel figure en liste d'exclusion cacherout.

## 4. Le dépôt fait foi, toujours

Un fichier reçu par un autre canal — session de chat, pièce jointe, export —
peut ignorer des décisions prises ici. C'est arrivé le 16/09/2026 : une version
datée du 20/08 aurait remis en ligne les tarifs au taux 3,65.

Ne jamais déployer un fichier qui ne vient pas du dépôt. Pour intégrer un
travail externe, en extraire l'apport et le porter ici — pas l'inverse.

## 5. Pièges de `site/index.html`

Fichier de 2,3 Mo, photos en base64, modifié par manipulation de texte. Avant de
pousser, vérifier :

- **Carrousel** : le nombre de `.slide` doit égaler le nombre de pastilles
  `goTo(n)`. Sinon `dots[cur]` vaut `undefined` et l'auto-rotation se bloque.
  Le carrousel est la vitrine, pas le catalogue.
- **Cartes destination** : elles vont dans la grille `#grid-tier1`, pas dans le
  carrousel. Une variante d'hôtel garde le nom de la ville en titre, c'est
  l'hôtel qui la distingue (modèle `לונדון - Pillar`).
- **Visibilité** : `#grid-tier1 > div:nth-child(n+13)` est masqué derrière le
  bouton « afficher plus ». Ajouter une carte sans ajuster ce seuil la cache.
- **Champs de fiche** : `hotel`, `rooms`, `facilities`, `includes` sont rendus en
  `innerHTML` (ils portent des pictogrammes SVG) ; `location` reste en
  `textContent`. Mettre du balisage dans `location` l'afficherait en clair.
- **Clés** : chaque `data-price-city` doit correspondre à une clé de
  `prices.json`, au caractère près. Sinon la carte reste à ₪0.

## 6. Vérifier avant de pousser

Deux bugs ont atteint la production en septembre 2026, tous deux détectables
mécaniquement. Avant tout push touchant `site/` :

1. `<div>` ouvrants = `<div>` fermants
2. chaque bloc `<script>` passe `node --check`
3. `.slide` = pastilles `goTo`
4. chaque `data-price-city` existe dans `prices.json`
5. aucun balisage dans un champ rendu en `textContent`

Le rendu visuel se vérifie en servant `site/` en HTTP (`python3 -m http.server`)
puis en chargeant la page. **Ouvrir le fichier en `file://` affiche toujours les
prix périmés** : le navigateur y bloque la lecture de `prices.json`.

## 7. Contraintes métier à ne jamais contourner

- Vols **directs uniquement**. Un vol avec escale n'est pas vendable, même moins cher.
- **Jamais de samedi**, ni au départ ni au retour.
- Vendredi : atterrissage avant 11 h en hiver, 14 h en été.
- Un hôtel dont la cacherout n'est pas tranchée ne se vend pas, quel que soit
  l'écart de prix. En attente, la carte affiche `לפי בקשה`.
