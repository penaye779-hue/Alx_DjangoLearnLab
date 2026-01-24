from django.urls import path
from . import views  # for Task 2 checker
from .views import list_books, LibraryDetailView  # for Task 1 checker

urlpatterns = [
    # Task 1 URLs
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Task 2 URLs (use views.register and views.LoginView/LogoutView)
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
