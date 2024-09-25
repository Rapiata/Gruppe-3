import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://realpython.github.io/fake-jobs/"


## Schreibe die Ergebnisse in eine CSV Datei
## Erstelle dazu ein Objekt, dass die Daten in Python ordentlich ablegt


# Andere Möglichkeit: Wir erstellen eine Klasse, die die Daten speichert - ein einfaches Objekt reicht aber auch in diesem Fall
# class Job:
#     def __init__(self, title, subtitle, location, date):
#         self.title = title
#         self.subtitle = subtitle
#         self.location = location
#         self.date = date


def extract_jobs(soup):
    jobs = []
    job_elements = soup.find_all("div", class_="card")

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title is-5")
        title = title_element.text

        subtitle_element = job_element.find("h3", class_="subtitle is-6 company")
        subtitle = subtitle_element.text

        location_element = job_element.find("p", class_="location")
        location = location_element.text

        date_element = job_element.find("time")
        date = date_element.text

        job = {
            "title": title,
            "subtitle": subtitle,
            "location": location,
            "date": date,
        }

        jobs.append(job)

    return jobs


""" Auftrag ist: die Stellenangebote aus der Webseite zu extrahieren. 
    1. Extrahiere die Titel der Jobangebote
    2. Untertitel
    3. Ort
    4. Datum
    5. Erstelle eine Liste mit Objekt, die die Daten speichert

    6. Erstelle ein CSV aus den Daten
"""
# Wir holen uns die Webdaten mit requests
response = requests.get(BASE_URL)

# Wir erstellen ein BeautifulSoup Objekt
soup = BeautifulSoup(response.text, "html.parser")

# Wir extrahieren die Daten aus der Soup
jobs = extract_jobs(soup)

# Wir erstellen ein CSV aus den Daten
df = pd.DataFrame([job for job in jobs])
df.to_csv("jobs.csv", index=False)
