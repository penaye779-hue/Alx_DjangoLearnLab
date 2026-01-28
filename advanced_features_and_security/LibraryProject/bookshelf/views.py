from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# -------------------------
# VIEW ALL BOOKS
# -------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# -------------------------
# CREATE NEW BOOK
# -------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description', '')
        Book.objects.create(title=title, author=author, description=description)
        return redirect('book_list')
    return render(request, 'bookshelf/create_book.html')


#
