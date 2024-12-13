from django.urls import path
from . import views

urlpatterns = [
    path('upload-payment/<int:course_id>/', views.upload_proof_of_payment, name='upload_payment'),
]
