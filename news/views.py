from django.views.generic import ListView, DetailView
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'pages/news/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        order_by = self.request.GET.get('order_by', 'desc')  

        # Filter berdasarkan urutan tanggal
        if order_by == 'asc':
            queryset = queryset.order_by('created_at')  
        else:
            queryset = queryset.order_by('-created_at') 

        # Pencarian berdasarkan judul
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['order_by'] = self.request.GET.get('order_by', 'desc')
        return context

class NewsDetailView(DetailView):
    model = News
    template_name = 'pages/news/news_detail.html'
