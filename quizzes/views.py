from django.shortcuts import render, redirect
from .models import Quiz, QuizResult, Answer
from .forms import QuizForm
from django.contrib.auth.decorators import login_required

@login_required 
def quiz_detail(request, quiz_id):
    # Ambil quiz berdasarkan id
    quiz = Quiz.objects.get(id=quiz_id)
    
    # Periksa apakah pengguna sudah mengerjakan quiz ini sebelumnya
    quiz_results = QuizResult.objects.filter(quiz=quiz, user=request.user)
    if quiz_results.exists():
        # Jika sudah ada hasil quiz sebelumnya, arahkan ke halaman hasil quiz
        return redirect('quiz_result', quiz_id=quiz.id)

    # Menghapus hasil quiz sebelumnya untuk user yang sama dan quiz yang sama
    if request.method == 'POST':
        form = QuizForm(request.POST, quiz=quiz)
        if form.is_valid():
            score = 0
            # Simpan hasil per soal dan hitung skor total
            for question in quiz.questions.all():
                selected_answer_id = form.cleaned_data[f'question_{question.id}']
                selected_answer = Answer.objects.get(id=selected_answer_id)
                is_correct = selected_answer.is_correct
                score += 1 if is_correct else 0
            
            # Simpan total skor untuk quiz dan pengguna ini
            QuizResult.objects.create(
                user=request.user,
                quiz=quiz,
                question=question,
                selected_answer=selected_answer,
                is_correct=is_correct,
                score=score
            )   
            
            # Arahkan ke halaman hasil quiz setelah pengisian
            return redirect('quiz_result', quiz_id=quiz.id)
    else:
        form = QuizForm(quiz=quiz)

    return render(request, 'pages/quiz/quiz_detail.html', {'form': form, 'quiz': quiz})

@login_required
def quiz_result(request, quiz_id):
    # Ambil quiz berdasarkan quiz_id
    quiz = Quiz.objects.get(id=quiz_id)

    # Ambil hasil quiz berdasarkan quiz_id dan user yang sedang login
    quiz_results = QuizResult.objects.filter(quiz=quiz, user=request.user)

    total_score = sum([result.score for result in quiz_results])

    # Tombol untuk mulai quiz lagi, menghapus hasil quiz sebelumnya
    if 'start_again' in request.POST:
        # Hapus semua hasil quiz sebelumnya untuk pengguna ini
        quiz_results.delete()
        # Arahkan kembali ke halaman quiz detail
        return redirect('quiz_detail', quiz_id=quiz.id)

    return render(request, 'pages/quiz/quiz_result.html', {
        'quiz': quiz,
        'quiz_results': quiz_results,
        'total_score': total_score,
    })
