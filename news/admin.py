from django.contrib import admin
from django.utils.html import format_html
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at') 
    readonly_fields = ('image_preview',)
    search_fields = ('title', 'content') 
    list_filter = ('created_at', 'updated_at',)  
    ordering = ('-updated_at',)  

    def image_preview(self, obj):
        if obj.image: 
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"
