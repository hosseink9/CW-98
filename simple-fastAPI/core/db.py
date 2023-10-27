from pymongo import MongoClient
# from pymongo import ASCENDING

client = MongoClient("mongodb://localhost:27017/")
print('🚀 Connected to MongoDB...')

db = client["fastapi"]
core_collection = db["library"]
users_collection = db["users"]

# Note = db.notes
# Note.create_index([("title", ASCENDING)], unique=True)
