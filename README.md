# Magyar Quiz

Une application web interactive conçue pour aider les utilisateurs à se préparer à l'examen de connaissances culturelles hongroises (Magyar Kulturális Ismereti Vizsga).

## Fonctionnalités

- 6 quiz thématiques avec 5 questions chacun
- Questions en hongrois avec choix multiples (A, B, C)
- Affichage des scores et des explications pour chaque réponse
- Calcul du score total sur l'ensemble des quiz
- Interface responsive et facile à utiliser

## Thèmes des quiz

1. Symboles nationaux et fêtes (Nemzeti jelképek és ünnepek)
2. Événements historiques majeurs (Történelmi események)
3. Littérature et musique (Irodalom és zene)
4. Institutions constitutionnelles (Alkotmányos intézmények)
5. Droits et devoirs des citoyens (Állampolgári jogok és kötelességek)
6. Questions mixtes (Vegyes kérdések)

## Comment démarrer l'application

1. Clonez ce dépôt
2. Installez les dépendances : `pip install flask`
3. Lancez l'application : `python main.py`
4. Accédez à l'application dans votre navigateur à l'adresse : `http://localhost:5000`

## Structure de l'application

- `main.py` : Point d'entrée de l'application
- `app.py` : Configuration Flask et routes
- `questions.json` : Base de données des questions de quiz
- `templates/` : Fichiers HTML
- `static/` : Fichiers CSS et JavaScript

## Technologies utilisées

- Backend : Python avec Flask
- Frontend : HTML, CSS, JavaScript
- Styling : Bootstrap 5
- Stockage des données : JSON
