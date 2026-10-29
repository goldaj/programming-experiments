# Les passages de la montagne : guide de jeu et passation Codex

## Pourquoi ce chantier

Le script historique `python/branching-adventure-qt/main.py` ne comportait que deux boutons, chacun menant immédiatement à une fin, sans sauvegarde et sans moteur de récit. **Il est conservé à l'identique** pour provenance. La nouvelle version est une application parallèle, utilisable sans PyQt.

## Jouer maintenant

Dans un terminal depuis la racine du dépôt :

```bash
python python/branching-adventure-qt/play_cli.py
```

Le joueur sélectionne un choix par son numéro. Les commandes `s` (sauvegarder), `r` (nouvelle partie), `q` (quitter) sont toujours disponibles. Les choix réellement impossibles n'apparaissent pas, par exemple le tunnel sans lanterne ou la porte sans pierre gravée. Les scènes et choix proviennent de `story.json`, sans écriture de code.

Avec PyQt5 installé, une interface à boutons et zone de récit reprend exactement la même partie :

```bash
python -m pip install PyQt5
python python/branching-adventure-qt/play_qt.py
```

Le moteur et l'interface terminal fonctionnent avec la **bibliothèque standard de Python 3.10+**, hors ligne. `play_qt.py` importe PyQt5 seulement lors du lancement graphique. Les données sont enregistrées dans `python/branching-adventure-qt/.adventure_save.json`, **ignoré dans Git**. `--new` force une nouvelle partie sans charger la sauvegarde précédente ; les commandes `--story` et `--save` permettent de travailler sur un brouillon ou une sauvegarde distincte.

## La véritable nouveauté fonctionnelle

- **18 scènes / 7 fins** avec chemins de retour et décisions irréversibles.
- Inventaire (lanterne, carte, pierre gravée) et indices (lecture du carnet) qui débloquent/retirent des choix.
- Choix utilisables une seule fois, avec `not_items` et `not_flags`. Les objets peuvent être donnés ou retirés, les indices mémorisés.
- Reprise de la session entre le terminal et PyQt. Chaque action déclenche une sauvegarde atomique (fichier temporaire écrit et synchronisé puis renommé).
- Empreinte SHA-256 du scénario : une sauvegarde de la version A ne peut pas être chargée silencieusement dans la version B.
- Validateur de structure : IDs contrôlés, destinations existantes, conditions non contradictoires, fins terminales, taille limitée.
- Audit de toutes les fins via exploration des états **nœud + inventaire + drapeaux** (et limite de 10 000 états pour éviter les boucles sans fin).

```bash
python python/branching-adventure-qt/play_cli.py --audit
python -m unittest discover -s tests -p 'test_branching_adventure.py' -v
```

La CI de GitHub exécute ces commandes sur Python 3.10 et 3.12, et compile aussi la source historique sans l'exécuter. L'audit doit annoncer **7 / 7 fins accessibles** ; cela est un critère de livraison à vérifier et pas une mesure supposée.

## Format du scénario et méthode de test

Le fichier JSON contient `title`, `start` et un dictionnaire `nodes`. Chaque scène possède `title`, `text` et soit `ending` pour une fin, soit des `choices` avec `label` et `to`. Champs optionnels de chaque choix :

- `needs` : objets nécessaires ; `not_items` : objets absents ;
- `requires_flags` : indices nécessaires ; `not_flags` : indices non encore mémorisés ;
- `gives` : objets gagnés ; `takes` : objets dépensés ; `sets` : drapeaux activés.

Exemple : une option `{"label":"Ouvrir","to":"vault","needs":["rune"]}` s'affiche uniquement après récupération de la pierre gravée.

Le test en mémoire parcourt les scénarios avec `discover_endings`. La suite teste aussi les conditions, le scénario de jeu complet en terminal, la compatibilité de sauvegarde et les erreurs de données. **Les tests ne remplacent pas une vraie session graphique PyQt5** : il faudra encore vérifier la fenêtre, les contrôles, les chemins de sauvegarde et les textes sur Windows/Linux.

## Prochaines étapes

1. Exécuter la CI et réparer tout problème effectivement démontré, sans toucher au prototype d'origine.
2. Tester la nouvelle GUI sur un ordinateur doté de PyQt5.
3. Ajouter l'option de prévisualisation des conditions non remplies et un éditeur de scènes JSON, sans autoriser l'exécution de code depuis les histoires.
4. Produire des statistiques de rejouabilité (fréquence réelle des 7 fins) sur simulations ou sessions consenties ; ne pas collecter de télémétrie personnelle.
5. Ajouter davantage de ramifications de qualité narrative (rebondissements, conséquences durables, fins alternatives), en gardant l'audit automatique.

**Contexte Git** : `feat/branching-adventure-engine-20261029` dérive de `main` et isole ce chantier des autres expériences d'apprentissage. Aucun fichier de sauvegarde utilisateur, secret ni historique privé n'a été consulté ou ajouté. Ne pas merger automatiquement ; garder `AGENTS.md` et `docs/CHATGPT_PROJECT_HISTORY.md` à jour pour Codex.
