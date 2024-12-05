from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.db.models import ImageField
from .models import Mentor
import os

# Menghapus gambar saat Mentor dihapus
@receiver(post_delete, sender=Mentor)
def delete_image_on_mentors_delete(sender, instance, **kwargs):
    if instance.photo:
        # Menghapus file gambar dari sistem file
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

# Menghapus gambar lama sebelum mengganti dengan gambar baru
@receiver(pre_save, sender=Mentor)
def delete_old_image_on_mentor_update(sender, instance, **kwargs):
    if instance.pk:  # Jika ini adalah update, bukan create
        old_instance = Mentor.objects.get(pk=instance.pk)
        if old_instance.photo != instance.photo:
            # Menghapus file gambar lama jika ada perubahan gambar
            if old_instance.photo:
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
