import main
import connection
import pymysql.cursors


cursor = main.conn.cursor()

# SQL command to create the products table
# create_products_table = """
# CREATE TABLE IF NOT EXISTS products (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     price DECIMAL(10, 2) NOT NULL,
#     category VARCHAR(255),
#     image VARCHAR(255)
# )
# """

# # SQL command to create the customers table
# create_customers_table = """
# CREATE TABLE IF NOT EXISTS customers (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     last_name VARCHAR(255) NOT NULL,
#     email VARCHAR(255) NOT NULL,
#     phone VARCHAR(15),
#     address VARCHAR(255),
#     password VARCHAR(255),
# )
# """

# # SQL command to create the orders table
# create_orders_table = """
# CREATE TABLE IF NOT EXISTS orders (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     time_order TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     status VARCHAR(50),
#     id_customer INT,
#     FOREIGN KEY (id_customer) REFERENCES customers(id)
# )
# """

# # SQL command to create the order_product table
# create_order_product_table = """
# CREATE TABLE IF NOT EXISTS order_product (
#     order_id INT,
#     product_id INT,
#     quantity INT,
#     PRIMARY KEY (order_id, product_id),
#     FOREIGN KEY (order_id) REFERENCES orders(id),
#     FOREIGN KEY (product_id) REFERENCES products(id)
# )
# """

# # Execute each SQL command
# try:
#     with conn.cursor() as cursor:
#         cursor.execute(create_products_table)
#         cursor.execute(create_customers_table)
#         cursor.execute(create_orders_table)
#         cursor.execute(create_order_product_table)
#     conn.commit()
#     print("Tables created successfully!")
# except pymysql.Error as e:
#     print(f"Error creating tables: {e}")
# finally:
#     conn.close()


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

for product in products:
    cursor.execute('INSERT INTO products (name, price,category) VALUES (%s, %s,%s)', product)


cursor.execute('SELECT * FROM products')
print(cursor.fetchall())

main.conn.commit()
main.conn.close()
