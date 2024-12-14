from django.urls import path
from . import views
from .views import PaymentHistoryView

urlpatterns = [
    path('upload-payment/<int:course_id>/', views.upload_proof_of_payment, name='upload_payment'),
    path('payment-history/', PaymentHistoryView.as_view(), name='payment_history'),
]
