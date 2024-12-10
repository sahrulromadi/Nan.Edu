# videos/admin.py
from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'video_url', 'description')
    search_fields = ('title', 'description', 'course__title')  
    list_filter = ('course',)
    ordering = ('-created_at',)

admin.site.register(Video, VideoAdmin)
