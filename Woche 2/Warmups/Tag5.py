"""
Scrape die Seite Python Jobs (https://pythonjobs.github.io/) und extrahiere die Job-Titel und das Erstellungsdatum.
Erstelle eine Klasse Job, die den Titel und das Erstellungsdatum speichern.
Gib eine Liste von Job-Objekten zurück, die auf der Seite zu finden sind
"""

from dataclasses import dataclass
from datetime import datetime

import requests
from bs4 import BeautifulSoup


@dataclass
class Job:
    title: str
    created: datetime


def scrape(url) -> list[Job]:
    jobs = []
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        format = "%a, %d %b %Y"

        job_elements = soup.find_all("div", class_="job")
        for job_element in job_elements:
            title = job_element.find("h1").text
            created_string = job_element.find(
                "i", class_="i-calendar"
            ).next_sibling.strip()

            created = datetime.strptime(created_string, format)
            job = Job(title, created)

            jobs.append(job)

        return jobs
    elif res.status_code == 404:
        raise Exception("Not Found!")
    else:
        raise Exception("An Unknown Error occurred")


url = "https://pythonjobs.github.io/"
jobs = scrape(url)


for job in jobs:
    print(job)
