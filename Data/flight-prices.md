# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-09-15
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vol direct (0 escale) A/R 3 nuits, départ dimanche par défaut 20/09/2026 → retour mercredi 23/09/2026
- **Statut connecteur Kiwi.com** : OK — connecté, résultats reçus pour 6/7 destinations (TBS : aucun direct A/R trouvé pour cette semaine précise, voir anomalie ci-dessous)

## ⚠️ Anomalie majeure signalée ce run — collision avec Yom Kippour

Le dimanche par défaut de ce run (**20/09/2026**) est l'**erev Yom Kippour** (Yom Kippour 5787 tombe la
soirée du 20 au soir du 21 septembre 2026 ; Roch Hachana avait déjà eu lieu le 12-14/09). Le journal
des runs de ce même repo notait déjà le 26/08/2026 que « Kippour rend S4 inexploitable, dimanche comme
lundi » — cette même contrainte touche désormais S1 mécaniquement, simplement parce que le calendrier a
avancé. Deux conséquences observées ce run :

1. **Aucun vol direct TLV→TBS trouvé pour le 20/09** (0 résultat, 0 escale) alors que le retour direct
   TBS→TLV existe bien ce jour-là (dès 247 $, 5 options) et que l'aller direct réapparaît la semaine
   suivante (27/09, dès 398 $). C'est un vrai trou d'horaire ce dimanche précis, pas un problème de code
   IATA.
2. **Hausse de prix générale et anormalement forte sur les 6 destinations restantes** par rapport au run
   du 2026-08-25 (voir tableau de comparaison plus bas) — de +6 % (PFO) à +82 % (ATH). Une hausse liée à
   la demande de voyage autour des fêtes est plausible (billets vendus pour des dates encadrant Kippour/
   Souccot), mais l'ampleur mérite un contrôle humain avant toute utilisation commerciale de ces prix.

**Recommandation** : ne pas utiliser le point S1 (20/09) tel quel pour un devis client — la date tombe
sur une fête où CouponKasher ne vend historiquement pas de départ dominical. Un second point de repère
a été relevé sur le dimanche suivant (27/09→30/09, en pleine semaine de Souccot — hôtels probablement
tendus mais vols opérationnels) : les prix y sont encore plus élevés partout, ce qui confirme que la
poussée n'est pas un artefact du 20/09 seul mais bien liée à la période des fêtes de Tichri dans son
ensemble. À réévaluer une fois la période des fêtes passée (courant octobre).

## Prix vols directs — Groupe A (S1-S3)

Point par défaut de ce run : dimanche **20/09/2026** → mercredi **23/09/2026** (⚠️ erev Yom Kippour, voir
anomalie ci-dessus — à ne pas considérer comme un prix « normal »).

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 20/09/2026 | Dimanche | 579 | 2026-09-15 | ⚠️ +35 % vs run du 25/08 (430$→579$) — 15 options directes |
| Vienne | VIE | S1 | 20/09/2026 | Dimanche | 486 | 2026-09-15 | ⚠️ +34 % vs run du 25/08 (363$→486$) — 12 options directes |
| Rome (Fiumicino) | FCO | S1 | 20/09/2026 | Dimanche | 387 | 2026-09-15 | +8 % vs run du 25/08 (358$→387$) — 15 options directes |
| Paphos | PFO | S1 | 20/09/2026 | Dimanche | 186 | 2026-09-15 | +6 % vs run du 25/08 (176$→186$) — 15 options directes |
| Athènes | ATH | S1 | 20/09/2026 | Dimanche | 289 | 2026-09-15 | ⚠️ +82 % vs run du 25/08 (159$→289$) — 15 options directes |
| Budapest | BUD | S1 | 20/09/2026 | Dimanche | 418 | 2026-09-15 | ⚠️ +69 % vs run du 25/08 (248$→418$) — 15 options directes |
| Tbilissi | TBS | S1 | 20/09/2026 | Dimanche | **GAP** | 2026-09-15 | 🚫 Aucun direct TLV→TBS trouvé ce jour (0 résultat, 0 escale) ; retour TBS→TLV direct OK dès 247$. Voir anomalie Yom Kippour ci-dessus. |

### Point de repère supplémentaire (hors schéma standard) — dimanche suivant, 27/09→30/09/2026

Relevé à titre de comparaison pour isoler l'effet Kippour/Souccot du 20/09 ci-dessus. Semaine de Souccot
(hol hamoed) — vols a priori opérationnels, hôtels probablement tendus (non vérifiés ici, hors périmètre
de ce run vol-seul).

