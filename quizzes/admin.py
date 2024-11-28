from django.contrib import admin
from .models import Quiz, Question, Answer, QuizResult

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'course', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'course',)
    ordering = ('-created_at',)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  
    fields = ('text', 'is_correct')  

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'created_at')
    search_fields = ('text', 'quiz',)
    list_filter = ('quiz', 'created_at')
    ordering = ('-created_at',)
    inlines = [AnswerInline] 

class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'question', 'selected_answer', 'is_correct', 'created_at')
    search_fields = ('user__username', 'quiz__title', 'question__text')
    list_filter = ('quiz', 'is_correct', 'created_at')
    ordering = ('-created_at',)

    readonly_fields = ('user', 'quiz', 'question', 'selected_answer', 'is_correct', 'created_at')

    # Menyembunyikan form input untuk membuat QuizResult tidak bisa diinput
    def has_add_permission(self, request):
        return False  

    def has_change_permission(self, request, obj=None):
        return True  

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizResult, QuizResultAdmin)