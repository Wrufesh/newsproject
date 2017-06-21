from django import template

from news.models import Category, News

register = template.Library()


@register.simple_tag
def get_current_categories():
    return Category.menus()


@register.simple_tag
def get_latest_news():
    return News.objects.all().order_by('published_date')[:10]