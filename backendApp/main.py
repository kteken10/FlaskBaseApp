from flask import Flask, jsonify, request
from models import db, Product
from config import config

app = Flask(__name__)

# Configuration de l'application Flask
env = 'development'  # Mettez ici votre environnement ('development' ou 'production')
app.config.from_object(config[env])
db.init_app(app)

# Création des tables
with app.app_context():
    db.create_all()

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

# Route pour supprimer un produit
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Produit non trouvé'}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Le produit a été supprimé avec succès'})

if __name__ == '__main__':
    app.run()

