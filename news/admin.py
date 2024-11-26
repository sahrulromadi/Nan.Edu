# news/admin.py

from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Menampilkan kolom yang relevan di admin
    search_fields = ('title', 'content')  # Menambahkan pencarian berdasarkan judul dan konten
    list_filter = ('created_at', 'updated_at')  # Filter berdasarkan tanggal pembuatan atau pembaruan
    ordering = ('-created_at',)  # Menampilkan berita terbaru di atas (sorting descending)
