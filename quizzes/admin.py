from django.contrib import admin
from .models import Quiz, Question, Answer, QuizResult

# Admin untuk model Quiz
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Admin untuk model Question
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3  # Jumlah baris kosong yang akan ditampilkan untuk menambah jawaban baru (bisa diubah sesuai kebutuhan)
    fields = ('text', 'is_correct')  # Menampilkan kolom teks jawaban dan status jawaban benar

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'created_at')
    search_fields = ('text',)
    list_filter = ('quiz', 'created_at')
    ordering = ('-created_at',)
    inlines = [AnswerInline] 
    # Admin untuk model QuizResult
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'question', 'selected_answer', 'is_correct', 'created_at')
    search_fields = ('user__username', 'quiz__title', 'question__text')
    list_filter = ('quiz', 'is_correct', 'created_at')
    ordering = ('-created_at',)

# Register models with their respective admin classes
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizResult, QuizResultAdmin)