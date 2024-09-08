from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
            logger.info(f"Profile created for user {instance.username}")
        except Exception as e:
            logger.error(f"Error creating profile for user {instance.username}: {e}")
