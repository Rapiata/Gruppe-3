"""
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

import refrom dataclasses import dataclassfrom bs4 import BeautifulSoupfrom db import Product, create_products@dataclassclass ProductCategory:    category: str    path: strdef extract_product_categories(soup: BeautifulSoup) -> list[ProductCategory]:    # webscraping magic    # 1. Auf wichtiges Element referenzieren    grid = soup.find("div", class_="categorygrid grid section")    product_elements = grid.find_all("a")    # 2. Alle Informationen aus dem Element extrahieren    product_categories = []    for product_element in product_elements:        product_link = product_element["href"]        product_name = product_element.text        product_category = ProductCategory(category=product_name, path=product_link)        product_categories.append(product_category)    # returns list of ProductCategory classes: {'category': 'category_name', 'url': 'category_url'}    return product_categoriesdef extract_product_details(soup: BeautifulSoup) -> bool:    # webscraping magic    # 1. Auf wichtiges Element referenzieren    grid = soup.find("div", class_="m_category-overview-tiles__products")    products = grid.find_all("a")    # 2. Alle Informationen aus dem Element extrahieren    product_details = []    for product in products:        # produktname        name = product.find("span", class_="tile_product-standard__title-inner").text        # preis        price_string = product.find(            "span", attrs={"data-test-id": "product-buy-price"}        ).text        price_extracted = re.search(r"\d+,\d{0,2}", price_string).group(0)        price = float(price_extracted.replace(",", "."))        # short description        short_description = product.find(            "div", class_="tile_product-standard__subline"        ).text        # auf lager        available = (            product.find("div", class_="tile_product-standard__status").text            == "Auf Lager"        )        # Produktklasse erstellen        product = Product(            name=name,            price=price,            short_description=short_description,            available=available,        )        # product_details append        product_details.append(product)    # CREATE - Operation in DB    create_products(product_details)    # returns list of product details: {'product': 'product_name', 'price': 'product_price', ...}    return True 
       
      

