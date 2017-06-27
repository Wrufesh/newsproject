from django.shortcuts import render

from news.models import News, Category


def index(request):
    news = News.objects.all().order_by('published_date')
    context = dict()
    context['latest_news'] = news[:10]
    context['top_news'] = news[:3]

    news_by_category = []

    for category in Category.menus():
        news_by_category.append((category, News.objects.filter(category=category)[:3]))

    context['news_by_category'] = news_by_category

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})