from pymongo import MongoClient

class PartBDatabase:
    def __init__(self):
        self.client, self.db = connect_to_mongodb()
        self.books_collection = self.db['books']

    def insert_book(self, book_data):
        self.books_collection.insert_one({
            'title': book_data['title'],
            'price': book_data['price'],
            'availability': book_data['availability'],
            'rating': book_data['rating']
        })

def connect_to_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['bookstore']
    return client, db
