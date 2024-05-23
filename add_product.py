from flask import Flask, jsonify, request
from models import db, Product

app = Flask(__name__)

def add_product():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    category = data.get('category')
    image = data.get('image')

    if not all([name, price, category, image]):
        return jsonify({"error": "Please fill in all fields"}), 400

    try:
        new_product = Product(
            name=name,
            price=price,
            category=category,
            image=image
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully", "product_id": new_product.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
