# Prompt de la routine de nettoyage — boîte matapiero@gmail.com

Ce fichier documente le prompt destiné à la Routine planifiée qui désencombre la boîte de
réception de Jacques. Même construction que `ROUTINE_PROMPT.md` (tarifs) : une session
**fraîche** à chaque déclenchement, donc un prompt autoporté.

## Le principe : trier ≠ supprimer

C'est la transposition, côté email, du `calculer ≠ publier` du pipeline tarifs.

| Étage | Effet | Réversible |
|---|---|---|
| **Archiver** | le thread sort de la boîte de réception, reste cherchable | oui, à tout moment |
| **Corbeille** | le thread part à la corbeille Gmail | oui, 30 jours |

Un email ne va jamais à la corbeille sans être passé par l'archivage **ou** sans avoir plus de
90 jours. Rien n'est jamais supprimé définitivement : la routine n'a pas le droit de vider la
corbeille, et ne le fera jamais.

Le défaut, pour toute adresse absente de `pipeline/email_rules.json`, est de **ne rien faire**.
Une boîte qui grossit est un problème moins grave qu'un email client détruit.

## Prompt envoyé par la Routine

```text
Tu es dans le repo matapiero-design/couponkasher---monitoring (déjà cloné dans cet
environnement). C'est le run de nettoyage de la boîte matapiero@gmail.com. Jacques ne le
déclenche pas à la main : tu l'exécutes seul, et personne ne relit avant que tu agisses.
Tiens-t'en strictement aux règles du repo.

1. git checkout main && git pull origin main
2. Vérifie que le connecteur Gmail est dans tes outils. S'il manque, n'essaie AUCUN
   contournement : note-le en fin de réponse, ne commite rien, arrête-toi là.
3. Lis pipeline/email_rules.json. C'est la seule source de vérité : n'invente jamais une
   adresse, une règle ou un délai qui n'y figure pas.
4. Génère les requêtes avec : python3 pipeline/email_cleanup.py --requetes
   Exécute-les TELLES QUELLES via search_threads. Ne les retouche pas à la main : les
   clauses de protection (-is:starred, -has:userlabels, -in:sent, -has:attachment) sont
   ce qui empêche de toucher une conversation client ou un billet.
5. Pour chaque thread remonté, note id, expéditeur, date et sujet, et écris le relevé dans
   Data/email-runs/run-<date>.json (même format que run-2026-08-26.json). Respecte le
   plafond de parametres.plafond_threads_par_run : au-delà, garde les plus anciens et
   laisse le reste au run suivant. Le plafond de rattrapage ne s'utilise QUE si Jacques
   l'a explicitement demandé dans le message qui déclenche ce run.
6. Fais valider le relevé : python3 pipeline/email_cleanup.py Data/email-runs/run-<date>.json
   Le script écarte les threads protégés et signale les anomalies. S'il sort en erreur, ou
   s'il liste une anomalie, N'APPLIQUE RIEN — commite le rapport et signale-le, c'est tout.
7. Seulement si l'étape 6 est propre, applique, en te limitant aux threads que le script a
   classés "traites" dans Data/email-cleanup.json — jamais aux "ecartes" :
   - étage archive   -> unlabel_thread du label INBOX
   - étage corbeille -> trash_thread
   Ne marque jamais rien comme lu au passage : le compteur de non-lus est à Jacques.
   Ne touche jamais à SPAM ni à la corbeille existante.
8. Commit ("Nettoyage emails — run 2026-XX-XX") et git push origin main. Pas de PR.
9. Termine par un résumé court : threads archivés, threads en corbeille, threads écartés par
   les protections et pourquoi, et ce qui reste en attente à cause du plafond.

Règles absolues, dans cet ordre de priorité :
- En cas de doute sur un thread, tu ne le touches pas. Le doute se résout toujours en
  faveur de la conservation.
- Tu ne vides jamais la corbeille et ne supprimes jamais définitivement.
- Tu ne modifies jamais pipeline/email_rules.json de ta propre initiative. Si tu repères un
  expéditeur qui mériterait d'entrer dans une règle, tu le PROPOSES dans ton résumé, en
  laissant le fichier intact. Ajouter une adresse est une décision de Jacques.
- Tu ne te désabonnes de rien, tu ne réponds à rien, tu n'envoies aucun email.
```

