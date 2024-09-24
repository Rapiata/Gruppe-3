import model
import requests
import view
from __init__ import BASE_URL, GITHUB_TOKEN


def get_user_repos(username):
    response = requests.get(BASE_URL + f"/users/{username}/repos")
    if response.status_code == 200:
        repos = response.json()
        # model speichert die Daten / extrahiert die daten
        repo_names = model.extract_repo_names(repos)

        # view...
    else:
        # view generiert einen Error
        print("Error")
        pass


def create_repo(username, repo_name):
    pass
