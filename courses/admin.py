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

    # agar courses menampilkan video dan quiz yang relevan (MASIH BELUM BISA)
    def __init__(self, *args, **kwargs):
        # Ambil 'course' dari initial atau instance
        course = kwargs.pop('course', None)
        super().__init__(*args, **kwargs)

        if course:
            self.fields['video'].queryset = Video.objects.filter(course=course)
            self.fields['quiz'].queryset = Quiz.objects.filter(course=course)
        else:
            self.fields['video'].queryset = Video.objects.none()
            self.fields['quiz'].queryset = Quiz.objects.none()

    # handling
    def clean(self):
        cleaned_data = super().clean()
        video = cleaned_data.get('video')
        quiz = cleaned_data.get('quiz')

        # Validasi agar hanya satu yang diisi, video atau quiz
        if video and quiz:
            raise ValidationError("Konten hanya bisa memiliki satu antara video atau quiz.")

        return cleaned_data

# Inline untuk CourseContent dengan validasi form
class CourseContentInline(admin.TabularInline):
    model = CourseContent
    form = CourseContentForm  
    extra = 1
    fields = ('video', 'quiz', 'order')  

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj:
            # Pastikan form menerima 'course' sebagai parameter tambahan
            for form in formset.form.base_fields.values():
                form.widget.attrs['data-course-id'] = obj.id
            formset.form = type(formset.form)(
                "CourseContentFormWithCourse",
                (formset.form,),
                {"__init__": lambda self, *args, **kwargs: CourseContentForm.__init__(self, *args, course=obj, **kwargs)},
            )
        return formset

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('title', 'description')
    inlines = [CourseContentInline]
    ordering = ('-created_at',)

admin.site.register(Course, CourseAdmin)
