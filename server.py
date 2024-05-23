from flask import Flask, jsonify
import main
import pymysql
from flask_cors import CORS
from login import login, register
from authToken import authenticate_token 
from add_product import add_product
from token_required import token_required
from create_order import create_order
from models import Product , Customer,Order,OrderProduct

app = main.app
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/products', methods=['POST'])
def get_products():
    products = Product.query.all()
    formatted_products = []
    for product in products:
        formatted_product = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "category": product.category,
            "image": product.image
        }
        formatted_products.append(formatted_product)

    response = jsonify(formatted_products)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@app.route('/customers')
def get_customers():
    customers = Customer.query.all()
    formatted_customers = []
    for customer in customers:
        formatted_customer = {
            'id': customer.id,
            'name': customer.name,
            'last_name': customer.last_name,
            'email': customer.email,
            'phone': customer.phone,
            'address': customer.address
        }
        formatted_customers.append(formatted_customer)

    response = jsonify(formatted_customers)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

    

@app.route('/login', methods=['POST'])
def login_route():
    return login()

@app.route('/register', methods=['POST'])
def register_route():
    return register()

@app.route('/authenticate', methods=['POST'])
def authenticate_route():
    return authenticate_token()

@app.route('/add_product', methods=['POST'])
@token_required

def add_product_route():
    return add_product()   


@app.route('/create_order', methods=['POST'])
def create_order_route():
    return create_order()

if __name__ == '__main__':
    app.run(debug=True)
