import os
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Membuat profil baru setiap kali pengguna dibuat
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

# Menyimpan profil pengguna setiap kali ada perubahan pada pengguna
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.profile:
        instance.profile.save()

# Menghapus foto lama ketika profil dihapus
@receiver(pre_delete, sender=Profile)
def delete_old_photo(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

# Menghapus gambar lama sebelum mengganti dengan gambar baru
@receiver(pre_save, sender=Profile)
def delete_old_photo_on_profile_update(sender, instance, **kwargs):
    if instance.pk:  
        old_instance = Profile.objects.get(pk=instance.pk)
        if old_instance.photo != instance.photo:
            if old_instance.photo:
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)