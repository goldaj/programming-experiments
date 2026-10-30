# Audit GitHub et passation — 30 octobre 2026

**Mission :** Bibliothèque d'exercices Python/Java/C++/web indépendants. Revue documentaire et GitHub uniquement, aucune compilation ni test exécutés pendant cette passe.

## Inventaire des branches
Branche principale : `main`.
- `feat/branching-adventure-engine-20261029` (`c8d7210ab7b18480cf3949bb4478ebff509295c9`) — behind, ahead 0, behind 3 par comparaison directe
- `main` (`01ab7ac20196409d234156e09ddd5b31bca8b03c`) — référence à conserver

## Pull requests
- [#1](https://github.com/goldaj/programming-experiments/pull/1) : fusionnée (`feat/branching-adventure-engine-20261029` → `main`).

## Challenge fonctionnel
Le nouveau moteur d'aventure doit garantir graphe atteignable, terminaisons, conditions d'inventaire/flags, sauvegarde atomique et impossibilité d'états morts. Le CLI ne prouve pas l'ergonomie PyQt5, et les exemples ne sont pas une application de production.

## Prochain agent
1. Lire docs/ADVENTURE_GUIDE.md et historique. 2. Lancer l'audit de story.json et tests Python. 3. Tester PyQt5 manuellement et ne pas écraser les autres expériences.

## Garde-fous et sources
Lire README (« # Expériences de programmation »), AGENTS.md et docs/CHATGPT_PROJECT_HISTORY.md. Ne pas annoncer de tests ou de validation manuelle non réalisés. Une branche anciennement fusionnée reste une référence Git à examiner avant nettoyage. Aucun code/prod/PR/branche modifié ; ajout de cette note de passation seulement.
