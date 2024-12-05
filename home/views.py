from django.shortcuts import render
from news.models import News
from courses.models import Course

# Create your views here.
def home(request):
    latest_news = News.objects.order_by('-created_at')[:5]
    latest_courses = Course.objects.order_by('-created_at')[:5]
    context = {
        'latest_news': latest_news,
        'latest_courses': latest_courses
    }
    return render(request, 'pages/home/home.html', context)
