from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string if needed
db = client['order_database']  # Replace 'order_database' with your database name
orders_collection = db['orders']  # Replace 'orders' with your collection name

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = orders_collection.find_one({"id": order_id})
    if order:
        order.pop('_id')  # Remove MongoDB's internal ID field for cleaner output
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(port=5001)
