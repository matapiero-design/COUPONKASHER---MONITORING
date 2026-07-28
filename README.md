# CouponKasher — Monitoring tarifs

Repo support de la Routine planifiée qui automatise la vérification quotidienne des prix de vols
directs TLV → destinations casher de CouponKasher (auparavant déclenchée manuellement par Jacques
chaque jour).

## Contenu

- `ROUTINE_PROMPT.md` — le prompt exact envoyé par la Routine planifiée à chaque déclenchement, et
  les paramètres de cadence/cible.
- `Data/flight-prices.md` — résultat du dernier run automatisé : tableau de prix vols directs par
  destination/semaine, et journal des runs (gaps, anomalies, statut connecteur). Mis à jour
  automatiquement — ne pas éditer à la main.

## Logique métier

La logique de vérification (destinations, contraintes Shabbat, exclusion des vols à escale,
formule de prix package, cadence S1-S3 quotidien / S4-S8 hebdomadaire) est définie dans le skill
`dashboard-suivi-prix-sejours-casher` — ce repo ne fait qu'automatiser son déclenchement et stocker
le résultat de vol (l'hôtel reste vérifié séparément, en hebdomadaire, voir le skill).

## Automatisation

Une Routine (`create_trigger`) déclenche une session fraîche chaque jour à 6h heure d'Israël, qui
exécute le prompt de `ROUTINE_PROMPT.md` et pousse directement sur `main`.
