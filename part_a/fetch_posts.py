import requests
from part_a.database import connect_to_mongodb

def fetch_posts_data(app_id):
    # Connect to MongoDB and get the database object
    db = connect_to_mongodb()

    # Fetch users from the users collection
    users_collection = db.users_collection  # Assuming the collection name is users_collection
    users = users_collection.find()

    for user in users:
        user_id = user["user_id"]
        api_url = f"https://dummyapi.io/data/v1/user/{user_id}/post"
        headers = {"app-id": app_id}

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            posts_data = response.json().get("data", [])
            for post in posts_data:
                print(post)
                post_data = {
                    "user_id": user_id,
                    "post_id": post.get("id", None),
                    "title": post.get("text", None),
                    "created_at": post.get("publishDate", None),
                    # Add more fields as needed
                }
                db.post_collection.insert_one(post_data)
                print(post_data)
        else:
            print(f"Failed to fetch posts data for user {user_id}")

    # Close database connection
    db.client.close()

if __name__ == "__main__":
    app_id = "65f1851fe5c046d508037541"
    fetch_posts_data(app_id)
