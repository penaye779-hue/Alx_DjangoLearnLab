from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Use views.register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
