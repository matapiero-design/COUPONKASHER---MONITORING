# Prompt de la routine quotidienne — automatisation tarifs CouponKasher

Ce fichier documente le prompt envoyé chaque jour à 6h (heure d'Israël) par la Routine planifiée
(`create_trigger`, cron) qui automatise la vérification de prix jusqu'ici déclenchée manuellement
par Jacques (voir skill `dashboard-suivi-prix-sejours-casher`, section "Cadence").

C'est une session **fraîche** à chaque déclenchement (`create_new_session_on_fire=true`) : le
prompt ci-dessous doit donc être autoporté, sans dépendre du contexte d'une conversation
précédente.

## Prompt envoyé par la Routine

```
Tu es dans le repo matapiero-design/couponkasher---monitoring (déjà cloné dans cet environnement).
C'est le run quotidien automatisé de vérification des tarifs vols CouponKasher — Jacques ne le
déclenche plus manuellement, c'est toi qui l'exécutes chaque matin.

1. git checkout main && git pull origin main
2. Utilise le skill `dashboard-suivi-prix-sejours-casher` avec la portée par défaut :
   - Groupe A uniquement (9-10 destinations Tier 1, voir le skill pour la liste)
   - Vols directs uniquement (0 escale), départ dimanche par défaut (lundi si gap)
   - S1-S3 systématiquement tous les jours
   - S4-S8 uniquement si on est dimanche (heure d'Israël) au moment du run — sinon ignorer cette
     section et laisser les valeurs existantes dans Data/flight-prices.md inchangées
   - Le connecteur Kiwi.com est attaché à cette session dès le départ — s'il n'apparaît pas dans
     les outils disponibles, ne bascule PAS silencieusement sur une recherche web générique :
     note le problème dans le Journal des runs et arrête-toi (voir étape 5)
3. Applique toutes les règles du skill sans exception : jamais de vol à escale même moins cher,
   jamais de départ/retour un samedi, contrainte d'atterrissage vendredi (11h hiver / 14h été,
   bornes à vérifier chaque année), Cracovie et Milan en pause, Groupe B non traité ici.
4. Mets à jour Data/flight-prices.md :
   - Remplace le tableau "Groupe A (S1-S3)" avec les prix du jour
   - Remplace le tableau "Groupe A (S4-S8)" uniquement si c'est un run dominical
   - Ajoute une ligne au "Journal des runs" (date/heure UTC, destinations traitées, gaps/anomalies,
     statut connecteur) — ne jamais écraser les lignes précédentes de ce journal, garder les 30
     dernières
   - Mets à jour les champs "Dernière mise à jour", "Portée du dernier run", "Statut connecteur
     Kiwi.com" en haut du fichier
5. Commit avec un message clair (ex: "Prix vols TLV — run automatisé 2026-07-28") et
   git push origin main directement — pas de PR pour ce run quotidien de données.
   Si le connecteur Kiwi.com était indisponible ou qu'aucune donnée n'a pu être récupérée, ne
   commite rien : laisse le fichier inchangé et signale le problème en fin de réponse.
6. Termine par un résumé court : destinations traitées, gaps, anomalies de prix notables.
```

## Paramètres de la Routine

- **Cadence** : quotidienne, 6h heure d'Israël (`0 3 * * *` en UTC, IDT été / à réévaluer si le
  décalage change en hiver — Israël passe en IST/UTC+2 fin octobre)
- **Cible** : push direct sur `main` de ce repo, sans PR intermédiaire (validé par Jacques)
- **Session** : fraîche à chaque déclenchement (`trig_01AC9Z8TrgTpLToieNmSJ6G4`, créée le
  28/07/2026 via l'API `create_trigger`)

### ⚠️ Limitation connue : connecteur Kiwi.com non attaché

L'API `create_trigger` de cette organisation **refuse le paramètre `connectors`**
("the connectors parameter is not available for this organization") — impossible d'attacher
Kiwi.com par ce chemin. La session déclenchée chaque jour n'a donc **pas accès au connecteur
Kiwi.com** tant que ce point n'est pas résolu autrement.

Conséquence : le prompt ci-dessus contient déjà le garde-fou du skill (ne jamais basculer
silencieusement sur une recherche web générique si le connecteur manque) — la session notera donc
le problème dans le "Journal des runs" et n'écrira aucun prix plutôt que de produire une donnée non
fiable. Le trigger tourne donc "à vide" (sans effet indésirable) tant que le connecteur n'est pas
résolu.

**Chemin recommandé pour résoudre** : recréer cette Routine depuis l'UI claude.ai/routines
(plutôt que par l'API `create_trigger`), qui permet d'attacher explicitement le connecteur
Kiwi.com à la Routine — décision de Jacques le 28/07/2026. Une fois fait, désactiver ou supprimer
le trigger `trig_01AC9Z8TrgTpLToieNmSJ6G4` créé par l'API pour éviter un doublon.

## Historique des décisions

- 28/07/2026 : passage du déclenchement manuel (un message de Jacques chaque jour) à une Routine
  planifiée quotidienne, suite à la note du skill `dashboard-suivi-prix-sejours-casher` indiquant
  que l'automatisation serait réévaluée "après quelques jours d'usage réel".
- 28/07/2026 : découverte que l'API `create_trigger` ne permet pas d'attacher de connecteur
  (Kiwi.com) dans cette organisation. Jacques a choisi de garder le trigger API tel quel (il ne
  produit pas de fausse donnée en l'absence du connecteur) et de recréer la Routine depuis l'UI
  claude.ai/routines pour obtenir l'accès à Kiwi.com.
