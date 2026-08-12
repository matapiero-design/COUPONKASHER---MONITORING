# Prix vols TLV — CouponKasher

Fichier complété automatiquement par la routine quotidienne (voir `ROUTINE_PROMPT.md`).
Ne pas éditer manuellement — toute édition manuelle sera écrasée au prochain run.

- **Dernière mise à jour** : 2026-08-12 03:34 UTC
- **Portée du dernier run** : 7 destinations (PRG, VIE, FCO, PFO, ATH, BUD, TBS), vols directs
  (0 escale) aller-retour 3 nuits, au départ de TLV, départ dimanche par défaut — S1 uniquement
  (portée définie par le prompt reçu — pas de S2-S3 ni S4-S8 dans ce run)
- **Statut connecteur Kiwi.com** : ✅ Disponible et fonctionnel (4e run consécutif confirmé sur ce
  périmètre) — la limitation documentée plus bas pour le trigger créé via l'API `create_trigger`
  ne s'est pas manifestée sur ce run.

⚠️ **Historique reconstitué le 2026-08-12** : les runs précédents (28/07 → 11/08/2026) avaient
chacun été committés sur une branche `claude/eager-hawking-*` isolée qui n'a jamais été fusionnée
sur `main` — `main` ne contenait donc que le fichier vide initial malgré ~15 runs quotidiens
réellement exécutés. L'historique ci-dessous a été reconstitué à partir de ces branches orphelines
pour ne pas perdre le suivi. **Point à signaler à Jacques** : tant que le mécanisme de session qui
déclenche cette routine pousse vers une branche par run (jamais mergée) plutôt que directement sur
`main` (comme documenté dans `ROUTINE_PROMPT.md`), ce risque de perte d'historique se reproduira
à chaque run futur.

## Prix vols directs — Groupe A (S1-S3)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| Prague | PRG | S1 | 17/08/2026 → 20/08/2026 | Lundi (gap dimanche, 2e run consécutif) | 706 | 2026-08-12 | ⚠️ Aucun vol direct dimanche 16/08 pour la 2e journée d'affilée — décalé lundi. Prix en baisse vs hier (843→706 $) mais toujours ~1.3-1.8x le reste du groupe |
| Vienne | VIE | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 625 | 2026-08-12 | OK |
| Rome | FCO | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 394 | 2026-08-12 | OK |
| Paphos | PFO | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 396 | 2026-08-12 | OK |
| Athènes | ATH | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 508 | 2026-08-12 | OK |
| Budapest | BUD | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 527 | 2026-08-12 | OK |
| Tbilissi | TBS | S1 | 16/08/2026 → 19/08/2026 | Dimanche | 843 | 2026-08-12 | ⚠️ +14.8% vs hier (734→843 $), 2e destination la plus chère du groupe — capacité directe limitée (1 vol/jour Arkia/Israir), tendance à la hausse à surveiller |

## Prix vols directs — Groupe A (S4-S8, run hebdomadaire dimanche)

