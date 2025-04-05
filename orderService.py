from flask import Flask, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['microservices_db']
data_collection = db['data']

@app.route('/orders', methods=['GET'])
def get_orders_by_user():
    user_id = request.args.get('user_id')
    user_orders = list(data_collection.find({"user_id": user_id, "type": "order"}, {"_id": 0}))  # Ensure correct query
    return jsonify(user_orders)

@app.route('/orders/all', methods=['GET'])
def get_all_orders():
    all_orders = list(data_collection.find({"type": "order"}, {"_id": 0}))  # Fetch all orders
    return jsonify(all_orders)

if __name__ == '__main__':
    app.run(port=5001)
