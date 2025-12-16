import requests
from bs4 import BeautifulSoup

def scrape_products():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    for book in soup.select(".product_pod")[:3]:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        products.append({
            "title": title,
            "price": price
        })
    return products
