from django.urls import path
#from .views import PostDeleteView, PostUpdateView
from blog import views
from .views import ProfileList


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('api/profiles/', ProfileList.as_view(),name='profile-list'),
]