| Destination | Aéroport | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|
| Prague | PRG | 27/09/2026 | Dimanche | 766 | 2026-09-15 | ⚠️ +78 % vs run du 25/08 — 15 options directes |
| Vienne | VIE | 27/09/2026 | Dimanche | 567 | 2026-09-15 | ⚠️ +56 % vs run du 25/08 — 15 options directes |
| Rome (Fiumicino) | FCO | 27/09/2026 | Dimanche | 439 | 2026-09-15 | +23 % vs run du 25/08 — 15 options directes |
| Paphos | PFO | 27/09/2026 | Dimanche | 389 | 2026-09-15 | ⚠️ +121 % vs run du 25/08 — 15 options directes |
| Athènes | ATH | 27/09/2026 | Dimanche | 359 | 2026-09-15 | ⚠️ +126 % vs run du 25/08 — 15 options directes |
| Budapest | BUD | 27/09/2026 | Dimanche | 466 | 2026-09-15 | ⚠️ +88 % vs run du 25/08 — 15 options directes |
| Tbilissi | TBS | 27/09/2026 | Dimanche | **GAP** | 2026-09-15 | 🚫 Aucun direct A/R trouvé (aller direct existe seul, dès 398$ ; aucun retour direct TBS→TLV trouvé le 30/09) |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — en attente du premier run hebdomadaire)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-09-15 | PRG, VIE, FCO, PFO, ATH, BUD (6/7 avec prix) + TBS en gap sur les deux dimanches testés | **Anomalie majeure** : le dimanche par défaut (20/09) est l'erev Yom Kippour — TBS n'a aucun direct A/R ce jour précis (aller direct absent, retour direct présent dès 247$ ; l'aller direct réapparaît le 27/09 à 398$). Les 6 autres destinations affichent une hausse générale et forte vs le run du 25/08 : de +6% (PFO) à +82% (ATH) sur le point du 20/09, et encore plus haut sur le point de contrôle du 27/09 (semaine de Souccot) : de +23% (FCO) à +126% (ATH). TBS reste également en gap sur le 27/09→30/09 (aller direct existe seul, aucun retour direct TBS→TLV trouvé le 30/09). Hypothèse retenue : effet de demande lié à la période des fêtes de Tichri (Roch Hachana 12-14/09, Kippour 20-21/09, Souccot à partir du 25/09) plutôt qu'un problème de données — les deux points testés (Kippour et Souccot) montrent la même direction et une intensité croissante. Recommandation : ne pas utiliser ces prix pour un devis client tel quel, et refaire un point de contrôle une fois la période des fêtes passée (courant octobre) pour confirmer le retour à la normale. Aucun écart structurel de type « une seule option / aéroport erroné » n'a été observé sur PRG/VIE/FCO/PFO/ATH/BUD (12 à 15 options directes trouvées à chaque fois) — la hausse touche donc le marché dans son ensemble, pas une destination isolée. | OK (Kiwi.com — connecté, réponses reçues sur toutes les requêtes ; quelques erreurs transitoires de proxy retentées avec succès) |
| 2026-08-25 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7) | Baisse de prix marquée et généralisée sur les 7 destinations vs le run du 2026-08-20 (de -27% pour TBS à -75% pour PRG). Explication la plus probable : date de départ testée plus éloignée (30/08 contre 23/08 lors du run précédent, soit 5 jours d'avance au lieu de 3) → sortie des tarifs de dernière minute les plus chers et ouverture de classes tarifaires moins chères, avec beaucoup plus d'options directes disponibles (PRG : 15 options directes ce run contre 1 seule le run précédent ; VIE : 15 contre 8). Ceci résout les deux anomalies notées le run précédent (PRG à 1723$ sur une seule option, VIE à 1284$) — elles semblent avoir été un effet de dernière minute plutôt qu'un problème de données. TBS reste l'exception avec seulement 4 options directes trouvées (contre 15 pour les autres destinations) et le prix le plus élevé du groupe (587$) — cohérent avec une offre directe TLV-TBS structurellement plus restreinte (Israir + El Al uniquement), pas une anomalie de données. À confirmer sur les prochains runs quotidiens pour distinguer volatilité de dernière minute vs tendance de fond. | OK |
| 2026-08-20 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (7/7, run initial) | PRG : une seule option directe (Smartwings aller / El Al retour) à 1723$, ~3x le prix des autres destinations du groupe (cluster ATH/FCO/BUD/PFO entre 364$ et 566$) — à surveiller les prochains jours pour confirmer si c'est structurel (peu de compagnies low-cost sur TLV-PRG direct) ou une anomalie ponctuelle. VIE également élevé (1284$, 8 options) mais cohérent avec l'absence de low-cost direct sur cette route — pas d'anomalie de données identifiée. Pas d'historique antérieur disponible pour comparaison (premier run avec données réelles). | OK |
