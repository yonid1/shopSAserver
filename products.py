import main
import connection
import pymysql.cursors


cursor = main.conn.cursor()

# יצירת טבלה אם היא עדיין לא קיימת
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS products (
#         id INTEGER PRIMARY KEY AUTO_INCREMENT,
#         name TEXT NOT NULL,
#         price FLOAT NOT NULL,
#         category TEXT NOT NULL
#     )
# ''')

products = [
    ('knife', 25,'cookware'),
    ('laptop', 799,'pc'),
    ('tv', 599,'electronics')
]
# cursor.execute('DELETE FROM products')
# cursor.execute('ALTER TABLE products AUTO_INCREMENT = 1')

# הוספת כל מוצר לטבלה
for product in products:
    cursor.execute('INSERT INTO products (name, price,category) VALUES (%s, %s,%s)', product)


# ביצוע שאילתת SELECT והדפסת התוצאה
cursor.execute('SELECT * FROM products')
print(cursor.fetchall())

# שמירת השינויים וסגירת החיבור
main.conn.commit()
main.conn.close()