## Paramètres de la Routine

- **Cadence proposée** : quotidienne, 5h heure d'Israël (`0 2 * * *` en UTC, IDT été — même
  réserve d'hiver que la routine tarifs, Israël passant en UTC+2 fin octobre). Une heure avant
  le run tarifs, pour que les deux ne se marchent pas dessus sur le même repo.
- **Cible** : push direct sur `main`, sans PR (même convention que le run tarifs).
- **Session** : fraîche à chaque déclenchement (`create_new_session_on_fire=true`).
- **Statut au 26/08/2026** : **la Routine n'est pas créée.** Le run à blanc est livré et attend
  la validation de Jacques (voir ci-dessous). Créer le trigger avant cette validation ferait
  partir des emails à la corbeille sans que personne ait relu les règles.

### Blocage connu : le connecteur Gmail doit être attaché depuis l'UI

Le même mur que pour Kiwi.com et Booking.com (voir `ROUTINE_PROMPT.md`) : l'API
`create_trigger` de cette organisation refuse le paramètre `connectors`. Une Routine créée par
l'API n'aura **aucun accès à Gmail**, et l'étape 2 du prompt l'arrêtera net — sans dégât, mais
sans effet.

**Chemin pour résoudre** : créer cette Routine depuis l'UI claude.ai/routines, qui permet
d'attacher explicitement le connecteur **Gmail** à la Routine.

## Ce que le run à blanc du 26/08/2026 a appris

- **Le volume réel est inconnu, et il est grand.** L'API Gmail cesse de compter à 200 threads :
  cinq des huit requêtes butent sur ce plafond. Kayak seul dépasse 200 threads, les trois
  adresses El Al aussi, le Beis Medrash de la Mir aussi. Sur une boîte de 24 183 messages, un
  plafond de 200 par run veut dire plusieurs dizaines de runs avant d'avoir résorbé
  l'historique. C'est lent par construction, et c'est le prix de la réversibilité.
- **Le filtre par mots-clés se déclenche surtout à tort, et c'est voulu.** 32 threads sont
  écartés par les mots-clés « billet / réservation / paiement », et à la lecture ce sont tous
  des publicités El Al contenant כרטיס טיסה, plus un jeu-concours Rolex contenant « ticket ».
  Aucun vrai transactionnel n'a fuité dans une règle marketing. Le filtre se trompe donc dans
  le sens sûr : il conserve de la pub, il ne détruit pas une facture.
- **Sur l'historique, les deux étages se confondent.** Un email marketing de 2025 franchit
  d'un coup les 30 et les 90 jours : il part directement à la corbeille sans jamais avoir été
  archivé. La séquence archive-puis-corbeille ne se voit vraiment que sur le flux à venir.

## Historique des décisions

- **26/08/2026 — création du nettoyage automatique.** Cadre posé par Jacques : archiver à
  30 jours, corbeille à 90 jours, jamais de suppression définitive.
- **26/08/2026 — Tehilim Yahad et Beis Medrash de la Mir : archive seulement.** Ces deux listes
  sortent de la boîte de réception mais ne partent jamais à la corbeille.
- **26/08/2026 — GoKosher classé en veille, pas en marketing.** C'est de la promo, mais d'un
  concurrent direct sur le séjour casher : archivé pour désencombrer, jamais détruit, pour
  rester consultable au moment de fixer une grille.
- **26/08/2026 — premier passage à blanc.** Décidé par Jacques : le pipeline est livré et
  mesuré avant que le moindre email ne bouge.
