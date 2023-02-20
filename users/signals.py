from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    #las señales permiten que 
    #ciertos “emisores” notifiquen a un conjunto de “receptores” que 
    #se ha producido alguna acción. Son especialmente útiles cuando muchos 
    #fragmentos de código pueden estar interesados ​​en los mismos eventos.

    #Este modulo no es indispensable para el proyecto y esta inconcluso.
    if created:
        Profile.objects.create(user=instance)