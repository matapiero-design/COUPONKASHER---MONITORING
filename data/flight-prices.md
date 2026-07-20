# Prix vols TLV → destinations — suivi quotidien

Méthode : vols directs uniquement (0 escale), aller-retour, 3 nuits, connecteur Kiwi.com, prix en USD (moins cher trouvé, taxes incluses).
Format : Prix ($) (Compagnie aller/retour). Dimanche (dim) = départ par défaut.
Destinations suivies : PRG, VIE, FCO, PFO, ATH, BUD, TBS (au départ de TLV).

## Note technique (20/07/2026)

Le fichier `data/flight-prices.md` n'existait pas dans le repo au moment de cette exécution :
- Le 17/07/2026, un premier essai de création a écrit le tableau de données dans le **message de commit** au lieu du contenu du fichier (`c916991`) — le fichier réel est resté vide.
- Un second essai a créé un fichier dont le **nom** contenait le texte destiné au contenu (`Data/flight-prices.md# Prix vols TLV Fichier a completer...`), toujours sans données exploitables.
- Les deux fichiers erronés ont été supprimés et ce fichier est recréé au bon emplacement (`data/` en minuscule) avec un historique de référence reconstruit depuis les logs git, suivi de la première ligne de données réellement vérifiées.

## Historique de référence — capture du 17/07/2026 (non vérifiée, reconstruite depuis un message de commit, jamais réellement sauvegardée)

| O&D | S1 (19-22/07) | S2 (26-29/07) | S3 (02-05/08) | S4 (09-12/08) | S5 (16-19/08) | S6 (23-26/08) | S7 (30/08-02/09) | S8 (06-09/09) |
|---|---|---|---|---|---|---|---|---|
| PRG dim | 365 (TUS Airways/Arkia) | — | 614 (Arkia) | 759 (Smartwings/TUS Airways) | 1001 (Smartwings/TUS Airways) | 832 (Arkia) | 562 (Smartwings/TUS Airways) | 463 (TUS Airways/Smartwings) |
| VIE dim | 395 (Blue Bird) | — | 772 (Blue Bird) | 901 (Blue Bird/Arkia) | 866 (Blue Bird/Arkia) | 900 (El Al/Blue Bird) | 540 (Blue Bird/Arkia) | 537 (n/d) |
| FCO dim | 382 (Israir/Wizz Air Malta) | 929 (Arkia/Wizz Air Malta) | 575 (Israir/Wizz Air Malta) | 392 (Wizz Air Malta) | 511 (Wizz Air Malta) | 444 (Wizz Air Malta) | 229 (Wizz Air Malta) | 157 (n/d) |
| PFO dim | 119 (Israir) | 287 (Israir) | 292 (H1/TUS Airways) | 299 (TUS Airways) | 385 (TUS Airways) | 584 (El Al/TUS Airways) | 127 (Israir/Arkia) | 179 (n/d) |
| ATH dim | 119 (Israir) | 218 (Arkia/Israir) | 346 (Arkia/Israir) | 437 (Israir/Arkia) | 535 (Israir/Arkia) | 435 (Aegean/Wizz Air Malta) | 217 (Israir) | 170 (n/d) |
| BUD dim | 305 (Blue Bird/Israir) | 639 (Arkia/Israir) | 689 (Arkia/Wizz Air) | 474 (Wizz Air/Blue Bird) | 546 (Wizz Air) | 578 (Wizz Air) | 298 (Wizz Air) | 295 (n/d) |
| TBS dim | hors périmètre | hors périmètre | hors périmètre | 745 (n/d) | 892 (Arkia) | 828 (Arkia/Israir) | 384 (Israir) | 376 (n/d) |

Notes de l'époque : (n/d) = compagnie non capturée à l'origine ; S2 (26-29/07) = semaine "choc" post-Ticha BeAv, prix doublés ou données manquantes sur plusieurs O&D ; S7-S8 = chute post-saison confirmée.

## Suivi vérifié — S2 (26-29/07/2026), vérifié le 20/07/2026 via Kiwi.com

| O&D | Prix ($) | Compagnie A/R | vs référence 17/07 | Remarque |
|---|---|---|---|---|
| PRG dim | — | — | — | Aucun vol direct le dimanche 26/07 cette semaine. Direct dispo ven 24/07 (423$, TUS Airways) ou jeu 30/07 (423$, TUS Airways). |
| VIE dim | — | — | — | Aucun vol direct le dimanche 26/07 cette semaine. Direct dispo ven 24/07 (422$, Blue Bird) ou jeu 30/07 (422$, Blue Bird). |
| FCO dim | 917 | Wizz Air Malta A/R | 929 → 917 (-1%) | Confirme la semaine "choc" post-Ticha BeAv déjà signalée. |
| PFO dim | 299 | Israir A/R | 287 → 299 (+4%) | Stable. |
| ATH dim | 270 | Israir / Wizz Air Malta | 218 → 270 (+24%) | Hausse notable, cf. anomalies ci-dessous. |
| BUD dim | 526 | Blue Bird / Wizz Air | 639 → 526 (-18%) | Baisse notable, cf. anomalies ci-dessous. |
| TBS dim | 757 | Israir / El Al | hors périmètre à l'époque | Première donnée vérifiée pour TBS sur cette semaine. |

## Anomalies détectées (20/07/2026)

1. **PRG et VIE : aucun vol direct le dimanche 26/07.** Cohérent avec le trou déjà noté dans l'historique de référence pour S2 (les deux étaient à "—"). Des vols directs existent cette semaine-là mais uniquement vendredi 24/07 ou jeudi 30/07 — à surveiller si le départ dominical redevient disponible la semaine prochaine.
2. **ATH dim : +24%** par rapport à la dernière capture de référence pour la même semaine (218$ → 270$). Écart notable mais plausible dans une semaine déjà signalée comme perturbée (post-Ticha BeAv) ; à confirmer avec le suivi de demain.
3. **BUD dim : -18%** par rapport à la dernière capture (639$ → 526$), soit la baisse la plus marquée de cette vérification — bonne opportunité de marge à signaler si elle se confirme.
4. **Intégrité des données :** le fichier de suivi n'a jamais réellement contenu de données avant aujourd'hui (voir Note technique ci-dessus) — les 8 semaines S1-S8 de l'historique de référence sont donc non vérifiées et ne doivent pas être traitées comme fiables à 100%, seulement comme point de repère indicatif.

## Journal des mises à jour

- **20/07/2026** — Reconstruction du fichier + première vérification réelle (S2, 26-29/07) pour PRG, VIE, FCO, PFO, ATH, BUD, TBS via Kiwi.com.
