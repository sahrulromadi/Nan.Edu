from django.views.generic import ListView, DetailView
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    ordering = ['-created_at']  # Urutkan dari berita terbaru

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
