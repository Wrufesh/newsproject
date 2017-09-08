from django import template
from django.conf import settings
from django.contrib.sites.models import Site

from news.models import Category, News, Tag
from newsproject.settings import DISCUS_USERNAME

register = template.Library()


@register.simple_tag
def get_current_categories():
    return Category.objects.all()


@register.simple_tag
def get_latest_news():
    return News.objects.all().order_by('-published_date')[:10]


@register.simple_tag
def get_all_tags():
    return Tag.objects.all()


@register.simple_tag
def get_discus_username():
    return DISCUS_USERNAME
