# admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'  # Nama plural untuk Profile
    fields = ('photo', 'user')  # Menampilkan field image dan user
    readonly_fields = ('photo',)  # Membuat field image menjadi hanya baca

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]  # Menambahkan inline Profile pada User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')  # Menampilkan kolom yang relevan

# Mendaftarkan kembali User dengan ProfileInline
admin.site.unregister(User)  # Melepas User yang ada
admin.site.register(User, UserAdmin)  # Mendaftarkan User dengan konfigurasi baru
