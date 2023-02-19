from django.urls import path
from .views import PostDeleteView, PostUpdateView, SearchResultsView, PostDetailView, UserPostsView
from . import views

from users.views import create_post



urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/', UserPostsView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('create/', create_post, name='create_post'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]