# Historique de projet ChatGPT — Programming Experiments

Archive de transmission à Codex créée le 2026-10-24, **non exhaustive**. Aucun export intégral des anciens échanges n'est disponible dans cette session.

## Périmètre vérifié dans README.md
Archives pédagogiques Python, Java, C++ et petite démo web MetaMask ; expériences non destinées à la production.

## Règles de reprise
Préserver exemples, attributions et historiques, isoler les commandes par langage et sous-dossier ; ne pas présumer de tests complets.

## Échanges attestés
- **2026-10-18** — Assistant (résumé reconstruit, non verbatim) : regroupement d'archives d'apprentissage/prototypes dans des dépôts distincts, conservation de la provenance et documentation honnête du niveau de validation.
- **2026-10-18 13:24:13 UTC** — Utilisateur (extrait verbatim) : « N'écrase aucun repo existant. »
- **2026-10-24** — Utilisateur (résumé reconstruit, non verbatim) : demande un AGENTS.md propre au dépôt, un historique lisible par Codex avec messages utilisateur/assistant et horodatages disponibles, ainsi qu'une mise à jour récurrente de la documentation.

## Limites et maintenance
Les transcriptions exactes des échanges précédents et leurs horaires ne sont pas disponibles ici ; aucune réponse de l'assistant n'a été inventée. Lorsque le propriétaire fournit des exports authentiques, conserver la distinction rôle/date/texte et vérifier les informations sensibles avant commit. Ajouter les nouveaux échanges sourcés en fin de document, sans réécrire le passé.

## Intervention du 29 octobre 2026 — véritable aventure à embranchements (résumé non verbatim)

- Contexte : poursuite immédiate d'améliorations GitHub fonctionnelles, sans revenir dans cette conversation sur mini-LLM, Éclaire, Space Invaders et Android Widget Lab une fois sa PR terminée.
- Dépôt choisi après inventaire de branches et PR : `goldaj/programming-experiments`, initialement `main` seule et aucune PR ouverte. Sous-dossier initial : prototype PyQt de 2 options, sans sauvegarde.
- Implémentation sur branche `feat/branching-adventure-engine-20261029` en **préservant** le `main.py` originel : moteur data-driven Python standard, histoire française de 18 scènes/7 fins, reprise de sauvegarde atomique, moteur de conditions pour inventaire/drapeaux, interface terminal et nouvelle interface PyQt distincte.
- Preuves prévues : tests `tests/test_branching_adventure.py` (fin accessibles, gates, restauration, erreurs, parcours CLI) et workflow Python 3.10/3.12 ; exécution réelle à confirmer dans Actions, validation graphique PyQt5 à effectuer sur poste.
- Instructions : ne pas forger de mesures, conserver l'original et les sauvegardes locales, ne pas fusionner sans revue. Lire `docs/ADVENTURE_GUIDE.md`.
