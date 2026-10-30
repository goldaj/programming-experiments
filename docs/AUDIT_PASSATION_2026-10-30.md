# Audit contradictoire / passation du 30 octobre 2026 — goldaj/programming-experiments

Source : branches, PR et arborescence GitHub ; tests et gameplay non exécutés.

## Branches
Branche principale `main` : `1b777b77186dc9765a7b92d3719c2fff8324c6c4`.
- `feat/branching-adventure-engine-20261029` : `behind`, 0 commits exclusifs, 1 commits de retard. Historique absorbé ; retirer après contrôle des usages GitHub.

## PR historiques
- [#1](https://github.com/goldaj/programming-experiments/pull/1) — closed, fusionnée : feat: 18-scene branching adventure with real inventory, seven endings and saves

## Structure observée
`.github`, `.gitignore`, `AGENTS.md`, `README.md`, `cpp`, `docs`, `java`, `python`, `tests`, `web`.

## Contre-questions fonctionnelles à tester
1. Rejouer les 18 scènes du moteur d'aventure et vérifier la cohérence des embranchements.
2. Tester les sept fins, l'inventaire, les sauvegardes et restaurations malformées.
3. Isoler les exemples pédagogiques des outils livrables et fournir une matrice de tests traçable.
4. Examiner la CI/les scripts, exécuter tests et partie manuelle avant certification ; aucune preuve de test nouveau n'est fournie par cette revue.
5. Conserver les branches de référence, éviter les PR redondantes, rattacher les preuves et les défauts observés au prochain commit.
