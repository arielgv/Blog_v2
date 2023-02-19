from django.urls import path
from .views import PostDeleteView, PostUpdateView
from . import views
from users.views import create_post


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('create/', create_post, name='create_post'),
]