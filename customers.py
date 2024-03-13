import main
import connection
import pymysql.cursors


cursor = main.conn.cursor()

customers=[
    ('yoni','Danino','yontand@gmai.com',527683170,'ashdod'),
    ('Moshe','azriel','moshe3510@gmail.com',507689513,'netivot')
]

for customer in customers:
    cursor.execute('INSERT INTO customers (name, last_name, email, phone, address) VALUES (%s,%s,%s,%s,%s)',customer)
cursor.execute('SELECT * FROM customers')
print(cursor.fetchall())

main.conn.commit()
main.conn.close()
