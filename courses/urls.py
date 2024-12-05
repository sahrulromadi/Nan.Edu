from django.urls import path
from .views import CoursesListView, CourseDetailView

urlpatterns = [
    path('', CoursesListView.as_view(), name='courses_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='courses_detail'),
]
