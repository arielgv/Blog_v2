from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    #Los serializadores son parte fundamental de Django Rest Framework ya que convierte toda
    #una estructura de datos para poder ser interpretada y agilizada por distintos formatos como Json.
    class Meta:
        model = Profile
        fields = '__all__'