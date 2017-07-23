from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.models import News, Category


def get_categories_context(request):
    return {'categories': Category.objects.all()}


class NewsListView(ListView):
    model = News

    def get_queryset(self):
        news = News.objects.order_by('-published_date')
        category_slug = self.kwargs.get('category_slug')
        author_slug = self.kwargs.get('author_slug')
        tag_slug = self.kwargs.get('tag_slug')
        if category_slug:
            news = news.filter(category__slug=category_slug)
        if author_slug:
            news = news.filter(author__slug=author_slug)
        if tag_slug:
            news = news.filter(tag__slug=tag_slug)
        return news


class NewsDetailView(DetailView):
    model = News
