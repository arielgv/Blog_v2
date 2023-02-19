from django.urls import path
from blog import views as v
from . import views
from .views import user_posts


urlpatterns = [
    path('', v.home, name='blog-home'),
    path('about/', v.about, name='blog-about'),
    path('api/profiles/', views.ProfileList.as_view(),name='profile-list'),
    path('api/posts/<int:user_id>/', user_posts,name='postlist'),
]