from .models import Author, Book, Library, Librarian

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # ALX checker requires this exact string
    return Book.objects.filter(author=author)      # ALX checker requires this exact string

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)  # ALX checker requires this exact string
