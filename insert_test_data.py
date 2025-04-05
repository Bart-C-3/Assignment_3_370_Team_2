from pymongo import MongoClient

# MongoDB connection setup
mongo_uri = 'mongodb://localhost:27017/'
db_name = 'microservices_db'
client = MongoClient(mongo_uri)
db = client[db_name]
data_collection = db['data']

# Insert test data
data_collection.insert_many([
    {"id": "1", "type": "user", "name": "Alice"},
    {"id": "2", "type": "user", "name": "Bob"},
    {"id": "1001", "type": "product", "name": "Laptop", "price": 1000},
    {"id": "1002", "type": "product", "name": "Phone", "price": 500},
    {"id": "1003", "type": "product", "name": "Tablet", "price": 300},
    {"order_id": "101", "type": "order", "user_id": "1", "product_id": "1001"},
    {"order_id": "102", "type": "order", "user_id": "1", "product_id": "1002"},
    {"order_id": "103", "type": "order", "user_id": "2", "product_id": "1003"}
])

print("Test data inserted successfully.")