# Die View stellt das Ergebnis in einer für den User lesbaren oder schönen Dartstellung dar
def print_book(book):
    print("View: Here is the book: " + book)


def print_books(book_titles):
    print("\n\nView: Here are the books:")
    # prints all books in the list
    for title in book_titles:
        print(title)
