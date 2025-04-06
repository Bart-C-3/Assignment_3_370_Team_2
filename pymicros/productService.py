from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string if needed
db = client['product_database']  # Replace 'product_database' with your database name
products_collection = db['products']  # Replace 'products' with your collection name

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products_collection.find_one({"id": product_id})
    if product:
        product.pop('_id')  # Remove MongoDB's internal ID field for cleaner output
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(port=5002)
