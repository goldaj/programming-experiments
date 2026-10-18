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
