from django.contrib import admin
from django.utils.html import format_html
from .models import Mentor

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_thumbnail')  # Tampilkan thumbnail foto di daftar admin
    search_fields = ('name', 'experience',)  # Fitur pencarian berdasarkan nama
    readonly_fields = ('photo_preview',)  # Preview foto di form detail

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.photo.url)
        return "No Photo"
    
    photo_thumbnail.short_description = 'Photo' 

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 150px; height: auto;" />', obj.photo.url)
        return "No Photo"
    
    photo_preview.short_description = 'Preview Photo'
