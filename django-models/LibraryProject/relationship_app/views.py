from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view
def book_list(request):
    books = Book.objects.all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output)

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
