#!/bin/bash

# Script pour exporter le projet Android Magyar Quiz

# Mettre à jour les fichiers du projet Android
npx cap copy android

echo "Création d'un fichier zip du projet Android..."
cd android && zip -r ../magyar-quiz-android.zip .

echo "✅ Projet exporté avec succès: magyar-quiz-android.zip"
echo ""
echo "Instructions pour construire l'APK:"
echo "-----------------------------------"
echo "1. Téléchargez le fichier magyar-quiz-android.zip sur votre ordinateur"
echo "2. Décompressez le fichier"
echo "3. Ouvrez Android Studio"
echo "4. Sélectionnez 'Open an existing Android Studio project'"
echo "5. Naviguez jusqu'au dossier décompressé et sélectionnez-le"
echo "6. Attendez que Gradle synchronise le projet"
echo "7. Dans le menu, sélectionnez 'Build' > 'Build Bundle(s) / APK(s)' > 'Build APK(s)'"
echo "8. L'APK sera généré dans le dossier app/build/outputs/apk/debug/"
echo ""
echo "Vous pouvez ensuite installer cet APK sur votre appareil Android."