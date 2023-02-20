from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # This class is not yet well developed because it already involves the use of an image as a static file and
    # since the purpose of this project is not about fine design details, it omitted to get it right
    # the Profile class that would include an individual image with each user.
    # a more complete version would include the possibility of uploading and having its own more detailed user profile page
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
