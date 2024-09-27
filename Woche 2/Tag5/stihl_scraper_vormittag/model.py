from dataclasses import dataclass
from typing import Optional

from bs4 import BeautifulSoup
from sqlmodel import Field, SQLModel, create_engine, select

# TODO: Database anbinden
engine = None


@dataclass
class ProductCategory:
    category: str
    path: str


# So war das voher
# @dataclass
# class Product:
#     name: str
#     price: float
#     short_description: str
#     available: bool
#     review: float


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    short_description: str
    available: bool


def initialize_db():
    global engine
    engine = create_engine("sqlite:///./stihl-products.db")
    SQLModel.metadata.create_all(engine)


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


@dataclass
class Product:
    name: str
    price: float
    short_description: str
    available: bool
    review: float


def extract_product_details(soup: BeautifulSoup) -> list[dict]:
    # webscraping magic
    global engine

    # 1. Auf wichtiges Element referenzieren
    grid = soup.find("div", class_="m_category-overview-tiles__products")
    products = grid.find_all("a")

    if not engine:
        raise Exception("No Engine for DB found")

    # 2. Alle Informationen aus dem Element extrahieren
    product_details = []
    for product in products:
        # produktname
        name = product.find("span", class_="tile_product-standard__title-inner").text
        # preis
        price = product.find("span", attrs={"data-test-id": "product-buy-price"}).text
        print(price)  # TODO: konvertiere zu float

        # short description
        short_description = product.find(
            "div", class_="tile_product-standard__subline"
        ).text
        # auf lager
        available = (
            product.find("div", class_="tile_product-standard__status").text
            == "Auf Lager"
        )
        # bewertung
        tile = product.find("div", class_="tile_product-standard__title")
        bv_container = tile.find(
            "div", class_="bv_main_container bv_hover bv_inline_rating_container_left"
        )

        review = None
        print(review)
        # TODO: Produktklasse erstellen
        # TODO: product_details append

    # returns list of product details: {'product': 'product_name', 'price': 'product_price', ...}
    return product_details
