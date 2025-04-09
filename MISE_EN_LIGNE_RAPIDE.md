# Guide de mise en ligne rapide - Magyar Quiz sur Hostinger

## Étapes de déploiement

1. **Téléchargez** le fichier `magyar-quiz-hostinger.zip` depuis ce projet
2. **Décompressez** le fichier sur votre ordinateur
3. **Connectez-vous** à votre compte Hostinger FTP:
   - Hôte FTP: `ftp://floralwhite-trout-805615.hostingersite.com`
   - Nom d'utilisateur: `u963436280.floralwhite-trout-805615.hostingersite.com`
   - Chemin d'accès: `public_html`
4. **Téléversez** tous les fichiers décompressés dans votre répertoire `public_html`
5. **Configurez Python** dans le panneau de contrôle Hostinger:
   - Allez dans "Avancé" > "Configuration Python"
   - Activez l'application Python
   - Définissez le chemin d'accès à l'application Python: `/`
   - Définissez le script de démarrage: `passenger_wsgi.py`
   - Sélectionnez la version Python: `Python 3.8` ou plus récente
   - Cliquez sur "Enregistrer"
6. **Configurez la variable d'environnement** dans le panneau de contrôle:
   - Ajoutez `SESSION_SECRET` avec une valeur aléatoire sécurisée

## Installation des dépendances

À partir du terminal SSH de Hostinger:

```bash
cd public_html
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-hostinger.txt
```

## Vérification

Votre site sera accessible à l'adresse:
- http://floralwhite-trout-805615.hostingersite.com

## Dépannage

Si vous rencontrez des problèmes:
1. Vérifiez les journaux d'erreurs dans le panneau de contrôle Hostinger
2. Consultez les fichiers `README_HOSTINGER.md` et `FLASK_HOSTINGER_GUIDE.md` pour des informations plus détaillées

## Configuration d'un nom de domaine personnalisé

Pour configurer un nom de domaine personnalisé:
1. Achetez un nom de domaine (via Hostinger ou un autre registrar)
2. Configurez les enregistrements DNS pour pointer vers votre hébergement Hostinger
3. Configurez le domaine dans le panneau de contrôle Hostinger