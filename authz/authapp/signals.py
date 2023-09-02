from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import UserData


@receiver(post_save, sender=User)
def create_user_data(sender, instance, created, **kwargs):
    if created:
        UserData.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_data(sender, instance, **kwargs):
    instance.userData.save()