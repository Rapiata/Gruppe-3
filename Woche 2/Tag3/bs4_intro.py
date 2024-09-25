import requests
from bs4 import BeautifulSoup

BASE_URL = "https://realpython.github.io/fake-jobs/"
response = requests.get(BASE_URL)


""" Auftrag ist: die Stellenangebote aus der Webseite zu extrahieren. 
    1. Extrahiere die Titel der Jobangebote
    2. ...
"""


# Wir erstellen ein BeautifulSoup Objekt
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h2", class_="title is-5")
for title in titles:
    print(title.text)
