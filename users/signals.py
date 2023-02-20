from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # signals allow
    # certain “senders” notify a set of “receivers” that
    # some action has occurred. They are especially useful when many
    # code snippets may be interested in the same events.
    # This module is not essential for the project and is unfinished.
    if created:
        Profile.objects.create(user=instance)