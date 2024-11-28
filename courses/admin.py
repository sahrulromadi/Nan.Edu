# courses/admin.py
from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import Course, CourseContent
from videos.models import Video
from quizzes.models import Quiz

# Membuat form custom untuk CourseContent
class CourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContent
        fields = ('video', 'quiz', 'order')

    def clean(self):
        cleaned_data = super().clean()
        video = cleaned_data.get('video')
        quiz = cleaned_data.get('quiz')

        # Validasi agar hanya satu yang diisi, video atau quiz
        if video and quiz:
            raise ValidationError("Konten hanya bisa memiliki satu antara video atau quiz.")
        elif not video and not quiz:
            raise ValidationError("Konten harus memiliki video atau quiz.")

        return cleaned_data

# Inline untuk CourseContent dengan validasi form
class CourseContentInline(admin.TabularInline):
    model = CourseContent
    form = CourseContentForm  # Menetapkan form custom
    extra = 1
    fields = ('video', 'quiz', 'order')  # Menampilkan video dan quiz dalam form
    # Menambahkan formfield_for_foreignkey agar memilih video dan quiz dengan mudah
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'video':
            kwargs['queryset'] = Video.objects.all()  # Menampilkan semua video untuk dipilih
        elif db_field.name == 'quiz':
            kwargs['queryset'] = Quiz.objects.all()  # Menampilkan semua quiz untuk dipilih
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('title', 'description')
    inlines = [CourseContentInline]
    ordering = ('price', 'created_at',)

    def get_users_with_access(self, obj):
        return ", ".join([user.username for user in obj.user_has_access.all()])
    get_users_with_access.short_description = 'Users with access'

admin.site.register(Course, CourseAdmin)
