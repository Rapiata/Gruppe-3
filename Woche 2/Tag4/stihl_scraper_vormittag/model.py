from dataclasses import dataclass

from bs4 import BeautifulSoup


@dataclass
class ProductCategory:
    category: str
    path: str


def extract_product_categories(soup: BeautifulSoup) -> list[dict]:
    # webscraping magic
    grid = soup.find("div", class_="categorygrid grid section")
    product_elements = grid.find_all("a")
    product_categories = []

    for product_element in product_elements:
        product_link = product_element["href"]
        product_name = product_element.text

        product_category = ProductCategory(category=product_name, path=product_link)
        product_categories.append(product_category)
    # returns list of product categories: {'category': 'category_name', 'url': 'category_url'}

    return product_categories


def extract_product_details(soup) -> list[dict]:
    # webscraping magic
    # returns list of product details: {'product': 'product_name', 'price': 'product_price', ...}
    pass
