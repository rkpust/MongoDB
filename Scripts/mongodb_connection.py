from pymongo import MongoClient

# MongoDB connection URI
uri = "mongodb://localhost:27017"

# Connect to MongoDB
client = MongoClient(uri)

try:
    # Verify the connection
    client.admin.command("ping")
    print("Successfully connected to MongoDB!")

    # Select a database
    db = client["TestDB"]

    # Select a collection
    collection = db["users"]

    print("Database:", db.name)
    print("Collection:", collection.name)

except Exception as e:
    print("Connection failed:", e)

finally:
    client.close()