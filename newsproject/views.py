from django.shortcuts import render

from news.models import News


def index(request):
    carousel_news = News.objects.all()
    context = dict()
    context['carousel_news'] = carousel_news
    return render(request, 'index.html', context)