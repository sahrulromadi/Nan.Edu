from django import forms
from .models import Answer, QuizResult

class QuizForm(forms.Form):
    # Form untuk menampilkan soal dan memilih jawaban
    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop('quiz')
        super(QuizForm, self).__init__(*args, **kwargs)
        
        # Menambahkan soal dan pilihan jawaban untuk setiap soal dalam quiz
        for question in quiz.questions.all():
            choices = [(answer.id, answer.text) for answer in question.answers.all()]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=choices,
                widget=forms.RadioSelect
            )

class QuizResultForm(forms.ModelForm):
    class Meta:
        model = QuizResult
        fields = ['score']
