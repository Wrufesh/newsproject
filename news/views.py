from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.models import News, Category


def get_categories_context(request):
    return {'categories': Category.objects.all()}


class NewsListView(ListView):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.request.GET.get('category_id', None)
        author_id = self.request.GET.get('author_id', None)
        tag_id = self.request.GET.get('tag_id', None)
        news = News.objects.order_by('-published_date')
        if category_id:
            news = news.filter(category__id=category_id)
        if author_id:
            news = news.filter(author__id=author_id)

        if tag_id:
            news = news.filter(tags__id=tag_id)

        context['object_list'] = news
        return context


class NewsDetailView(DetailView):
    model = News
