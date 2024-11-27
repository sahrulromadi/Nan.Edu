# courses/models.py
from django.db import models
from videos.models import Video  # Mengimpor model Video dari aplikasi videos
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user_has_access = models.ManyToManyField(User, related_name='courses_access')

    def __str__(self):
        return self.title


class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)  # Konten berhubungan dengan video
    order = models.PositiveIntegerField()  # Urutan konten dalam course
    created_at = models.DateTimeField(auto_now_add=True)  # Waktu pembuatan konten
    updated_at = models.DateTimeField(auto_now=True)  # Waktu update konten

    class Meta:
        ordering = ['order']  # Menentukan urutan konten berdasarkan field 'order'

    def __str__(self):
        return f"Content: {self.video.title if self.video else 'No video'} for {self.course.title}"
