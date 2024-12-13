from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from .forms import PaymentForm

@login_required
def upload_proof_of_payment(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.course = course
            payment.amount = course.price
            payment.save()
            messages.success(request, 'Payment proof submitted successfully.')
            return redirect('home')  
    else:
        form = PaymentForm()
    return render(request, 'pages/payments/upload_proof.html', {'form': form, 'course': course})
