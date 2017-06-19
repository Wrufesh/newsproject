from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.models import News


class NewsListView(ListView):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.request.GET.get('category_id', None)
        if category_id:
            context['object_list']  = News.objects.filter(category__id=category_id).order_by('publication_date')
        else:
            context['object_list'] = News.objects.all().order_by('publication_date')
        return context


class NewsDetailView(DetailView):
    model = News
