# Simple Application Flask

Ce projet est une application Flask simple, organisée, structurée et bien configurée.

## Structure du projet

L'application suit une structure de projet typique pour une meilleure organisation et maintenabilité du code :

- `app.py` : Fichier principal de l'application, contenant la création de l'instance de l'application Flask et la définition des routes.
- `config.py` : Fichier de configuration de l'application, où vous pouvez définir les variables de configuration telles que les paramètres de base de données, les clés secrètes, etc.
- `models.py` : Fichier contenant le modèle de données de l'application. Vous pouvez définir les classes de modèle, les relations entre les tables, etc. ici.
- `.env` : Fichier d'environnement contenant les variables d'environnement de l'application. C'est l'endroit où vous pouvez stocker des informations sensibles telles que les identifiants de connexion à la base de données. Assurez-vous de ne pas inclure ce fichier dans votre dépôt de code source pour des raisons de sécurité.

## Installation

1. Clonez le dépôt du projet : `git clone https://github.com/votre-utilisateur/simple-app-flask.git`
2. Accédez au répertoire du projet : `cd simple-app-flask`
3. Créez un environnement virtuel : `python -m venv venv`
4. Activez l'environnement virtuel :
   - Sur Windows : `venv\Scripts\activate`
   - Sur macOS/Linux : `source venv/bin/activate`
5. Installez les dépendances : `pip install -r requirements.txt`

## Configuration de la base de données

1. Ouvrez le fichier `.env` et mettez à jour la valeur de la variable `DB_URI` avec votre URI de connexion à la base de données PostgreSQL :
   - Exemple : `DB_URI=postgresql://your_username:your_password@your_host:your_port/your_database`
2. Assurez-vous que votre base de données est configurée correctement avec les mêmes informations.

## Exécution de l'application

1. Activez l'environnement virtuel si ce n'est pas déjà fait.
2. Lancez l'application : `python main.py` votre application peut bien evidement porter le nom ` app.py`
3. Accédez à l'application dans votre navigateur à l'adresse `http://localhost:5000`

N'hésitez pas à explorer le code source de l'application et à l'adapter selon vos besoins.

