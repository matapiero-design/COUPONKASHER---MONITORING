# Prompt de la routine quotidienne — automatisation tarifs CouponKasher

Ce fichier documente le prompt envoyé chaque jour à 6h (heure d'Israël) par la Routine planifiée
qui automatise la vérification de prix jusqu'ici déclenchée manuellement par Jacques
(voir skill `dashboard-suivi-prix-sejours-casher`, section "Cadence").

C'est une session **fraîche** à chaque déclenchement (`create_new_session_on_fire=true`) : le
prompt ci-dessous doit donc être autoporté, sans dépendre du contexte d'une conversation
précédente.

Depuis le 25/08/2026, le run ne se limite plus au vol : il produit un **prix package complet
vol + hôtel**, l'hôtel étant désormais vérifiable par nom exact via le connecteur Booking.com.

## Prompt envoyé par la Routine

```text
Tu es dans le repo matapiero-design/couponkasher---monitoring (déjà cloné dans cet environnement).
C'est le run quotidien automatisé des tarifs CouponKasher — Jacques ne le déclenche plus
manuellement, c'est toi qui l'exécutes chaque matin.

1. git checkout main && git pull origin main
2. Vérifie que les DEUX connecteurs sont disponibles dans tes outils : Kiwi.com (vol) et
   Booking.com (hôtel). S'il en manque un, ne bascule PAS sur une recherche web générique :
   note le problème dans le Journal des runs et arrête-toi (voir étape 7).
3. Applique le skill dashboard-suivi-prix-sejours-casher avec la portée par défaut :
   - Groupe A uniquement — la liste fait foi dans pipeline/destinations.json de ce repo
   - Schéma de séjour : 3 nuits / 4 jours, départ dimanche → retour mercredi.
     Pas de vol direct le dimanche → repli lundi → jeudi, et l'hôtel doit être ré-interrogé
     sur les dates décalées (jamais un hôtel sur des dates différentes du vol).
   - S1-S3 systématiquement tous les jours ; S4-S8 uniquement si on est dimanche
   - Vol : Kiwi.com, TLV → destination, 1 adulte, USD, max_sector_stopovers=0 (0 escale strict)
   - Hôtel : Booking.com, hotel_names = le nom exact de pipeline/destinations.json + destination
     = la ville de contexte, 2 adultes, 1 chambre, 3 nuits, USD. Le prix retourné est le TOTAL
     du séjour pour 2 adultes : le prix par personne, c'est ce total ÷ 2.
     Si le nom d'hôtel retourné par Booking ne correspond pas au partenaire attendu, ne
     l'utilise pas comme prix vendable — marque la ligne "à confirmer".
4. Applique toutes les règles du skill sans exception : jamais de vol à escale même moins cher,
   jamais de départ/retour un samedi, contrainte d'atterrissage vendredi (11h hiver / 14h été,
   bornes à vérifier chaque année), Cracovie et Milan en pause, Groupe B non traité ici.
5. Écris le run brut dans Data/runs/run-<date>.json (même format que les runs précédents), puis
   lance : python3 pipeline/pricing.py Data/runs/run-<date>.json
   Ce script calcule le prix package, régénère Data/package-prices.md et Data/package-prices.json,
   et signale les écarts > 15 % vs les prix actuellement publiés.
6. Mets aussi à jour Data/flight-prices.md (tableaux vol + Journal des runs, 30 dernières lignes).
7. Commit avec un message clair (ex: "Prix package — run automatisé 2026-08-28") et
   git push origin main directement — pas de PR pour ce run quotidien de données.
   Si un connecteur était indisponible ou qu'aucune donnée n'a pu être récupérée, ne commite
   rien : laisse les fichiers inchangés et signale le problème en fin de réponse.
8. NE TOUCHE JAMAIS à site/prices.json ni à site/index.html. Publier un prix sur
   couponkasher.co.il est une décision de Jacques, pas un effet de bord du run.
9. Termine par un résumé court : destinations traitées, gaps, écarts > 15 % à confirmer.
```

## Paramètres de la Routine

- **Cadence** : quotidienne, 6h heure d'Israël (`0 3 * * *` en UTC, IDT été / à réévaluer si le
  décalage change en hiver — Israël passe en IST/UTC+2 fin octobre)
- **Cible** : push direct sur `main` de ce repo, sans PR intermédiaire (validé par Jacques)
- **Session** : fraîche à chaque déclenchement (`trig_01AC9Z8TrgTpLToieNmSJ6G4`, créée le
  28/07/2026 via l'API `create_trigger`)

### Blocage connu : connecteurs non attachés à la Routine

L'API `create_trigger` de cette organisation **refuse le paramètre `connectors`**
("the connectors parameter is not available for this organization") — impossible d'attacher
Kiwi.com ni Booking.com par ce chemin. La session déclenchée chaque jour n'a donc **accès à
aucun des deux connecteurs** tant que ce point n'est pas résolu.

Conséquence : le prompt ci-dessus contient le garde-fou (ne jamais basculer silencieusement sur
une recherche web générique si un connecteur manque) — la session note le problème dans le
Journal des runs et n'écrit aucun prix plutôt que de produire une donnée non fiable. Le trigger
tourne donc "à vide" (sans effet indésirable) tant que les connecteurs ne sont pas résolus.

**Chemin pour résoudre** : recréer cette Routine depuis l'UI claude.ai/routines (plutôt que par
l'API `create_trigger`), qui permet d'attacher explicitement les connecteurs à la Routine — en
attachant cette fois **Kiwi.com ET Booking.com**. Une fois fait, désactiver ou supprimer le
trigger `trig_01AC9Z8TrgTpLToieNmSJ6G4` créé par l'API pour éviter un doublon.

## Historique des décisions

- 28/07/2026 : passage du déclenchement manuel (un message de Jacques chaque jour) à une Routine
  planifiée quotidienne, suite à la note du skill `dashboard-suivi-prix-sejours-casher` indiquant
  que l'automatisation serait réévaluée "après quelques jours d'usage réel".
- 28/07/2026 : découverte que l'API `create_trigger` ne permet pas d'attacher de connecteur
  (Kiwi.com) dans cette organisation. Jacques a choisi de garder le trigger API tel quel (il ne
  produit pas de fausse donnée en l'absence du connecteur) et de recréer la Routine depuis l'UI
  claude.ai/routines pour obtenir l'accès à Kiwi.com.
- 25/08/2026 : le run passe du **prix vol seul** au **prix package vol + hôtel**. Le connecteur
  Booking.com accepte une recherche par `hotel_names` (nom d'hôtel exact) — c'est précisément ce
  qui manquait à lastminute.com et qui bloquait la vérification hôtelière depuis le 8 juillet.
  Validé de bout en bout sur 8 destinations du Groupe A le 25/08 (voir `Data/runs/run-2026-08-25.json`).
- 25/08/2026 : séparation stricte entre **calculer** (le run, dans `Data/`) et **publier** (le site,
  dans `site/`). Le run ne publie jamais : il signale les écarts > 15 % et Jacques tranche.
