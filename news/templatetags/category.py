from django import template
from django.conf import settings
from django.contrib.sites.models import Site

from news.models import Category, News, Tag

register = template.Library()


@register.simple_tag
def get_current_categories():
    return Category.menus()


@register.simple_tag
def get_latest_news():
    return News.objects.all().order_by('-published_date')[:10]


@register.simple_tag
def get_all_tags():
    return Tag.objects.all()


@register.simple_tag
def get_site_object():
    return Site.objects.get(id=settings.SITE_ID)
