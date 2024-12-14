from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from .models import Payment
from .forms import PaymentForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PaymentHistoryView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'pages/payments/payment_history.html'
    context_object_name = 'payments'
    paginate_by = 1
    ordering = ['-created_at']  

    def get_queryset(self):
        user = self.request.user
        queryset = Payment.objects.filter(user=user).order_by('-created_at')

        filter_option = self.request.GET.get('status', 'all')
        search_query = self.request.GET.get('search', '').strip()

        # Filter berdasarkan status
        if filter_option != 'all':
            queryset = queryset.filter(status=filter_option)

        # Pencarian berdasarkan title courses
        if search_query:
            queryset = queryset.filter(course__title__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_option'] = self.request.GET.get('status', 'all')
        context['search_query'] = self.request.GET.get('search', '')
        return context