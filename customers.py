import bcrypt
import main
import connection
import pymysql.cursors

cursor = main.conn.cursor()

# פונקציה להצפנת הסיסמה
def hash_password(password):
    # מקבלים את הסיסמה ומחזירים אותה מוצפנת
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

customers = [
    ('yoni', 'Danino', 'yontand@gmail.com', 527683170, 'ashdod', hash_password('123456')),
    ('Moshe', 'azriel', 'moshe3510@gmail.com', 507689513, 'netivot', hash_password('654321'))
]

for customer in customers:
    cursor.execute('INSERT INTO customers (name, last_name, email, phone, address, password) VALUES (%s,%s,%s,%s,%s,%s)', customer)

cursor.execute('SELECT * FROM customers')
print(cursor.fetchall())

main.conn.commit()
main.conn.close()
