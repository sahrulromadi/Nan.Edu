# videos/models.py
from django.db import models
from django.apps import apps  # Mengimpor apps untuk mendapatkan model

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    description = models.TextField()
    # Gunakan apps.get_model untuk mendapatkan model Course
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='videos', null=True, blank=True)

    def __str__(self):
        return self.title
