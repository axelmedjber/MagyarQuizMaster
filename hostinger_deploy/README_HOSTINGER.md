# Magyar Quiz - Instructions de déploiement sur Hostinger

## Installation

1. Téléchargez tous les fichiers dans le répertoire `public_html` de votre hébergement via FTP
2. Connectez-vous à votre panneau de contrôle Hostinger
3. Allez dans la section "Terminal SSH" ou utilisez SSH directement
4. Naviguez vers votre répertoire `public_html`
5. Créez un environnement virtuel Python:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements-hostinger.txt
   ```
6. Redémarrez l'application Python dans le panneau de contrôle Hostinger

## Configuration de Python sur Hostinger

1. Dans le panneau de contrôle Hostinger, allez dans "Avancé" > "Configuration Python"
2. Activez l'application Python
3. Définissez le chemin d'accès à l'application Python: `/`
4. Définissez le script de démarrage: `passenger_wsgi.py`
5. Sélectionnez la version Python: `Python 3.8` ou plus récente
6. Cliquez sur "Enregistrer"

## Configuration des variables d'environnement

Dans le panneau de contrôle Hostinger, ajoutez la variable d'environnement suivante:
- Nom: `SESSION_SECRET`
- Valeur: `générez une valeur aléatoire sécurisée`

## Dépannage

Si vous rencontrez des problèmes:
1. Vérifiez les journaux d'erreurs dans le panneau de contrôle Hostinger
2. Assurez-vous que le module Python est activé
3. Vérifiez que tous les fichiers ont été correctement téléchargés
4. Vérifiez les permissions des fichiers (644 pour les fichiers, 755 pour les dossiers)
