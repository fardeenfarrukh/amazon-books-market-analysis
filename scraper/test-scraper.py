import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)

product_table = soup.find("table", class_="table")
print(product_table)

book_data = {}
for row in product_table.find_all("tr"):
    key = row.find("th").text.strip()
    value = row.find("td").text.strip()
    book_data[key] = value
    
book_data["BookTitle"] = soup.find("h1").text.strip()
book_data["BookDescription"] = soup.find("div", id="product_description").find_next("p").text.strip()
book_data["BookRating"] = soup.find("p", class_="star-rating")["class"][1]
    
print(book_data)
