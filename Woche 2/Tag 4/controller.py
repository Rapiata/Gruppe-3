from urllib.parse import urljoin

import model
import requests
import view
from bs4 import BeautifulSoup

BASE_URL = "https://www.stihl.de/de/"


def scrape_product_categories() -> list[dict]:
    # 1. request auf die startseite
    full_url = urljoin(BASE_URL, "geraete-werkzeuge")
    response = requests.get(full_url)

    if response.status_code == 200:
        # 2. soup erstellen
        soup = BeautifulSoup(response.text, "html.parser")
        # 3. model aufrufen - extrahiere produkt kategorien
        product_categories = model.extract_product_categories(soup)
        # 4. return produkt kategorien, weitergabe an zweiten schritt: scrape_products
        return product_categories
    else:
        raise Exception("Request failed, URL does not exist!")


def scrape_products(product_categories: list[dict]) -> None:
    # 1. request auf die dedizierte produktkategorie
    # 2. soup erstellen
    # 3. model aufrufen - extrahiere produktdetails
    # 4. view: produkte mit details darstellen

    pass

