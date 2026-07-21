# Prix vols TLV → destinations

Méthode : vols directs uniquement (0 escale), aller-retour, 3 nuits, connecteur Kiwi.com, prix en USD (1 adulte, classe éco, prix le plus bas trouvé).
Destinations suivies : PRG, VIE, FCO, PFO, ATH, BUD, TBS — départ TLV, dimanche par défaut.

## Note sur l'historique

Le fichier précédent avait été supprimé puis recréé avec un nom corrompu (le contenu s'était retrouvé dans le nom de fichier au lieu du corps du fichier). La grille de prix "S1 à S8" qui apparaissait dans un message de commit du 17/07/2026 n'a jamais existé dans le contenu réel du fichier (diff = 0 ligne) : elle ne peut donc pas être considérée comme une donnée vérifiée. L'historique ci-dessous repart sur des bases saines à partir du 21/07/2026, avec uniquement des prix réellement obtenus via le connecteur Kiwi.com.

## Suivi quotidien

| Date vérif. | Destination | Départ (dim.) | Retour | Prix (USD) | Compagnies (aller/retour) | Vol direct |
|---|---|---|---|---|---|---|
| 2026-07-21 | ATH | 2026-07-26 | 2026-07-29 | 246 | BZ (Blue Bird) / 6H (Israir) | Oui |
| 2026-07-21 | PFO | 2026-07-26 | 2026-07-29 | 288 | 6H (Israir) / 6H (Israir) | Oui |
| 2026-07-21 | BUD | 2026-07-26 | 2026-07-29 | 489 | IZ (Arkia) / W6 (Wizz Air) | Oui |
| 2026-07-21 | TBS | 2026-07-26 | 2026-07-30* | 665 | 6H (Israir) / LY (El Al) | Oui |
| 2026-07-21 | FCO | 2026-07-26 | 2026-07-29 | 956 | IZ (Arkia) / W4 (Wizz Air Malta) | Oui |
| 2026-07-21 | VIE | — | — | n/d | — | **Aucun vol direct AR disponible pour dim. 26/07 → mer. 29/07** |
| 2026-07-21 | PRG | — | — | n/d | — | **Aucun vol direct AR disponible pour dim. 26/07 → mer. 29/07** |
| 2026-07-21 | VIE (réf., dim. suivant) | 2026-08-02 | 2026-08-05 | 666 | BZ (Blue Bird) / BZ (Blue Bird) | Oui |
| 2026-07-21 | PRG (réf., dim. suivant) | 2026-08-02 | 2026-08-05 | 670 | IZ (Arkia) / IZ (Arkia) | Oui |

*TBS : vol aller de nuit (départ 26/07 21h30, arrivée 27/07 01h05 heure locale) ; 3 nuits sur place, retour le matin du 30/07.

## Anomalies détectées

1. **PRG et VIE : pas de vol direct AR pour le dimanche 26/07 → mercredi 29/07.** Le connecteur Kiwi.com renvoie 0 résultat en aller-retour direct strict pour ces deux destinations sur cette semaine précise, alors que des vols directs à l'aller existent bien sur d'autres jours (lun-sam) et que le direct AR redevient disponible dès le dimanche suivant (02/08 → 05/08, à 670 $ et 666 $ respectivement). Cela ressemble à un trou ponctuel dans le planning des compagnies (Arkia sur PRG, Blue Bird sur VIE) plutôt qu'à une absence de route. À surveiller : si le trou persiste plusieurs dimanches de suite, cela indique un changement durable de fréquence plutôt qu'un aléa.
2. **FCO à 956 $** est nettement plus cher que les autres destinations testées cette semaine (246–665 $ pour ATH/PFO/BUD/TBS). Les seules options directes AR trouvées combinent Arkia (IZ335, un seul vol/jour) avec Wizz Air Malta ou ITA Airways sur le retour — peu d'offre = prix élevé. À revérifier les prochains jours pour voir si c'est une anomalie ponctuelle ou le niveau de prix normal de cette route en pleine saison.
3. **Historique antérieur non fiable** : les prix "S1 à S8" mentionnés dans un commit du 17/07/2026 n'ont jamais été écrits dans le fichier réel (voir note ci-dessus) — ne pas les utiliser comme référence de comparaison.
