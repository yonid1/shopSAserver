from flask import Flask, request, jsonify
import main
import jwt
from bcrypt import checkpw
import bcrypt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

app = Flask(__name__)
 
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def hash_password(password):

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def register():
    conn = main.conn
    if conn:
        try:
            data = request.json
            email = data.get('email')
            # Assuming we still want to hash the password before storing
            password = hash_password(data.get('password'))
            name = data.get('firstName')
            last_name = data.get('lastName')
            address = data.get('address')
            phone = data.get('phone')
            print("Received email:", email) 
            # Simple validation for all fields
            if not all([email, password, name, last_name, address, phone]):
                print(email, password, name, last_name, address, phone)
                return jsonify({"error": "Please fill in all fields"}), 401

            cursor = conn.cursor()
            cursor.execute('SELECT * FROM customers WHERE email = %s', (email,))
            existing_user = cursor.fetchone()
            print("Existing user:", existing_user) 
            if existing_user:
             return jsonify({"error": "Email already exists"}), 400

            
            cursor.execute('INSERT INTO customers (email, password, name, last_name, address, phone) VALUES (%s, %s, %s, %s, %s, %s)', 
                           (email, password, name, last_name, address, phone))
            conn.commit()
            token = create_token(email)
            print("token",token)
            return jsonify({'token': token})
            # return jsonify({"message": "User registered successfully"}), 201
        except Exception as e:
            print(f"Error during registration: {e}")
            return jsonify({"error": "Failed to register user", "details": str(e)}), 500
    else:
        return jsonify({"error": "Failed to connect to the database"}), 500

def login():
    conn = main.conn
    if conn:
        data = request.get_json()
        if 'email' not in data or 'password' not in data:
            return jsonify({"error": "Missing email or password in request"}), 400
        
        email = data['email']
        password = data['password']
        
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE email = %s', (email))
        user = cursor.fetchone()
        print(user)
        if not user:
            return jsonify({"error": "User not found"}), 404

        if not checkpw(password.encode('utf-8'), user[6].encode('utf-8')):
            return jsonify({"error": "Invalid email or password"}), 401

        token = create_token(email)
        print("token",token)
        return jsonify({'token': token})

    else:
        return jsonify({"error": "Failed to connect to database"}), 500
# פונקציה ליצירת טוקן לאימות
def create_token(email):
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {'email': email, 'exp': expiration_time}
    token = jwt.encode(payload, SECRET_KEY)
    return token

if __name__ == '__main__':
    app.run(debug=True)
