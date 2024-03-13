# main.py

from part_a.fetch_users import fetch_users_data
from part_a.fetch_posts import fetch_posts_data
from part_b.scrape_books import scrape_books_data

def main():
    # Define your app_id
    app_id = "65f1851fe5c046d508037541"

    # Execute Part A
    fetch_users_data(app_id)
    fetch_posts_data(app_id)

    # Execute Part B
    scrape_books_data()

if __name__ == "__main__":
    main()
