from django.views.generic import ListView, DetailView
from .models import Course, CourseContent
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class CoursesListView(ListView):
    model = Course
    template_name = 'pages/courses/courses_list.html'
    context_object_name = 'courses_list'
    ordering = ['-created_at']
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        queryset = Course.objects.all().order_by('-created_at')  

        # Ambil filter dan search query dari GET parameter
        filter_option = self.request.GET.get('filter', 'all')  
        search_query = self.request.GET.get('search', '').strip()  

        # Filter courses berdasarkan kepemilikan
        if filter_option == 'owned':
            queryset = queryset.filter(user_has_access=user)

        # Filter berdasarkan pencarian
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Tambahkan informasi akses pengguna ke setiap kursus
        for course in context['courses_list']:
            # Tentukan apakah user memiliki akses atau tidak
            course.has_access = course.user_has_access.filter(id=self.request.user.id).exists()
            
        context['filter_option'] = self.request.GET.get('filter', 'all')  
        context['search_query'] = self.request.GET.get('search', '')  
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'pages/courses/courses_detail.html'
    context_object_name = 'course'

    @method_decorator(login_required(login_url='account_login'))
    def dispatch(self, request, *args, **kwargs):
        course = self.get_object()  

        # Periksa apakah pengguna memiliki akses ke kursus
        if not course.user_has_access.filter(id=self.request.user.id).exists():
            # Jika tidak memiliki akses, redirect ke halaman pembayaran
            return redirect(reverse('upload_payment', kwargs={'course_id': course.pk}))

        return super().dispatch(request, *args, **kwargs)

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