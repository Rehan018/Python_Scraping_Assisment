import requests
from part_a.database import connect_to_mongodb

def fetch_users_data(app_id):
    api_url = "https://dummyapi.io/data/v1/user"
    headers = {"app-id": app_id}

    # Connect to MongoDB and get the database object
    db = connect_to_mongodb()

    # Fetch users data
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        users_data = response.json().get("data", [])
        for user in users_data:
            # Print user data to inspect the structure
            print(user)
            
            # Extract user data
            user_id = user.get("id", None)
            full_name = f"{user.get('firstName', '')} {user.get('lastName', '')}"
            email = user.get("email", None)
            
            # Ensure user_id and full_name are not None
            if user_id is not None and full_name.strip() != "":
                user_data = {"user_id": user_id, "full_name": full_name.strip(), "email": email}
                db.posts_collection.insert_one(user_data)
    else:
        print("Failed to fetch users data")

    # Close database connection
    db.client.close()

if __name__ == "__main__":
    app_id = "65f1851fe5c046d508037541"
    fetch_users_data(app_id)
