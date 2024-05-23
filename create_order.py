from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import Product, Customer, Order, OrderProduct,db
from loguru import logger
import main

# הגדרת הלוגר לכתוב לקובץ "app.log"
logger.add("app.log", level="DEBUG")

# פונקציה ליצירת הזמנה
def create_order():
    data = request.json
    id_customer = data.get('id_customer')
    products = data.get('products')

    if not id_customer or not products:
        return jsonify({"error": "Invalid data"}), 400

    try:
        new_order = Order(
            time_order=datetime.now(),
            status='Pending',
            id_customer=id_customer
        )
        db.session.add(new_order)
        logger.debug('Order created successfully')
        db.session.flush()

        for product in products:
            product_id = product['id']
            quantity = product['quantity']

            order_product = OrderProduct(
                order_id=new_order.id,
                product_id=product_id,
                quantity=quantity
            )
            db.session.add(order_product)

        db.session.commit()
        return jsonify({"message": "Order created successfully", "order_id": new_order.id}), 201
    except Exception as e:
        db.session.rollback()
        logger.exception(f"Error creating order: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    db.create_all()
    main.app.run(debug=True)
