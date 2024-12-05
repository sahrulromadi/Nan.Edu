from django.views.generic import ListView, DetailView
from .models import Course, CourseContent

class CoursesListView(ListView):
    model = Course
    template_name = 'pages/courses/courses_list.html'
    context_object_name = 'courses_list'
    ordering = ['-created_at']

class CourseDetailView(DetailView):
    model = Course
    template_name = 'pages/courses/courses_detail.html'

    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()

        # Ambil content_id dari query string, default ke konten pertama jika tidak ada
        content_id = self.request.GET.get('content_id')
        if content_id:
            selected_content = CourseContent.objects.filter(course=course, id=content_id).first()
        else:
            selected_content = CourseContent.objects.filter(course=course).order_by('order').first()

        context['contents'] = CourseContent.objects.filter(course=course).order_by('order')
        context['selected_content'] = selected_content
        return context