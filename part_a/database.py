import pymongo

def connect_to_mongodb():
    mongo_uri = "mongodb://localhost:27017/bookstore"
    client = pymongo.MongoClient(mongo_uri)

    # Access the database
    db = client.get_database()

    return db
