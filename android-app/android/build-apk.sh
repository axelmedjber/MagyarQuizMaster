#!/bin/bash
cd $(dirname $0)
echo "Compilation de l'APK de Magyar Quiz..."
./gradlew assembleDebug
echo "Si la compilation a réussi, l'APK se trouve dans: app/build/outputs/apk/debug/app-debug.apk"
