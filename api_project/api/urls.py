from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # must use path()
]
# Create router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # Include router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]