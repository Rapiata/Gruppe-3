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

        # view zeigt die Daten an
        view.output_repo_names(repo_names)

    else:
        # view generiert einen Error
        view.output_error(
            "GET /users/{username}/repos, status code:" + str(response.status_code)
        )


def create_repo(username, repo_name):
    response = requests.post(
        BASE_URL + f"/user/repos",
        json={"name": repo_name},
        auth=(
            username,
            GITHUB_TOKEN,
        ),  # Basic Auth - Ganz wichtig, da die meisten APIs nicht ohne Authentifizierung funktionieren
    )
    if response.status_code == 201:
        data = response.json()
        # model speichert die neuen Daten / extrahiert die daten
        repo_name = model.extract_repo_names([data])
        # view zeigt eine Erfolgsnachricht an
        view.output_repo_created(repo_name[0])
    else:
        # view generiert einen Error
        view.output_error("POST /user/repos, status code:" + str(response.status_code))