| Destination | Aéroport | Semaine | Date départ | Jour | Prix A/R ($) | Vérifié le | Statut |
|---|---|---|---|---|---|---|---|
| _(aucune donnée — S4-S8 non couvert : run du 2026-08-12 n'est pas un dimanche, et hors de la portée du prompt reçu)_ | | | | | | | |

## Journal des runs

| Date/heure (UTC) | Destinations traitées | Gaps / anomalies | Statut connecteur |
|---|---|---|---|
| 2026-07-28 03:35 | PRG, VIE, FCO, PFO, ATH, BUD, TBS — S1-S3 (7 dest. × 3 sem. = 21 recherches, 21/21 réussies) | Aucun gap (vol direct trouvé dimanche pour toutes les combinaisons). PRG augmente fortement avec l'éloignement (625→927→951$, +52%) — à surveiller, pas de comparaison historique possible (premier run). TBS ne figure pas dans la liste Groupe A/B de référence du skill `dashboard-suivi-prix-sejours-casher` — à confirmer avec Jacques si nouvelle destination active. Portée limitée aux 7 destinations demandées (hors AMS, LHR, CDG du Groupe A standard). | Opérationnel |
| 2026-07-29 (run manuel, hors cron) | PRG, VIE, FCO, PFO, ATH, BUD, TBS — 7/7 vols directs A/R 3 nuits trouvés, départ dimanche 02/08/2026, retour 05/08/2026 | Aucune anomalie de prix détectée (pas d'historique antérieur pour comparaison — premier relevé de prix réel du fichier). ATH ressort comme le tarif le plus bas du groupe (255 $), à surveiller si la tendance se confirme. | OK |
| 2026-07-30 03:36 | PRG, VIE, FCO, PFO, ATH, BUD, TBS × S1-S3 (21 recherches, dimanche, 3 nuits, vols directs uniquement) | Aucun gap (vol direct trouvé partout). Anomalies de prix notées : PRG (saut S1→S2), VIE (prix élevé constant), FCO (écart S1 vs S2-S3), BUD (S1 plus cher) | OK — 1 erreur transitoire Cloudflare 502 sur TLV→FCO S2, résolue au retry immédiat |
| 2026-07-31 | PRG, VIE, FCO, PFO, ATH, BUD, TBS × S1-S3 (21 recherches) | Premier run — pas d'historique antérieur pour comparaison. PRG S3 à 977$ contre ~560$ sur S1/S2 (+~75%) ; FCO S1 à 722$ contre ~370$ sur S2/S3 (+~90%) ; ATH S3 à 454$ contre ~270-285$ sur S1/S2 (+~65%) — à surveiller. Aucun gap de disponibilité. | Opérationnel |
| 2026-08-04 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, dimanche 09/08→12/08, 3 nuits, vols directs) | PRG (730$), VIE (836$) et TBS (625$) nettement plus chers que ATH/BUD/FCO/PFO (310-366$). PRG et TBS n'ont que 4 offres directes chacun (vs 15 pour les autres) — probable cause : faible fréquence de vols directs plutôt qu'une vraie hausse de tarif. À surveiller. | OK |
| 2026-08-05 | PRG, VIE, FCO, PFO, ATH, BUD, TBS × S1-S3 (21 recherches) | Gap : PRG dimanche S2 (comblé lundi 17/08, +23% vs S1). Anomalies prix : VIE S3 +66% vs S2 ; PFO S3 dépasse 400$ (520$, +112% vs S1) ; ATH S2 dépasse 400$ (442$). Tendances haussières S1→S3 sur PRG et BUD. TBS ajouté hors liste Groupe A/B du skill — à valider avec Jacques. | Disponible, 21/21 recherches réussies |
| 2026-08-06 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, dimanche 09/08/2026, 3 nuits, vols directs uniquement) | Aucun gap. Aucune anomalie de prix détectée (pas d'historique pour comparaison). TBS n'appartient pas à la liste de référence des 18 destinations du skill — ajouté ponctuellement. AMS, LHR, CDG (Groupe A habituel) non couverts, non demandés. | ✅ Connecteur Kiwi.com disponible et fonctionnel |
| 2026-08-07 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, dimanche 09/08 → mercredi 12/08, 3 nuits, 0 escale) | Premier run réel — pas d'historique pour comparer une tendance. TBS ressort comme la destination la plus chère (742 $, Israir/Arkia uniquement) contre 625 $ VIE et 692 $ PRG ; PFO nettement la moins chère (267 $). Rien qui ressemble à une erreur de prix. S2/S3 non demandés, laissés vides. | ✅ OK |
| 2026-08-08 03:33 | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, dép. dimanche 09/08/2026, retour 12/08/2026, 3 nuits, vols directs uniquement) | Aucun gap. Anomalie notée : PRG à 778$ nettement au-dessus de VIE (643$) et BUD (579$) alors que la distance/durée de vol est comparable — à surveiller faute d'historique pour confirmer une tendance. | OK |
| 2026-08-09 03:35 (run initial) | PRG, VIE, FCO, PFO, ATH, BUD, TBS — dimanche 16/08/2026, A/R 3 nuits | PRG anormalement cher (1244 $) — plus de 3× BUD (384$) et près de 2× VIE (690$), aucune alternative directe sous 1000$ trouvée. Hypothèses : capacité limitée sur la route pour cette date précise, ou effet saisonnier (mi-août). | ✅ Disponible |
| 2026-08-10 (run automatisé, portée S1-S3) | PRG, VIE, FCO, PFO, ATH, BUD, TBS × S1-S3 (21 recherches) | 2 anomalies de prix (PRG S1 = 1201 $, VIE S2 = 1229 $) ; écart de portée entre la liste de 7 destinations transmise par la routine et la liste "Groupe A" (9) du skill — à valider par Jacques ; aucun gap de vol direct | OK — connecteur disponible, 21/21 recherches réussies |
| 2026-08-11 03:34 UTC | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, A/R 3 nuits) | **Gap PRG** : aucun vol direct TLV→PRG le dimanche 16/08 (route opérée seulement lun/mer/jeu/ven/sam sur cette période) → décalé au lundi 17/08, retour 20/08, prix 843 $, soit ~1.4-2.3x le prix des autres destinations (366-596 $) — plausible (décalage de date + capacité directe réduite) mais à re-vérifier. **TBS** : 734 $, second prix le plus élevé du groupe, cohérent avec une capacité directe limitée (1 vol/jour Arkia/Israir), à surveiller dans la durée. Premier run réel de ce fichier sur `main` — pas d'historique antérieur disponible sur cette branche pour comparaison de tendance (voir note de reconstitution d'historique ci-dessus). | OK — connecteur disponible et utilisé pour les 7 destinations (recherches directes + recherches de secours flexibles pour PRG/TBS) |
| 2026-08-12 03:34 UTC | PRG, VIE, FCO, PFO, ATH, BUD, TBS (S1, A/R 3 nuits) | **Gap PRG persistant** : toujours aucun vol direct dimanche 16/08 pour la 2e journée consécutive → décalé lundi 17/08 → jeudi 20/08, 706 $ (en baisse vs 843 $ hier mais toujours ~1.3-1.8x le reste du groupe — route à considérer comme structurellement non-dominicale sur cette période, à confirmer avec Jacques). **TBS en hausse** : 843 $ (+14.8% vs 734 $ hier), confirme sa position de 2e destination la plus chère du groupe pour la 2e fois consécutive — cohérent avec la capacité limitée déjà notée (1 vol/jour Arkia/Israir), tendance haussière à surveiller mais pas d'action requise. Autres destinations (VIE 625$, FCO 394$, PFO 396$, ATH 508$, BUD 527$) en ligne avec la fourchette habituelle (variation jour-à-jour normale de +0 à +9% vs hier). | ✅ OK — connecteur Kiwi.com disponible et fonctionnel pour la 4e fois consécutive sur ce périmètre |
