# Magyar Quiz - Application Android

Ce projet permet de créer une application Android pour Magyar Quiz en utilisant Capacitor. L'application encapsule le site web Magyar Quiz dans une application Android native.

## Fichiers prêts à l'emploi

Deux fichiers zip sont disponibles pour créer votre APK:

1. `magyar-quiz-android-ready.zip` - Version optimisée avec des configurations compatibles (recommandé)
2. `magyar-quiz-android.zip` - Version standard du projet Capacitor

## Options pour créer l'APK

### Option 1 : Service de build en ligne (Méthode la plus simple)

1. Téléchargez le fichier `magyar-quiz-android-ready.zip`
2. Allez sur [Appetize.io](https://appetize.io/upload) ou [BuildJet](https://buildjet.com/)
3. Téléversez le fichier zip et suivez les instructions pour générer votre APK
4. Téléchargez l'APK généré

### Option 2 : Utilisation d'Android Studio

1. Téléchargez le fichier `magyar-quiz-android-ready.zip`
2. Décompressez-le sur votre ordinateur
3. Ouvrez Android Studio
4. Sélectionnez "Open an existing Android Studio project"
5. Naviguez jusqu'au dossier décompressé et sélectionnez-le
6. Attendez que Gradle synchronise le projet
7. Dans le menu, sélectionnez "Build > Build Bundle(s) / APK(s) > Build APK(s)"
8. L'APK sera généré dans le dossier `app/build/outputs/apk/debug/`

### Option 3 : Utilisation de la ligne de commande (pour utilisateurs avancés)

Si vous avez le SDK Android installé sur votre ordinateur:

1. Téléchargez et décompressez `magyar-quiz-android-ready.zip`
2. Ouvrez un terminal dans le dossier décompressé
3. Exécutez `./build-apk.sh`
4. L'APK sera généré dans `app/build/outputs/apk/debug/app-debug.apk`

## Scripts utiles

- `prepare-for-apk.sh` - Optimise le projet pour faciliter la création d'APK et génère le fichier `magyar-quiz-android-ready.zip`
- `export-android.sh` - Crée une archive standard du projet Capacitor dans `magyar-quiz-android.zip`
- `build-apk.sh` (inclus dans le zip) - Script pour compiler l'APK en ligne de commande

## Personnalisation

### Icône de l'application

Pour changer l'icône de l'application, remplacez les fichiers dans les dossiers:
- `android/app/src/main/res/mipmap-*dpi/`

### Nom de l'application

Le nom de l'application peut être modifié dans le fichier:
- `android/app/src/main/res/values/strings.xml`

## Notes importantes

- L'application nécessite une connexion Internet pour fonctionner car elle charge le site web depuis l'URL `https://magyar-quiz.replit.app`
- Pour une application complètement hors ligne, il faudrait transformer le site Flask en application native Android