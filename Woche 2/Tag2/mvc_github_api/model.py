def extract_repo_names(repos):
    repo_names = []
    for repo in repos:
        name = repo["name"]
        repo_names.append(name)

    # Model sollte eigentlich die Daten in einer Datenbank speichern - Datenbank haben wir aber noch nicht
    return repo_names
