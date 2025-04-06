from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string if needed
db = client['user_database']  # Replace 'user_database' with your database name
users_collection = db['users']  # Replace 'users' with your collection name

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({"id": user_id})
    if user:
        user.pop('_id')  # Remove MongoDB's internal ID field for cleaner output
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
