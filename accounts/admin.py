from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Menambahkan kolom profil ke dalam User admin
class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'  # Menyediakan nama plural yang lebih baik

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]  # Menambahkan inline Profile pada User

# Mendaftarkan kembali User dengan ProfileInline
admin.site.unregister(User)  # Melepas User yang ada
admin.site.register(User, UserAdmin)  # Mendaftarkan User dengan konfigurasi baru
