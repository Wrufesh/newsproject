from django import template

from news.models import Category, News, Tag

register = template.Library()


@register.simple_tag
def get_current_categories():
    return Category.menus()


@register.simple_tag
def get_latest_news():
    return News.objects.all().order_by('published_date')[:10]

@register.simple_tag
def get_all_tags():
    return Tag.objects.all()