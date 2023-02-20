from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #Los serializadores son parte fundamental de Django Rest Framework ya que convierte toda
    #una estructura de datos para poder ser interpretada y agilizada por distintos formatos como Json.
    class Meta:
        model = Post
        fields = '__all__'

