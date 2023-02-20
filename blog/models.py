from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Here we create the models that later migrate as a database to postgresql,
# always before each modification, the makemigrations command is executed to update the corresponding tables
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title