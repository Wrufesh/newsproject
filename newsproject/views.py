from django.shortcuts import render

from news.models import News, Category


def index(request):
    carousel_news = News.objects.all()
    context = dict()
    context['carousel_news'] = carousel_news

    news_by_category = []

    for category in Category.menus:
        news_by_category.append((category.name, News.objects.filter(category=category)))

    context['news_by_category'] = news_by_category

    return render(request, 'index.html', context)
