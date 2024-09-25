import requests
from bs4 import BeautifulSoup

BASE_URL = "https://realpython.github.io/fake-jobs/"
response = requests.get(BASE_URL)


""" Auftrag ist: die Stellenangebote aus der Webseite zu extrahieren. 
    1. Extrahiere die Titel der Jobangebote
    2. Untertitel
    3. Ort
    4. Datum
"""


# Wir erstellen ein BeautifulSoup Objekt
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h2", class_="title is-5")
for title in titles:
    print(title.text)

# 2. Extrahiere die Untertitel der Jobangebote
subtitles = soup.find_all("h3", class_="subtitle is-6 company")
for subtitle in subtitles:
    print(subtitle.text)

# 3. Extrahiere die Orte der Jobangebote
locations = soup.find_all("p", class_="location")
for location in locations:
    print(location.text)

# 4. Extrahiere die Datum der Jobangebote
dates = soup.find_all("time")
for date in dates:
    print(date.text)
