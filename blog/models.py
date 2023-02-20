from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Aqui creamos los modelos que luego migran como base de datos hacia postgresql,
# siempre ante cada modificacion, se realiza el comando makemigrations para actualizar las tablas correspondientes
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title