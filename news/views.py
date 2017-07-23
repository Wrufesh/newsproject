from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.models import News, Category


def get_categories_context(request):
    return {'categories': Category.objects.all()}


class NewsListView(ListView):
    model = News

    def get_queryset(self):
        news = News.objects.order_by('-published_date')
        if self.category_slug:
            news = news.filter(category__slug=self.category_slug)
        if self.author_slug:
            news = news.filter(author__slug=self.author_slug)
        if self.tag_slug:
            news = news.filter(tag__slug=self.tag_slug)
        return news


class NewsDetailView(DetailView):
    model = News
