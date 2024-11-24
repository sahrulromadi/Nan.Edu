import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def save(self, *args, **kwargs):
        # Jika profil sudah ada, periksa apakah gambar diperbarui dan hapus file lama
        if self.pk:
            old_profile = Profile.objects.get(pk=self.pk)
            if old_profile.photo != self.photo:
                # Menghapus foto lama jika berbeda dengan foto yang baru
                if old_profile.photo:
                    if os.path.isfile(old_profile.photo.path):
                        os.remove(old_profile.photo.path)

        # Simpan objek profil
        super(Profile, self).save(*args, **kwargs)