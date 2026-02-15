from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.urls import path
from .views import register, profile
from django.urls import path
from .views import register, profile
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import search_posts, posts_by_tag
urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),                  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),      # View single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),           # Create post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Update post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete post
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'), 
]
urlpatterns += [
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
urlpatterns += [
    path('search/', search_posts, name='post-search'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),
]