import os
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
db_name = os.getenv('MONGO_DB_NAME', 'microservices_db')
client = MongoClient(mongo_uri)
db = client[db_name]
data_collection = db['data']

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_collection.find_one({"id": user_id, "type": "user"}, {"_id": 0})  # Filter by type 'user'
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
