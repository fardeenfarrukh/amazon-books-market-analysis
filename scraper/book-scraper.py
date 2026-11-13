import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

# Website URL
base_url = "https://books.toscrape.com/"
category_urls = [
    "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
    "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html",
    "https://books.toscrape.com/catalogue/category/books/classics_6/index.html"
]
category_names = [
    "Travel",
    "Mystery",
    "Historical Fiction",
    "Sequential Art",
    "Classics"
]

def collect_book_urls(category_url):
    book_urls = []
    current_page_url = category_url

    while current_page_url:
        page_response = requests.get(current_page_url)
        page_response.raise_for_status()
        page_response.encoding = 'utf-8'
        page_soup = BeautifulSoup(page_response.text, "html.parser")
        
        for link in page_soup.select("article.product_pod h3 a"):
            book_urls.append(urljoin(current_page_url, link["href"]))

        next_page = page_soup.select_one("li.next a")
        current_page_url = urljoin(current_page_url, next_page["href"]) if next_page else None
    
    return book_urls

def extract_book_details(book_url):
    page_response = requests.get(book_url)
    page_response.raise_for_status()
    page_response.encoding = 'utf-8'
    page_soup = BeautifulSoup(page_response.text, "html.parser")

    product_table = page_soup.find("table", class_="table")
    book_details = {}

    for row in product_table.find_all("tr"):
        key = row.find("th").text.strip()
        value = row.find("td").text.strip()
        book_details[key] = value

    book_details["BookTitle"] = page_soup.find("h1").text.strip()
    description_section = page_soup.find("div", id="product_description")
    book_description = description_section.find_next("p").get_text(" ", strip=True) if description_section else ""
    book_details["BookDescription"] = book_description
    book_details["BookRating"] = page_soup.find("p", class_="star-rating")["class"][1]
    book_details["ProductURL"] = book_url

    return book_details

all_book_urls = []
book_categories = {}

for category_url, category_name in zip(category_urls, category_names):
    book_urls = collect_book_urls(category_url)
    all_book_urls.extend(book_urls)

    for book_url in book_urls:
        book_categories[book_url] = category_name

print("Total book URLs:", len(all_book_urls))

all_books = []

for book_url in all_book_urls:
    try:
        book_details = extract_book_details(book_url)
        book_details["BookCategory"] = book_categories[book_url]
        all_books.append(book_details)
        print("Scraped:", book_details["BookTitle"])
    except Exception as error:
        print("Failed:" , book_url, error)
print("Successfully scraped:", len(all_books))

df = pd.DataFrame(all_books)
df.to_csv("data/raw/books_raw.csv", index=False, encoding="utf-8-sig")

print("Raw dataset saved successfully!")