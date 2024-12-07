from django.views.generic import ListView, DetailView
from .models import Course, CourseContent
from django.shortcuts import redirect
from django.urls import reverse

class CoursesListView(ListView):
    model = Course
    template_name = 'pages/courses/courses_list.html'
    context_object_name = 'courses_list'
    ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.all().order_by('-created_at')  # Default: Semua courses

        # Ambil filter dan search query dari GET parameter
        filter_option = self.request.GET.get('filter', 'all')  # Default: 'all'
        search_query = self.request.GET.get('search', '').strip()  # Default: kosong

        # Filter courses berdasarkan kepemilikan
        if filter_option == 'owned':
            queryset = queryset.filter(user_has_access=user)

        # Filter berdasarkan pencarian
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_option'] = self.request.GET.get('filter', 'all')  # Kirim filter ke template
        context['search_query'] = self.request.GET.get('search', '')  # Kirim search ke template
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'pages/courses/courses_detail.html'
    context_object_name = 'course'

    def dispatch(self, request, *args, **kwargs):
        course = self.get_object()  # Ambil objek Course berdasarkan pk yang ada di kwargs

        # Periksa apakah pengguna memiliki akses ke kursus
        if not course.user_has_access.filter(id=self.request.user.id).exists():
            # Jika tidak memiliki akses, redirect ke halaman home
            return redirect(reverse('home'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object() # mengambil course berdasarkan pk yang ada di kwargs

        # Ambil content_id dari query string, default ke konten pertama jika tidak ada
        content_id = self.request.GET.get('content_id')
        if content_id:
            selected_content = CourseContent.objects.filter(course=course, id=content_id).first()
        else:
            selected_content = CourseContent.objects.filter(course=course).order_by('order').first()

        context['contents'] = CourseContent.objects.filter(course=course).order_by('order')
        context['selected_content'] = selected_content
        return context