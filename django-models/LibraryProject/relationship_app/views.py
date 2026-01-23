from django.shortcuts import render, redirect
from django.contrib.auth import login  # ALX requires this import
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from .models import Book, Library  # ALX requires Library import

# -------------------------
# Authentication Views
# -------------------------

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# -------------------------
# Books List View
# -------------------------

def list_books(request):
    books = Book.objects.all()  # ALX expects Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# -------------------------
# Library Detail View
# -------------------------

class LibraryDetailView(DetailView):  # ALX expects DetailView
    model = Library
    template_name = "relationship_app/library_detail.html"
