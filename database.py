import os
from datetime import datetime

from pymongo import MongoClient

# Connect to MongoDB Atlas
try:
    mongodb_uri = os.getenv("MONGODB_URI")

    if not mongodb_uri:
        raise ValueError("MONGODB_URI is not set")

    client = MongoClient(mongodb_uri, serverSelectionTimeoutMS=5000)

    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully!")
    
# Create database and collection
    db = client["spam_classifier"]
    collection = db["predictions"]

except Exception as e:
    print("❌ MongoDB Connection Failed")
    print(e)
    collection = None


def save_prediction(message, cleaned, label, confidence):

    if collection is None:
        print("Database Not Connected")
        return

    record = {
        "message": message,
        "cleaned": cleaned,
        "label": label,
        "confidence": confidence,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    result = collection.insert_one(record)

    print("Inserted ID:", result.inserted_id)


def get_all_predictions():

    if collection is None:
        return []

    records = list(collection.find({}, {"_id": 0}))

    print("Found Records:", len(records))

    return records