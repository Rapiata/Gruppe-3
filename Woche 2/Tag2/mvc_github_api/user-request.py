import controller

if __name__ == "__main__":
    print("Hello World")

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

    if input_text == "auslesen":
        # controller soll alle repositories auslesen
        pass
    elif input_text == "anlegen":
        # controller soll neues repository anlegen
        pass
