from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
 
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

def authenticate_token():
    
    # Extract the token from the request
    token = request.headers.get('Authorization')
    print ('authenticate_token',token)
    if not token:
        return jsonify({"error": "Token is missing"}), 401

    try:
        # Decode the token and verify its signature
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        # You can perform additional checks on the payload here if needed

        # If verification is successful, return a success message
        return jsonify({"message": "Token is valid"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(debug=True)