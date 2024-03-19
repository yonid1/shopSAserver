import pymysql


host = 'localhost'
user = 'root'
password = '123456'
database = 'MyStore'

try:
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connected successfully!")
except pymysql.Error as e:
    print(f"Connection failed: {e}")

