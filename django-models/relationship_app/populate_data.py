# relationship_app/populate_data.py
import os
import sys
import django

# Add the project root to Python path so Python can find LibraryProject
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Library, Book, Author

def populate():
    # Create some authors
    author1, _ = Author.objects.get_or_create(name="J.K. Rowling")
    author2, _ = Author.objects.get_or_create(name="George Orwell")

    # Create some libraries
    library1, _ = Library.objects.get_or_create(name="Central Library", location="Downtown")
    library2, _ = Library.objects.get_or_create(name="Community Library", location="Uptown")

    # Add books to libraries
    Book.objects.get_or_create(title="Harry Potter", author=author1, library=library1)
    Book.objects.get_or_create(title="1984", author=author2, library=library2)
    Book.objects.get_or_create(title="Animal Farm", author=author2, library=library1)

    print("Database populated successfully!")

if __name__ == "__main__":
    populate()
