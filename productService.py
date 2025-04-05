from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['microservices_db']
data_collection = db['data']

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = data_collection.find_one({"id": product_id, "type": "product"}, {"_id": 0})  # Ensure correct query
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/all', methods=['GET'])
def get_all_products():
    all_products = list(data_collection.find({"type": "product"}, {"_id": 0}))  # Fetch all products
    return jsonify(all_products)

if __name__ == '__main__': 
    app.run(port=5002)
