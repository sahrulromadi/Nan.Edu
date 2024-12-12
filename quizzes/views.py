from django.shortcuts import render, redirect
from .models import Quiz, QuizResult, Answer
from .forms import QuizForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required 
def quiz_detail(request, quiz_id):
    # Ambil quiz berdasarkan id
    quiz = Quiz.objects.get(id=quiz_id)

    # Periksa apakah pengguna memiliki akses ke kursus terkait
    if not quiz.course.user_has_access.filter(id=request.user.id).exists():
        # Jika tidak memiliki akses, redirect ke halaman home
        return redirect(reverse('home'))
    
    # Periksa apakah pengguna sudah mengerjakan quiz ini sebelumnya
    quiz_results = QuizResult.objects.filter(quiz=quiz, user=request.user)
    if quiz_results.exists():
        # Jika sudah ada hasil quiz sebelumnya, arahkan ke halaman hasil quiz
        return redirect('quiz_result', quiz_id=quiz.id)

    # Menghapus hasil quiz sebelumnya untuk user yang sama dan quiz yang sama
    if request.method == 'POST':
        form = QuizForm(request.POST, quiz=quiz)
        if form.is_valid():
            correct_answers = 0
            total_questions = quiz.questions.count()

            # Hitung jumlah jawaban yang benar
            for question in quiz.questions.all():
                selected_answer_id = form.cleaned_data[f'question_{question.id}']
                selected_answer = Answer.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:
                    correct_answers += 1

            # Hitung skor dinamis
            score = (correct_answers / total_questions) * 100
            
            # Simpan total skor untuk quiz dan pengguna ini
            QuizResult.objects.create(
                user=request.user,
                quiz=quiz,
                score=score,
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

    # Periksa apakah pengguna memiliki akses ke kursus terkait
    if not quiz.course.user_has_access.filter(id=request.user.id).exists():
        # Jika tidak memiliki akses, redirect ke halaman home
        return redirect(reverse('home'))

    # Ambil hasil quiz berdasarkan quiz_id dan user yang sedang login
    quiz_results = QuizResult.objects.filter(quiz=quiz, user=request.user)

    if not quiz_result:
        return redirect('quiz_detail', quiz_id=quiz.id)

    # Total skor yang didapat
    total_score = sum([result.score for result in quiz_results])

    # Menghitung jawaban benar dan salah berdasarkan total skor
    total_questions = quiz.questions.count()
    correct_answers = round((total_score / 100) * total_questions) 
    wrong_answers = total_questions - correct_answers  

    # Tombol untuk mulai quiz lagi, menghapus hasil quiz sebelumnya
    if 'start_again' in request.POST:
        # Hapus semua hasil quiz sebelumnya untuk pengguna ini
        quiz_results.delete()
        # Arahkan kembali ke halaman quiz detail
        return redirect('quiz_detail', quiz_id=quiz.id)
    
    # Tambahkan kursus terkait ke dalam konteks
    course = quiz.course

    return render(request, 'pages/quiz/quiz_result.html', {
        'quiz': quiz,
        'quiz_results': quiz_results,
        'total_score': total_score,
        'correct_answers': correct_answers,
        'wrong_answers': wrong_answers,
        'course': course,
    })
