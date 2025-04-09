#!/bin/bash

# Script pour préparer le projet Android pour la compilation APK
echo "=== Préparation du projet Magyar Quiz pour la compilation APK ==="

# 1. Mettre à jour les fichiers du projet Android
echo "Synchronisation des fichiers web..."
npx cap copy android

# 2. Mettre à jour les variables.gradle pour une meilleure compatibilité
echo "Mise à jour des configurations de build..."
cat > android/variables.gradle << EOF
ext {
    minSdkVersion = 21
    compileSdkVersion = 33
    targetSdkVersion = 33
    androidxActivityVersion = '1.4.0'
    androidxAppCompatVersion = '1.4.2'
    androidxCoordinatorLayoutVersion = '1.2.0'
    androidxCoreVersion = '1.8.0'
    androidxFragmentVersion = '1.4.1'
    coreSplashScreenVersion = '1.0.0'
    androidxWebkitVersion = '1.4.0'
    junitVersion = '4.13.2'
    androidxJunitVersion = '1.1.3'
    androidxEspressoCoreVersion = '3.4.0'
    cordovaAndroidVersion = '10.1.1'
}
EOF

# 3. Mettre à jour le build.gradle principal pour une version de Gradle plus compatible
echo "Mise à jour de la configuration Gradle..."
cat > android/build.gradle << EOF
// Top-level build file where you can add configuration options common to all sub-projects/modules.

buildscript {
    
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:7.2.1'
        classpath 'com.google.gms:google-services:4.3.13'

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}

apply from: "variables.gradle"

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
EOF

# 4. Créer un fichier local.properties
echo "Configuration du SDK Android..."
cat > android/local.properties << EOF
## This file must *NOT* be checked into Version Control Systems,
# as it contains information specific to your local configuration.
#
# Location of the SDK. This is only used by Gradle.
# For customization when using a Version Control System, please read the
# header note.
sdk.dir=/opt/android/sdk
EOF

# 5. Ajouter un script de build simplifié pour l'APK
echo "Création d'un script de build simplifié..."
cat > android/build-apk.sh << EOF
#!/bin/bash
cd \$(dirname \$0)
echo "Compilation de l'APK de Magyar Quiz..."
./gradlew assembleDebug
echo "Si la compilation a réussi, l'APK se trouve dans: app/build/outputs/apk/debug/app-debug.apk"
EOF
chmod +x android/build-apk.sh

# 6. Créer un fichier zip du projet Android optimisé
echo "Création d'un fichier zip du projet Android optimisé..."
cd android && zip -r ../magyar-quiz-android-ready.zip . -x "*.gradle.kts" -x "*.gradle/wrapper*" -x "*build/outputs*" -x "*.idea*" -x "*.iml" -x "*local.properties~"

echo "✅ Projet préparé avec succès: magyar-quiz-android-ready.zip"
echo ""
echo "Instructions pour construire l'APK:"
echo "-----------------------------------"
echo "Option 1 - Compilation en ligne (recommandé):"
echo "1. Téléchargez le fichier magyar-quiz-android-ready.zip"
echo "2. Allez sur https://appetize.io/upload"
echo "3. Téléchargez le fichier zip et suivez les instructions"
echo ""
echo "Option 2 - Compilation locale avec Android Studio:"
echo "1. Téléchargez le fichier magyar-quiz-android-ready.zip"
echo "2. Décompressez le fichier"
echo "3. Ouvrez Android Studio"
echo "4. Sélectionnez 'Open an existing Android Studio project'"
echo "5. Naviguez jusqu'au dossier décompressé et sélectionnez-le"
echo "6. Une fois le projet chargé, cliquez sur 'Build > Build Bundle(s) / APK(s) > Build APK(s)'"
echo "7. L'APK sera généré dans le dossier app/build/outputs/apk/debug/"
echo ""
echo "Option 3 - Compilation sans Android Studio:"
echo "1. Téléchargez le fichier magyar-quiz-android-ready.zip"
echo "2. Décompressez le fichier"
echo "3. Assurez-vous que le SDK Android est installé"
echo "4. Ouvrez un terminal dans le dossier décompressé"
echo "5. Exécutez './build-apk.sh'"
echo "6. L'APK sera généré dans le dossier app/build/outputs/apk/debug/"