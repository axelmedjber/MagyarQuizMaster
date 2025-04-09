#!/bin/bash

# Script pour préparer le déploiement sur Hostinger
echo "=== Préparation du déploiement de Magyar Quiz sur Hostinger ==="

# Créer le répertoire de déploiement
mkdir -p hostinger_deploy
echo "✅ Dossier de déploiement créé"

# Copier les fichiers nécessaires
echo "Copie des fichiers..."
cp -R templates static questions.json app.py passenger_wsgi.py .htaccess requirements-hostinger.txt README.md hostinger_deploy/
echo "✅ Fichiers principaux copiés"

# Créer un fichier README spécifique pour l'hébergement s'il n'existe pas déjà
if [ ! -f hostinger_deploy/README_HOSTINGER.md ]; then
  cat > hostinger_deploy/README_HOSTINGER.md << EOF
# Magyar Quiz - Instructions de déploiement sur Hostinger

## Installation

1. Téléchargez tous les fichiers dans le répertoire \`public_html\` de votre hébergement via FTP
2. Connectez-vous à votre panneau de contrôle Hostinger
3. Allez dans la section "Terminal SSH" ou utilisez SSH directement
4. Naviguez vers votre répertoire \`public_html\`
5. Créez un environnement virtuel Python:
   \`\`\`
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements-hostinger.txt
   \`\`\`
6. Redémarrez l'application Python dans le panneau de contrôle Hostinger

## Configuration de Python sur Hostinger

1. Dans le panneau de contrôle Hostinger, allez dans "Avancé" > "Configuration Python"
2. Activez l'application Python
3. Définissez le chemin d'accès à l'application Python: \`/\`
4. Définissez le script de démarrage: \`passenger_wsgi.py\`
5. Sélectionnez la version Python: \`Python 3.8\` ou plus récente
6. Cliquez sur "Enregistrer"

## Configuration des variables d'environnement

Dans le panneau de contrôle Hostinger, ajoutez la variable d'environnement suivante:
- Nom: \`SESSION_SECRET\`
- Valeur: \`générez une valeur aléatoire sécurisée\`

## Dépannage

Si vous rencontrez des problèmes:
1. Vérifiez les journaux d'erreurs dans le panneau de contrôle Hostinger
2. Assurez-vous que le module Python est activé
3. Vérifiez que tous les fichiers ont été correctement téléchargés
4. Vérifiez les permissions des fichiers (644 pour les fichiers, 755 pour les dossiers)

Pour des informations plus détaillées, consultez le fichier \`FLASK_HOSTINGER_GUIDE.md\`
EOF
  echo "✅ Instructions d'installation créées"
fi

# Créer un fichier zip pour faciliter le téléchargement
cd hostinger_deploy
zip -r ../magyar-quiz-hostinger.zip .
cd ..
echo "✅ Archive magyar-quiz-hostinger.zip créée"

echo ""
echo "=== Instructions de déploiement ==="
echo "1. Téléchargez le fichier magyar-quiz-hostinger.zip"
echo "2. Décompressez-le et téléversez tous les fichiers dans le répertoire public_html via FTP:"
echo "   - Hôte FTP: ftp://floralwhite-trout-805615.hostingersite.com"
echo "   - Nom d'utilisateur: u963436280.floralwhite-trout-805615.hostingersite.com"
echo "   - Chemin d'accès: public_html"
echo "3. Suivez les instructions dans les fichiers README_HOSTINGER.md et FLASK_HOSTINGER_GUIDE.md"
echo ""
echo "Votre site sera accessible à l'adresse: http://floralwhite-trout-805615.hostingersite.com"
echo ""
echo "Note: Pour utiliser un nom de domaine personnalisé, vous devrez configurer les DNS dans le panneau de contrôle Hostinger."