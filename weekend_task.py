# Library system using dictionaries and lists
library = []  # list to store all books


def add_book(book_id, title, author, **kwargs):
    """Add a new book to the library, supporting extra optional fields."""
    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    # Add any optional fields passed (like genre, year)
    for key, value in kwargs.items():
        book[key] = value
    
    library.append(book)
    return f"Book '{title}' added successfully!"


def search_books(*args):
    """Search books by title or author using multiple search keywords."""
    results = []
    for book in library:
        for term in args:
            if term.lower() in book["title"].lower() or term.lower() in book["author"].lower():
                results.append(book)
                break  # avoid duplicates if both title and author match
    return results


def borrow_book(book_id):
    """Borrow a book if available."""
    for book in library:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return f"You borrowed '{book['title']}'"
            else:
                return f"Book '{book['title']}' is not available"
    return "Book not found."


def return_book(book_id):
    """Return a book by setting it available again."""
    for book in library:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                return f"You returned '{book['title']}'"
            else:
                return f"Book '{book['title']}' was not borrowed"
    return "Book not found."

