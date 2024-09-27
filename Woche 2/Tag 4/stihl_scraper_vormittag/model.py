from dataclasses import dataclass

from bs4 import BeautifulSoup


@dataclass
class ProductCategory:
    category: str
    path: str


def extract_product_categories(soup: BeautifulSoup) -> list[ProductCategory]:
    # webscraping magic

    # 1. Auf wichtiges Element referenzieren
    grid = soup.find("div", class_="categorygrid grid section")
    product_elements = grid.find_all("a")

    # 2. Alle Informationen aus dem Element extrahieren
    product_categories = []
    for product_element in product_elements:
        product_link = product_element["href"]
        product_name = product_element.text

        product_category = ProductCategory(category=product_name, path=product_link)
        product_categories.append(product_category)

    # returns list of ProductCategory classes: {'category': 'category_name', 'url': 'category_url'}
    return product_categories


def extract_product_details(soup: BeautifulSoup) -> list[dict]:
    # webscraping magic

    # 1. Auf wichtiges Element referenzieren
    grid = soup.find("div", class_="m_category-overview-tiles__products")
    products = grid.find_all("a")

    # 2. Alle Informationen aus dem Element extrahieren
    product_details = []
    for product in products:
        pass

    # returns list of product details: {'product': 'product_name', 'price': 'product_price', ...}
    return product_details