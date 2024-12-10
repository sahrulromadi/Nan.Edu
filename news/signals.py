from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import News
import os

# Menghapus gambar saat News dihapus
@receiver(post_delete, sender=News)
def delete_image_on_news_delete(sender, instance, **kwargs):
    if instance.image:
        # Menghapus file gambar dari sistem file
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

# Menghapus gambar lama sebelum mengganti dengan gambar baru
@receiver(pre_save, sender=News)
def delete_old_image_on_news_update(sender, instance, **kwargs):
    if instance.pk:  # Jika ini adalah update, bukan create
        old_instance = News.objects.get(pk=instance.pk)
        if old_instance.image != instance.image:
            # Menghapus file gambar lama jika ada perubahan gambar
            if old_instance.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
