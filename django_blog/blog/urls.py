from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.urls import path
from .views import register, profile
urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),                  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),      # View single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),           # Create post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Update post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete post
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]
