from flask import Flask, request, jsonify
import main
import jwt
from bcrypt import checkpw

app = Flask(__name__)
 
# ניתן להגדיר מפתח סודי לטוקן
app.config['SECRET_KEY'] = 'your_secret_key'

def register():
    conn = main.conn
    if conn:
        data = request.get_json()
        email = data['email']
        password = data['password']
        # צור פונקציה שבודקת האם האימייל כבר קיים במסד הנתונים
        # אם כן, החזר שגיאה או קוד הסטטוס מתאים

        # אם האימייל אינו קיים, הוסף את המשתמש החדש למסד הנתונים ואמת אותו
        # שלח הודעת JSON עם אישור ההרשמה או הודעת שגיאה במידה והרשמת המשתמש נכשלה

    else:
        return jsonify({"error": "Failed to connect to database"}), 500

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
    token = jwt.encode({'email': email}, app.config['SECRET_KEY'])
    return token

if __name__ == '__main__':
    app.run(debug=True)
