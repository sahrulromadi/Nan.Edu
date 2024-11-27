# videos/admin.py
from django.contrib import admin
from .models import Video
from courses.models import Course  # Mengimpor model Course untuk digunakan di admin

class VideoAdmin(admin.ModelAdmin):
    # Menampilkan kolom yang relevan untuk Video
    list_display = ('title', 'course', 'video_url', 'description')
    # Menambahkan pencarian berdasarkan judul dan deskripsi video
    search_fields = ('title', 'description', 'course__title')  # Menambahkan pencarian berdasarkan judul kursus
    # Menambahkan filter untuk melihat video berdasarkan kursus
    list_filter = ('course',)

admin.site.register(Video, VideoAdmin)
