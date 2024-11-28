from django.views.generic import ListView, DetailView
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'pages/news/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-created_at']

class NewsDetailView(DetailView):
    model = News
    template_name = 'pages/news/news_detail.html'
