import controller

if __name__ == "__main__":

    # Anforderungen an die API:
    # 1. Alle Repositories eines Users auslesen
    # 2. Neues Repository anlegen

    # Wie unterscheiden wir die beiden Anforderungen?
    # User Input - Selbst schreiben:
    # 1. "auslesen"
    # 2. "anlegen"
    input_text = input("Was möchtest du mit der API tun?\n")

    while input_text != "auslesen" and input_text != "anlegen":
        print("Ungültige Eingabe, probier nochmal...")
        input_text = input("Was möchtest du mit der API tun?\n")

    # Zusatz: Welcher User?
    input_username = input("Für welchen User möchtest du die Aktion ausführen?\n")

    if input_text == "auslesen":
        # controller soll alle repositories auslesen
        controller.get_user_repos(input_username)

    elif input_text == "anlegen":
        # Zusatz: Repo Name?
        input_repo_name = input("Wie soll das neue Repository heißen?\n")

        # controller soll neues repository anlegen
        controller.create_repo(input_username, input_repo_name)
