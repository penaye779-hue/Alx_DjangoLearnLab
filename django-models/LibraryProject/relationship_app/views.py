from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view for library details
from django.views.generic.detail import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
