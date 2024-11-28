# courses/models.py
from django.db import models
from videos.models import Video  
from quizzes.models import Quiz 
from django.contrib.auth.models import User
from django.db.models import Max
from django.core.exceptions import ValidationError

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user_has_access = models.ManyToManyField(User, related_name='courses_access')

    def __str__(self):
        return self.title


class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)  
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)  
    order = models.PositiveIntegerField()  # Urutan konten dalam course
    created_at = models.DateTimeField(auto_now_add=True)  # Waktu pembuatan konten
    updated_at = models.DateTimeField(auto_now=True)  # Waktu update konten

    class Meta:
        ordering = ['order']  # Menentukan urutan konten berdasarkan field 'order'

    def __str__(self):
        return f"Content: {self.video.title if self.video else 'No video'} for {self.course.title}"

    def save(self, *args, **kwargs):
        # Jika order belum diset, otomatis berikan urutan berikutnya
        if not self.order:
            # Mengambil urutan konten tertinggi untuk kursus ini dan menambahkannya 1
            max_order = CourseContent.objects.filter(course=self.course).aggregate(Max('order'))['order__max']
            self.order = (max_order or 0) + 1
        
        super().save(*args, **kwargs)

    def clean(self):
        # Validasi jika video dan quiz keduanya diisi
        if self.video and self.quiz:
            raise ValidationError("Konten hanya bisa memiliki satu antara video atau quiz.")
        elif not self.video and not self.quiz:
            raise ValidationError("Konten harus memiliki video atau quiz.")