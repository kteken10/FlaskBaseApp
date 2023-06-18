# Application Mobile de Shop

Ce projet est une application mobile de boutique simple, organisée, structurée et bien configurée.

## Structure du projet

L'application suit une structure de projet typique pour une meilleure organisation et maintenabilité du code :

- `ShopMobileAppbackend/` : Dossier contenant le backend de l'application.
  - `app.py` : Fichier principal du backend de l'application, contenant la création de l'instance de l'application Flask et la définition des routes.
  - `config.py` : Fichier de configuration du backend de l'application, où vous pouvez définir les variables de configuration telles que les paramètres de base de données, les clés secrètes, etc.
  - `models.py` : Fichier contenant le modèle de données du backend de l'application. Vous pouvez définir les classes de modèle, les relations entre les tables, etc. ici.
  - `.env` : Fichier d'environnement contenant les variables d'environnement du backend de l'application. C'est l'endroit où vous pouvez stocker des informations sensibles telles que les identifiants de connexion à la base de données. Assurez-vous de ne pas inclure ce fichier dans votre dépôt de code source pour des raisons de sécurité.

- `ShopMobileAppFrontend/` : Dossier contenant le frontend de l'application.
  - `App.js` : Fichier principal du frontend de l'application, contenant la logique de l'interface utilisateur et les appels d'API vers le backend.

## Installation

1. Clonez le dépôt du projet : `git clone https://github.com/votre-utilisateur/application-mobile-shop.git`
2. Accédez au répertoire du projet : `cd application-mobile-shop`
3. Installez les dépendances du backend : `cd ShopMobileAppbackend && pip install -r requirements.txt`
4. Installez les dépendances du frontend : `cd ../ShopMobileAppFrontend && npm install`

## Configuration de la base de données

1. Ouvrez le fichier `ShopMobileAppbackend/.env` et mettez à jour la valeur de la variable `DB_URI` avec votre URI de connexion à la base de données :
   - Exemple : `DB_URI=postgresql://utilisateur:motdepasse@hôte:port/nom_de_la_base_de_données`
2. Assurez-vous que votre base de données est configurée correctement avec les mêmes informations.

## Exécution du backend

1. Assurez-vous d'être dans le répertoire `ShopMobileAppbackend/`.
2. Lancez le backend de l'application : `python app.py`
3. L'application backend sera accessible à l'adresse `http://localhost:5000`

## Exécution du frontend

1. Assurez-vous d'être dans le répertoire `ShopMobileAppFrontend/`.
2. Lancez l'application frontend : `expo start`
3. Ouvrez l'application Expo sur votre appareil mobile ou émulateur et scannez le code QR affiché dans la console Expo pour lancer l'application.

N'hésitez pas à explorer le code source du backend et du frontend de l'application, et à les adapter selon vos besoins.

