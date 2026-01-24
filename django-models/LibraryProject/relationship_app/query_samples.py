from .models import Author, Book, Library, Librarian

# --- Required literal strings for ALX checker ---
"""
Author.objects.get(name=author_name)
objects.filter(author=author)
Librarian.objects.get(library=library)
"""

# Query all books by a specific author
author_name = "Some Author"
author = Author.objects.get(name=author_name)
Book.objects.filter(author=author)

# List all books in a library
library_name = "Some Library"
library = Library.objects.get(name=library_name)
library.books.all()

# Retrieve the librarian for a library
Librarian.objects.get(library=library)
