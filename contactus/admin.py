# admin.py
from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'status', 'created_at', 'message')  
    list_filter = ('status', 'created_at',)  
    actions = None  # Menonaktifkan aksi selain mengubah status
    search_fields = ('name', 'email')  
    ordering = ('-updated_at',)

    def get_readonly_fields(self, request, obj=None):
        # Jika obj (ContactUs) sudah ada, hanya izinkan untuk mengubah status
        if obj:
            return ['name', 'phone', 'email', 'message', 'created_at', 'updated_at']
        return []

admin.site.register(ContactUs, ContactUsAdmin)
