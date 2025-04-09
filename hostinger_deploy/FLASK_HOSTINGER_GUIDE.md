# Guide de déploiement Flask sur Hostinger

Ce guide vous explique comment déployer correctement une application Flask sur l'hébergement Hostinger.

## Prérequis

1. Un compte Hostinger avec Python activé
2. Accès FTP à votre hébergement
3. Une application Flask fonctionnelle

## Structure de fichiers recommandée

Voici la structure de fichiers recommandée pour votre déploiement:

```
public_html/
├── .htaccess                # Configuration Apache
├── passenger_wsgi.py        # Point d'entrée pour Passenger WSGI
├── app.py                   # Votre application Flask
├── requirements-hostinger.txt  # Dépendances Python
├── static/                  # Fichiers statiques (CSS, JS, images)
├── templates/               # Templates HTML
└── venv/                    # Environnement virtuel Python (créé sur le serveur)
```

## Étape 1: Configuration Python sur Hostinger

1. Connectez-vous à votre panneau de contrôle Hostinger
2. Allez dans "Avancé" > "Configuration Python"
3. Activez l'application Python
4. Choisissez la version Python (recommandé: Python 3.8 ou plus récent)
5. Définissez le chemin de l'application: `/`
6. Définissez le script de démarrage: `passenger_wsgi.py`
7. Cliquez sur "Enregistrer"

## Étape 2: Téléversement des fichiers

1. Utilisez un client FTP (comme FileZilla) pour vous connecter à votre serveur
2. Téléversez tous les fichiers dans le répertoire `public_html`
3. Assurez-vous que les permissions sont correctes:
   - Fichiers: 644 (rw-r--r--)
   - Dossiers: 755 (rwxr-xr-x)

## Étape 3: Configuration de l'environnement virtuel

1. Connectez-vous à votre serveur en SSH
2. Naviguez vers votre répertoire `public_html`
3. Créez et activez un environnement virtuel:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements-hostinger.txt
   ```

## Étape 4: Configuration des variables d'environnement

Hostinger permet de définir des variables d'environnement via le panneau de contrôle:

1. Allez dans "Avancé" > "Variables d'environnement"
2. Ajoutez les variables nécessaires (comme `SESSION_SECRET`)
3. Cliquez sur "Enregistrer"

## Dépannage

### Erreur 500 Internal Server Error

Vérifiez les journaux d'erreur dans le panneau de contrôle Hostinger (section "Logs").

### L'application ne démarre pas

1. Vérifiez que le module Python est activé
2. Vérifiez que `passenger_wsgi.py` est correctement configuré
3. Assurez-vous que toutes les dépendances sont installées

### Problèmes de chemin d'accès aux fichiers

Dans votre code Flask, utilisez toujours des chemins relatifs ou absolus complets:

```python
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'questions.json')
```

### Redémarrage de l'application

Si vous modifiez votre code, vous devrez redémarrer l'application Python via le panneau de contrôle Hostinger (section "Redémarrer").

## Optimisations

### Mise en cache

Configurez le cache pour améliorer les performances:

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
@cache.cached(timeout=60)
def index():
    # ...
```

### Compression des ressources statiques

Le fichier `.htaccess` inclus configure déjà la compression GZIP pour les fichiers statiques.

### Utilisation de CDN

Envisagez d'utiliser un CDN comme Cloudflare pour améliorer les performances globales de votre application.