# admin.py
from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'status', 'created_at', 'message')  # Menampilkan field yang relevan
    list_filter = ('status',)  # Filter berdasarkan status (read/unread)
    actions = None  # Menonaktifkan aksi selain mengubah status
    search_fields = ('name', 'email', 'message')  # Menambahkan pencarian berdasarkan nama, email, atau pesan

    def get_readonly_fields(self, request, obj=None):
        # Jika obj (ContactUs) sudah ada, hanya izinkan untuk mengubah status
        if obj:
            return ['name', 'phone', 'email', 'message', 'created_at']  # Hanya status yang bisa diubah
        return []

admin.site.register(ContactUs, ContactUsAdmin)
