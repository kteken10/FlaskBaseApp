import os
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, session, jsonify, url_for,request
from flask_cors import CORS
from models import db, Visiteur, Fournisseur, Automobile, AutomobileImage
from config import config

app = Flask(__name__)
env_type = 'development'
secret_key = os.urandom(24).hex()
app.secret_key = secret_key
app.config.from_object(config[env_type])
db.init_app(app)
# Création des tables
with app.app_context():
    db.create_all()
CORS(app)  # Pour autoriser les requêtes CORS

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)



## GESTION DE L'AUTHENTICATION 
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("get_user_infos", _external=True)  # Remplacez par votre URL de redirection
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": "http://localhost:5000",  # Remplacez par votre URL de redirection après la déconnexion
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

# Routes pour les visiteurs
@app.route('/visiteurs', methods=['GET'])
def get_visiteurs():
    visiteurs = Visiteur.query.all()
    result = [
        {
            'id': visiteur.id,
            'nom': visiteur.nom,
            'email': visiteur.email,
            'numero_telephone': visiteur.numero_telephone,
            'photo_profil': visiteur.photo_profil,
            'date_enregistrement': visiteur.date_enregistrement.isoformat()
        }
        for visiteur in visiteurs
    ]
    return jsonify(result)

@app.route('/visiteurs/<int:visiteur_id>', methods=['GET'])
def get_visiteur(visiteur_id):
    visiteur = Visiteur.query.get(visiteur_id)
    if visiteur:
        result = {
            'id': visiteur.id,
            'nom': visiteur.nom,
            'email': visiteur.email,
            'numero_telephone': visiteur.numero_telephone,
            'photo_profil': visiteur.photo_profil,
            'date_enregistrement': visiteur.date_enregistrement.isoformat()
        }
        return jsonify(result)
    else:
        return jsonify({'message': 'Visiteur non trouvé'})

@app.route('/visiteurs', methods=['POST'])
def create_visiteur():
    data = request.json
    visiteur = Visiteur(
        nom=data['nom'],
        email=data['email'],
        numero_telephone=data['numero_telephone'],
        photo_profil=data['photo_profil'],
        date_enregistrement=data['date_enregistrement']
    )
    db.session.add(visiteur)
    db.session.commit()
    return jsonify({'message': 'Visiteur créé avec succès'})

# Routes pour les fournisseurs
@app.route('/fournisseurs', methods=['GET'])
def get_fournisseurs():
    fournisseurs = Fournisseur.query.all()
    result = [
        {
            'id': fournisseur.id,
            'nom_fournisseur': fournisseur.nom_fournisseur,
            'email': fournisseur.email,
            'numero_telephone': fournisseur.numero_telephone,
            'logo_fournisseur': fournisseur.logo_fournisseur,
            'date_enregistrement': fournisseur.date_enregistrement.isoformat(),
            'localisation': fournisseur.localisation,
            'adresse': fournisseur.adresse
        }
        for fournisseur in fournisseurs
    ]
    return jsonify(result)

@app.route('/fournisseurs/<int:fournisseur_id>', methods=['GET'])
def get_fournisseur(fournisseur_id):
    fournisseur = Fournisseur.query.get(fournisseur_id)
    if fournisseur:
        result = {
            'id': fournisseur.id,
            'nom_fournisseur': fournisseur.nom_fournisseur,
            'email': fournisseur.email,
            'numero_telephone': fournisseur.numero_telephone,
            'logo_fournisseur': fournisseur.logo_fournisseur,
            'date_enregistrement': fournisseur.date_enregistrement.isoformat(),
            'localisation': fournisseur.localisation,
            'adresse': fournisseur.adresse
        }
        return jsonify(result)
    else:
        return jsonify({'message': 'Fournisseur non trouvé'})

@app.route('/fournisseurs', methods=['POST'])
def create_fournisseur():
    data = request.json
    fournisseur = Fournisseur(
        nom_fournisseur=data['nom_fournisseur'],
        email=data['email'],
        numero_telephone=data['numero_telephone'],
        logo_fournisseur=data['logo_fournisseur'],
        date_enregistrement=data['date_enregistrement'],
        localisation=data['localisation'],
        adresse=data['adresse']
    )
    db.session.add(fournisseur)
    db.session.commit()
    return jsonify({'message': 'Fournisseur créé avec succès'})

# Routes pour les automobiles
@app.route('/automobiles', methods=['GET'])
def get_automobiles():
    automobiles = Automobile.query.all()
    result = [
        {
            'id': automobile.id,
            'marque': automobile.marque,
            'prix': float(automobile.prix),
            'type_vehicule': automobile.type_vehicule,
            'couleur': automobile.couleur,
            'date_enregistrement': automobile.date_enregistrement.isoformat(),
            'fournisseur_id': automobile.fournisseur_id
        }
        for automobile in automobiles
    ]
    return jsonify(result)

@app.route('/automobiles/<int:automobile_id>', methods=['GET'])
def get_automobile(automobile_id):
    automobile = Automobile.query.get(automobile_id)
    if automobile:
        result = {
            'id': automobile.id,
            'marque': automobile.marque,
            'prix': float(automobile.prix),
            'type_vehicule': automobile.type_vehicule,
            'couleur': automobile.couleur,
            'date_enregistrement': automobile.date_enregistrement.isoformat(),
            'fournisseur_id': automobile.fournisseur_id
        }
        return jsonify(result)
    else:
        return jsonify({'message': 'Automobile non trouvée'})

@app.route('/automobiles', methods=['POST'])
def create_automobile():
    data = request.json
    automobile = Automobile(
        marque=data['marque'],
        prix=data['prix'],
        type_vehicule=data['type_vehicule'],
        couleur=data['couleur'],
        fournisseur_id=data['fournisseur_id']
    )
    db.session.add(automobile)
    db.session.commit()
    return jsonify({'message': 'Automobile créée avec succès'})

# Routes pour les images d'automobile
@app.route('/images', methods=['GET'])
def get_images():
    images = AutomobileImage.query.all()
    result = [
        {
            'id': image.id,
            'url_image': image.url_image,
            'automobile_id': image.automobile_id
        }
        for image in images
    ]
    return jsonify(result)

@app.route('/images/<int:image_id>', methods=['GET'])
def get_image(image_id):
    image = AutomobileImage.query.get(image_id)
    if image:
        result = {
            'id': image.id,
            'url_image': image.url_image,
            'automobile_id': image.automobile_id
        }
        return jsonify(result)
    else:
        return jsonify({'message': 'Image non trouvée'})

@app.route('/images', methods=['POST'])
def create_image():
    data = request.json
    image = AutomobileImage(
        url_image=data['url_image'],
        automobile_id=data['automobile_id']
    )
    db.session.add(image)
    db.session.commit()
    return jsonify({'message': 'Image créée avec succès'})
if __name__ == "__main__":
    app.run(host="localhost", port=5000)
