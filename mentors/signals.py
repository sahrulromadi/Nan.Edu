from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Mentor

@receiver(post_delete, sender=Mentor)
def delete_image_on_mentors_delete(sender, instance, **kwargs):
    if instance.photo:
        instance.photo.delete(False)
