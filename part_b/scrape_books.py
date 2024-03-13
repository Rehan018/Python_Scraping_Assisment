import requests
from bs4 import BeautifulSoup
from part_b.database import PartBDatabase, connect_to_mongodb

def scrape_books_data():
    base_url = "http://books.toscrape.com"
    books_url = base_url + "/catalogue/page-{}.html"

    # Initialize the database
    db_instance = PartBDatabase()

    # Iterate through all 50 pages
    for page_num in range(1, 50):
        page_url = books_url.format(page_num)
        response = requests.get(page_url)
        if response.status_code == 200:
            page_content = response.content
            soup = BeautifulSoup(page_content, 'html.parser')

            books = soup.find_all('article', class_='product_pod')
            for book in books:
                title = book.find('h3').a.get('title')
                price = float(book.find('p', class_='price_color').get_text().strip('£'))
                availability = book.find('p', class_='instock availability').get_text().strip()
                rating_classes = book.find('p', class_='star-rating')['class']
                rating = rating_classes[1]
                rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
                rating_value = rating_map.get(rating, None)

                # Construct a dictionary for the book data
                book_data = {
                    'title': title,
                    'price': price,
                    'availability': availability,
                    'rating': rating_value
                }
                # Insert the book data into the database
                db_instance.insert_book(book_data)
        else:
            print(f"Failed to fetch page {page_num}")
    # Close database connection
    db_instance.client.close()

if __name__ == "__main__":
    scrape_books_data()
