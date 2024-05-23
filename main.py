from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/MyStore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

host = 'localhost'
user = 'root'
password = '123456'
database = 'MyStore'

with app.app_context():
    db.create_all()


# try:
#     conn = pymysql.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )
#     print("Connected successfully!")
# except pymysql.Error as e:
#     print(f"Connection failed: {e}")

if __name__ == "__main__":
    app.run(debug=True)
