from flask import Flask, jsonify
import main
import pymysql
from flask_cors import CORS
from login import login, register
from authToken import authenticate_token 
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/products', methods=['POST'])
def get_products():
    conn = main.conn
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        formatted_products = []
        for product in products:
            formatted_product = {
                "id": product[0],
                "name": product[1],
                "price": product[2],
                "category": product[3]
            }
            formatted_products.append(formatted_product)

        response = jsonify(formatted_products)
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        return response

    else:
        return jsonify({"error": "Failed to connect to the database"}), 500


@app.route('/customers')
def get_customers():
    conn = main.conn
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers')
        customers = cursor.fetchall()
        # conn.close()

        formatted_customers = []
        for customer in customers:
            formatted_customer = {
                'id': customer[0],
                'name': customer[1],
                'last_name': customer[2],
                'email': customer[3],
                'phone': customer[4],
                'address': customer[5]
            }
            formatted_customers.append(formatted_customer)

        response = jsonify(formatted_customers)
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        return response

    else:
        return jsonify({"error": "Failed to connect to database"}), 500

@app.route('/login', methods=['POST'])
def login_route():
    return login()

@app.route('/register', methods=['POST'])
def register_route():
    return register()

@app.route('/authenticate', methods=['POST'])
def authenticate_route():
    return authenticate_token()



if __name__ == '__main__':
    app.run(debug=True)
