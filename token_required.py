from functools import wraps
from flask import request, jsonify
import jwt
import os
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        print("token: %s" % token)
        if not token:

            return jsonify({"error": "Token is missing"}), 401

        try:
            payload = jwt.decode(token,os.getenv('SECRET_KEY'), algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        
        return f(*args, **kwargs)
    
    return decorated_function
