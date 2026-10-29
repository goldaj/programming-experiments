# Agent instructions — Programming Experiments

**Lire README.md puis docs/CHATGPT_PROJECT_HISTORY.md avant chaque changement.**

Projet : Archives pédagogiques Python, Java, C++ et petite démo web MetaMask ; expériences non destinées à la production.

Règles : Préserver exemples, attributions et historiques, isoler les commandes par langage et sous-dossier ; ne pas présumer de tests complets.

Préserver la provenance et ne jamais écraser les versions existantes. Documenter ce qui a réellement été testé. Après chaque modification, enrichir docs/CHATGPT_PROJECT_HISTORY.md si une instruction, décision ou nouveau dialogue pertinent est disponible ; séparer citations exactes des résumés et noter les dates seulement si certaines. Ne publier ni secrets ni données privées.

## Aventure à embranchements, reprise du 29 octobre 2026

- Nouvelle branche `feat/branching-adventure-engine-20261029` basée sur `main`, sans PR concurrente lors de l'examen. Ne pas écraser le fichier historique `python/branching-adventure-qt/main.py`.
- `story_engine.py` : moteur pur Python, validation du graphe, objets/flags, choix conditionnels, sauvegarde atomique, reprise contrôlée et exploration des fins accessibles.
- `story.json` : contenu original français (18 scènes, 7 fins) ; pas de données privées.
- `play_cli.py` : version jouable sans dépendances ; `play_qt.py` : interface améliorée nécessitant PyQt5. Aucun lien réseau.
- Lire `docs/ADVENTURE_GUIDE.md`. Les tests d'état, sauvegardes, choix conditionnels et terminaison se trouvent dans `tests/test_branching_adventure.py`.
- Commandes CI : `python -m unittest discover -s tests -p 'test_branching_adventure.py' -v` et `python python/branching-adventure-qt/play_cli.py --audit`. Vérifier les runs réels avant de déclarer tests verts.
- Préserver toutes les sauvegardes locales `.adventure_save.json` (ignorées) ; ne pas les versionner ou les remplacer par des exemples. Vérifier GUI sur un vrai poste PyQt5 avant merge. Pas de fusion automatique.
