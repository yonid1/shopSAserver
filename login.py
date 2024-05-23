from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import main
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
from models import db, Customer

app = Flask(__name__)
 
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def hash_password(password):
    return generate_password_hash(password)

def register():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')
        hashed_password = hash_password(password)
        name = data.get('firstName')
        last_name = data.get('lastName')
        address = data.get('address')
        phone = data.get('phone')
        
        print(f"Registering user: {email}")
        print(f"Hashed password: {hashed_password}")

        if not all([email, hashed_password, name, last_name, address, phone]):
            return jsonify({"error": "Please fill in all fields"}), 401

        existing_user = Customer.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "Email already exists"}), 400
        
        new_customer = Customer(
            email=email,
            password=hashed_password,
            name=name,
            last_name=last_name,
            address=address,
            phone=phone
        )
        db.session.add(new_customer)
        db.session.commit()

        user_data = {
            'id': new_customer.id,
            'name': new_customer.name,
            'last_name': new_customer.last_name,
            'email': new_customer.email,
            'phone': new_customer.phone,
            'address': new_customer.address
        }
        print('userdata--- ',new_customer.id)
        token = create_token(email)
        return jsonify({'token': token,'userName':new_customer.name,'id_customer':new_customer.id}),200

    except Exception as e:
        print(f"Error during registration: {e}")
        return jsonify({"error": "Failed to register user", "details": str(e)}), 500


def login():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        
        user = Customer.query.filter_by(email=email).first()
        
        print(f"Login attempt for user: {email}")
        
        if user:
            print(f"User found: {user.email}, Hashed password: {user.password}")
            if check_password_hash(user.password, password):
                token = create_token(email)
                return jsonify({'token': token, 'id_customer': user.id, 'name': user.name})
            else:
                print("Invalid password")
                return jsonify({"error": "Invalid email or password"}), 401
        else:
            print("User not found")
            return jsonify({"error": "User not found"}), 404

    except Exception as e:
        print(f"Error during login: {e}")
        return jsonify({"error": f"Failed to login: {e}"}), 500

def create_token(email):
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {'email': email, 'exp': expiration_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

if __name__ == '__main__':
    app.run(debug=True)
