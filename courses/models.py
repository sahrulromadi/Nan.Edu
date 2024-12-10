# courses/models.py
from django.db import models
from videos.models import Video  
from quizzes.models import Quiz 
from django.contrib.auth.models import User
from django.db.models import Max
from mentors.models import Mentor
from django.core.exceptions import ValidationError

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='courses_images/', blank=True, null=True)
    user_has_access = models.ManyToManyField(User, related_name='courses_access')
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=False, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title

class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)  
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)  
    order = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        ordering = ['order']  

    def clean(self):
        # Validasi agar 'order' tidak duplikat dalam kursus yang sama
        if CourseContent.objects.filter(course=self.course, order=self.order).exclude(id=self.id).exists():
            raise ValidationError(f"Urutan {self.order} sudah digunakan. Order tidak boleh sama")
        
        super().clean()

    def save(self, *args, **kwargs):
        # Jika order belum diset, otomatis berikan urutan berikutnya
        if not self.order:
            max_order = CourseContent.objects.filter(course=self.course).aggregate(Max('order'))['order__max']
            self.order = (max_order or 0) + 1

        super().save(*args, **kwargs)

        # Setelah menyimpan, pastikan urutan konten berurutan
        self.reorder_contents()

    def reorder_contents(self):
        # Ambil semua konten dari kursus ini dan urutkan berdasarkan 'order'
        contents = CourseContent.objects.filter(course=self.course).order_by('order')
        
        # Update urutan agar berurutan (tidak ada gap)
        for index, content in enumerate(contents):
            if content.order != index + 1:  # Jika urutan tidak sesuai
                content.order = index + 1  # Sesuaikan urutan
                content.save()

    def __str__(self):
        return str(self.order)
