from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from .models import Payment
from .forms import PaymentForm
from django.core.paginator import Paginator

@login_required
def upload_proof_of_payment(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Cek apakah user sudah pernah mengirim bukti pembayaran untuk kursus ini dan statusnya masih pending
    existing_payment = Payment.objects.filter(user=request.user, course=course, status=Payment.PaymentStatus.PENDING).first()
    if existing_payment:
        # Jika sudah ada pembayaran dengan status PENDING, arahkan ke riwayat pembayaran
        return redirect('payment_history')
    
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

@login_required
def payment_history(request):
    payments = Payment.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(payments, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'pages/payments/payment_history.html', {'page_obj': page_obj})