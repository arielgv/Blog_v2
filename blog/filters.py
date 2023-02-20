import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    #Esta clase funciona bajo módulos genericos de filtro de Django
    #a traves de un simple cuadro de búsqueda, controla los post que contengan lo ingresado.
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

        