import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    #This class works under Django's generic Filter modules
    #through a simple search box, control the posts that contain what you entered.
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

        