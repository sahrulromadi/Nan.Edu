from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ('photo', 'photo_preview', 'user')  
    readonly_fields = ('photo_preview',)  

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 150px; height: auto;" />', obj.photo.url)
        return "No Photo"
    
    photo_preview.short_description = 'Preview Photo'  

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]  # Menambahkan inline Profile pada User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')  
    list_filter = ('is_active',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.unregister(User)  # Melepas User yang ada
admin.site.register(User, UserAdmin) 
