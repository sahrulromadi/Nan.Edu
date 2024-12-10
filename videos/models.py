# videos/models.py
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    description = models.TextField()
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='videos', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
