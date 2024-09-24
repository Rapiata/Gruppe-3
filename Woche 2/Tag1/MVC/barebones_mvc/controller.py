import model
import view


# User Request kommt rein, Controller muss diesen Request aufnehmen und verarbeiten.
def delegate_request(request):
    if request == "User asks for a book":
        print("Controller: User request received")

        # Controller muss Model fragen: "Hast du ein Buch?"
        book = model.get_book()

        # Der Conroller delegiert die Antwort an die View
        view.print_book(book)

    else:
        print("Controller: I don't understand the request: " + request)
