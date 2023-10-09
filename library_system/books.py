library_books = {}

def add_book(title, author):

    book = {
    'title': title,
    'author': Author
}
    library_books.append(book)


def borrow_book(title):
    for book in library_books:
        if book('title') == title and book('availibility'):
            book('availibility')== False
    return True

def return_book(title):
    for book in library_books:
        if book('title') == title and book('availibility'):
            book('availibility') == True
    return False

def find_book(title):
        for title in library_books:
            if title == 'title':
                return_book('title')
