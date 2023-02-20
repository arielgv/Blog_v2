from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Esta clase aún no esta bien desarrollada porque ya implica el uso de una imagen como archivo estatico y 
    # ya que el proposito de este proyecto no es acerca de detalles de disenos finos, se omitio lograr bien 
    # la clase Perfil que incluiria una imagen individual con cada usuario.
    # una version mas completa abarcaria la posibilidad de subir y tener una propia pagina de perfil de usuario mas detallada
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
