from flask import Flask, request, jsonify
import main
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    if request.method == 'POST':
        # קבלת הנתונים מהבקשה שהתקבלה מהקליינט
        data = request.json
        
        # הוספת הלקוח למסד הנתונים
        conn = main.conn
        if conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO customers (name, last_name, email, phone, address) VALUES (%s, %s, %s, %s, %s)', (data['name'], data['last_name'], data['email'], data['phone'], data['address']))
            conn.commit()
            conn.close()
            return jsonify({"message": "Customer added successfully"}), 200
        else:
            return jsonify({"error": "Failed to connect to database"}), 500

if __name__ == '__main__':
    app.run(debug=True)
