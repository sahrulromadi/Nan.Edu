from django.contrib.auth.models import User
from django.db import models
from django.apps import apps


class Quiz(models.Model):
    title = models.CharField(max_length=255, help_text="Judul kuis")
    description = models.TextField(blank=True, help_text="Deskripsi singkat tentang kuis")
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='quizzes', null=True, blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, 
        related_name='questions', 
        on_delete=models.CASCADE, 
        default=1  # Gunakan ID kuis yang valid
    )
    text = models.CharField(max_length=255, help_text="Tulis pertanyaan")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, help_text="Tulis pilihan jawaban")
    is_correct = models.BooleanField(default=False, help_text="Tandai jika jawaban ini benar")

    def __str__(self):
        return f"{self.text} (Benar: {self.is_correct})"


class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='results')
    selected_answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True, blank=True, related_name='results')
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.question.text} (Benar: {self.is_correct})"
