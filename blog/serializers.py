from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #Serializers are a fundamental part of the Django Rest Framework as it converts all
    #a data structure to be able to be interpreted and expedited by different formats such as Json.
    class Meta:
        model = Post
        fields = '__all__'

