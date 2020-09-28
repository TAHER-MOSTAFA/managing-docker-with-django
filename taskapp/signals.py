from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Docker
from .celery_helpers import MakingContainer

@receiver(post_save, sender=Docker)
def task_availabilty(sender, instance, *args, **kwargs):
    if instance.status!='Done':
        MakingContainer.apply_async(args=(instance.id,))