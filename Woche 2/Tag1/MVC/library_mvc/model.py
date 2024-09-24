# Der Bibliothekar, der die Bücher kennt und diese zurückgibt
def get_book():
    return "In 80 Tagen um die Welt"


def get_book_titles(data):
    print("Model: Extracting book titles")
    book_titles = []
    # Hier extrahieren wir die Bücher aus dem API Request
    for book in data:
        title = book["title"]
        book_titles.append(title)

    return book_titles
