# Magyar Quiz

Une application web interactive conçue pour aider les utilisateurs à se préparer à l'examen de connaissances culturelles hongroises (Magyar Kulturális Ismereti Vizsga).

## Caractéristiques

- Quiz thématiques sur la culture hongroise
- Interface multilingue (hongrois, français, anglais)
- Design moderne avec Tailwind CSS
- Affichage bilingue des questions et réponses
- Version Android disponible

## Version mobile Android (APK)

L'application est maintenant disponible en version Android pour une utilisation sur appareils mobiles.

### Fichiers disponibles

- **[android-app/magyar-quiz-android-ready.zip](android-app/magyar-quiz-android-ready.zip)** - Version optimisée, recommandée pour la création d'APK
- **[android-app/magyar-quiz-android.zip](android-app/magyar-quiz-android.zip)** - Version standard du projet Android

### Trois méthodes pour créer l'APK

1. **Service en ligne** - Utiliser [Appetize.io](https://appetize.io/upload) pour générer l'APK sans installation
2. **Android Studio** - Ouvrir le projet et construire l'APK localement
3. **Ligne de commande** - Utiliser le script `build-apk.sh` inclus dans le zip

Pour les instructions détaillées, consultez le [README de la version Android](android-app/README.md).

## Utilisation de la version web

1. Accédez à l'application en ligne à l'adresse: [Magyar Quiz](https://magyar-quiz.replit.app)
2. Sélectionnez un thème de quiz
3. Répondez aux questions dans le temps imparti
4. Consultez vos résultats détaillés à la fin du quiz

## Notes techniques

- Application web construite avec Flask (Python)
- Base de données de questions en JSON avec traductions bilingues
- Interface utilisateur inspirée de Shadcn UI avec Tailwind CSS
- Version mobile créée avec Capacitor pour encapsuler l'application web

© 2025 Magyar Quiz