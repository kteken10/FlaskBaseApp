import os
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, session, jsonify, url_for,request
from flask_cors import CORS
from models import db, Product
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

@app.route("/users")
def get_user_infos():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    user = session.get("user")
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not authenticated"})


## GESTION DES UTILISATEUR

# Route pour récupérer tous les produits
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = []
    for product in products:
        product_data = {
            'name': product.name,
            'price': product.price
        }
        result.append(product_data)
    return jsonify(result)

# Route pour ajouter un produit
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')

    if not name or not price:
        return jsonify({'error': 'Tous les champs sont obligatoires'}), 400

    product = Product(name=name, price=price)
    db.session.add(product)
    db.session.commit()

    return jsonify({'message': 'Le produit a été ajouté avec succès'}), 201

# Route pour mettre à jour un produit
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Produit non trouvé'}), 404

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')

    if not name or not price:
        return jsonify({'error': 'Tous les champs sont obligatoires'}), 400

    product.name = name
    product.price = price
    db.session.commit()

    return jsonify({'message': 'Le produit a été mis à jour avec succès'})

# Route pour supprikmer un produit
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Produit non trouvé'}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Le produit a été supprimé avec succès'})

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
