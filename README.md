# Expériences de programmation

Archives d’apprentissage et petits programmes autonomes en Python, Java et C++. Ce dépôt montre des essais de conception, d’algorithmes et d’interfaces ; il ne présente pas ces exercices comme des applications terminées.

| Dossier | Sujet | Dépendances |
| --- | --- | --- |
| `python/prime-number-analysis/` | Exploration des nombres premiers et d’exports de données | Python, pandas |
| `python/prime-numbers-tkinter/` | Recherche de nombres premiers avec interface | Python, Tkinter |
| `python/branching-adventure-qt/` | Mini récit à embranchements, boutons et état d’interface | Python, PyQt5 |
| `java/calculator/` | Analyse et calcul d’une expression arithmétique | JDK |
| `java/roman-numerals/` | Conversion de chiffres romains | JDK |
| `cpp/project-euler/` | Essais pour des exercices algorithmiques | Compilateur C++ |

Pour Python, lancer `python main.py` depuis le sous-dossier concerné après installation des dépendances. Pour Java, compiler le fichier dans `src/`, puis lancer la classe `Calculator` ou `Converter`. Les noms des exercices C++ conservent les différentes tentatives d’origine.

Les commentaires et attributions des sources sont conservés. Les corrections de cours fournies par des tiers et les exemples livrés avec des bibliothèques ne sont pas inclus. Les scripts vides et simples modèles de l’IDE ne sont pas présentés comme des réalisations.

Validation de l’import : analyse syntaxique Python et compilation Java/C++ quand l’outil local le permet. La vérification fonctionnelle approfondie et la normalisation des dépendances restent à faire.

## Mini démonstration web

`web/metamask-connect/index.html` explore l’accès au compte sélectionné via le fournisseur Ethereum du navigateur et les messages de refus/absence d’extension. Le fichier ne contient aucune adresse, clé ou transaction préconfigurée. C’est une simple expérience d’interface, sans intégration métier ; aucune connexion à un portefeuille réel n’a été effectuée pour l’import.

Limite de l’expérience de transformation des nombres premiers : le script conservé est exploratoire et sa boucle peut produire un export vide ; son hypothèse de transformation reste à reprendre.

## Vérification des sources historiques

Les deux exercices Java compilent avec le JDK local. Trois des quatre essais C++ passent la vérification syntaxique. `cpp/project-euler/projet_euler_2_try1/main.cpp` reste une ébauche non compilable : après activation de C++11, une référence à la variable `f` demeure non déclarée. Cette version est conservée comme travail inachevé ; elle n’est pas présentée comme une solution validée.

## Aventure à embranchements : nouvelle version jouable

L'ancienne démo PyQt de deux choix `python/branching-adventure-qt/main.py` reste intacte. Une nouvelle version **entièrement jouable en français** propose 18 scènes, des objets à récupérer, des choix conditionnels, 7 fins différentes et une sauvegarde automatique par étape.

**Sans installation :**
```bash
python python/branching-adventure-qt/play_cli.py
python python/branching-adventure-qt/play_cli.py --audit
```

**Avec interface :**
```bash
python -m pip install PyQt5
python python/branching-adventure-qt/play_qt.py
```

Aucun réseau n'est utilisé. Une sauvegarde `.adventure_save.json` est créée localement et ignorée par Git. Les deux interfaces partagent le même moteur et le même format de sauvegarde. Tests automatiques sans PyQt : `python -m unittest discover -s tests -p 'test_branching_adventure.py' -v`. Voir [Guide aventure](docs/ADVENTURE_GUIDE.md) pour la reprise Codex, les limites et les méthodes de test.
