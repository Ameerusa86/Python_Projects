from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import os


def scrape_books():
    url = "http://books.toscrape.com"

    chrome_options = Options()
    chrome_options.add_argument(
        "--headless"
    )  # Run headless Chrome for better performance
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    books = []

    while True:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for book in soup.select(".product_pod"):
            title = book.h3.a["title"]
            price = book.select_one(".price_color").text
            availability = book.select_one(".availability").text.strip()
            books.append({"title": title, "price": price, "availability": availability})

        next_button = soup.select_one(".next a")
        if next_button:
            next_page_url = next_button["href"]
            if "catalogue/" in next_page_url:
                next_page_url = next_page_url.replace("catalogue/", "")
            driver.get(f"{url}/{next_page_url}")
            time.sleep(3)
        else:
            break

    driver.quit()

    if not os.path.exists("data"):
        os.makedirs("data")

    df = pd.DataFrame(books)
    df.to_csv("data/books.csv", index=False)
    print("Scraping completed and data saved to data/books.csv")


if __name__ == "__main__":
    scrape_books()
