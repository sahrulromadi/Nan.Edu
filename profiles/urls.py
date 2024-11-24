from django.urls import path
from . import views

urlpatterns = [
    path('view-profile/', views.profile_view, name='view_profile'),
    path('edit-profile/', views.profile_update, name='edit_profile'),
]
