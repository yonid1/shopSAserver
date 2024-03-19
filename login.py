from flask import Flask, request, jsonify
import main
import jwt

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
        email = data['email']
        password = data['password']
        # בדוק התאמה של פרטי ההתחברות במסד הנתונים
        # אם הפרטים נכונים, צור והחזר טוקן
        # אם הפרטים אינם נכונים, החזר הודעת שגיאה רלוונטית

    else:
        return jsonify({"error": "Failed to connect to database"}), 500

# פונקציה ליצירת טוקן לאימות
def create_token(email):
    token = jwt.encode({'email': email}, app.config['SECRET_KEY'])
    return token

if __name__ == '__main__':
    app.run(debug=True)
