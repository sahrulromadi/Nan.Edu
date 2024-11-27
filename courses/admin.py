# courses/admin.py
from django.contrib import admin
from .models import Course, CourseContent
from videos.models import Video  # Mengimpor model Video dari aplikasi videos

class CourseContentInline(admin.TabularInline):
    model = CourseContent
    extra = 1
    fields = ('video', 'order')  # Hapus 'created_at' dari fields yang ditampilkan
    # Menambahkan formfield_for_foreignkey agar memilih video dengan mudah
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'video':
            kwargs['queryset'] = Video.objects.all()  # Menampilkan semua video untuk dipilih
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_users_with_access')
    search_fields = ('title', 'description')
    inlines = [CourseContentInline]

    def get_users_with_access(self, obj):
        return ", ".join([user.username for user in obj.user_has_access.all()])
    get_users_with_access.short_description = 'Users with access'



admin.site.register(Course, CourseAdmin)
