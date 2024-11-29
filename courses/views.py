from django.views.generic import ListView
from .models import Course

class CoursesListView(ListView):
    model = Course
    template_name = 'pages/courses/courses_list.html'
    context_object_name = 'courses_list'
    ordering = ['-created_at']
