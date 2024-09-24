import model
import requests
import view

base_url = "https://postman-library-api.glitch.me"


# User Request kommt rein, Controller muss diesen Request aufnehmen und verarbeiten.
def delegate_request(request):
    if request == "I want a list of all book titles":
        print("Controller: User request received")

        # Controller macht einen API request an die externe Library API
        # GET request /books
        response = requests.get(base_url + "/books")
        # wir bekommen einen response zurück, den geben wir an das Model weiter
        data = response.json()

        # Controller fragt Model, alle Titel zu extrahieren
        # Dafür werden die Daten aus dem API Request an das Model übergeben
        book_titles = model.get_book_titles(data)

        # Der Conroller delegiert die Antwort an die View
        view.print_books(book_titles)

    else:
        print("Controller: I don't understand the request: " + request)
