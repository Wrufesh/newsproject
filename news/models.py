import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from lxml import html
from django.utils import timezone
from django.db.models import Q, Prefetch

from django.core.cache import cache

from datetime import datetime

from newsproject.settings import MEDIA_ROOT
from newsproject.utils.cache import invalidate_template_cache
from newsproject.utils.forms import unique_slugify


class Tag(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Leave empty/unchanged for default slug.')

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Tag, self).save(*args, **kwargs)
        invalidate_template_cache('sidebar')
        invalidate_template_cache('news_tags')

    def __str__(self):
        return self.name

    def get_topic_count(self):
        return self.news.all().count()


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='authors_pictures', null=True, blank=True)
    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Leave empty/unchanged for default slug.')

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Author, self).save(*args, **kwargs)
        invalidate_template_cache('top-news')
        invalidate_template_cache('latest-news')
        invalidate_template_cache('category_news')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    show_in_menu = models.BooleanField(default=True)
    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Leave empty/unchanged for default slug.')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super().save(*args, **kwargs)

        invalidate_template_cache('sidebar')
        invalidate_template_cache('categories_menu')
        invalidate_template_cache('category_news')
        invalidate_template_cache('latest-news')

    class Meta:
        verbose_name_plural = 'Categories'


class News(models.Model):
    headline = models.CharField(max_length=500)
    article = models.TextField()
    category = models.ForeignKey(Category, related_name='news')
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, related_name='news')
    created_by = models.ForeignKey(User)
    published_date = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Leave empty/unchanged for default slug.')

    def save(self, *args, **kwargs):
        unique_slugify(self, self.headline)
        super(News, self).save(*args, **kwargs)
        invalidate_template_cache('sidebar')
        invalidate_template_cache('top-news')
        invalidate_template_cache('latest-news')
        invalidate_template_cache('category_news')

    def get_thumbnail(self):
        xhtml = html.fromstring(self.article)
        img_sources = xhtml.xpath('//img/@src')
        if img_sources:
            return img_sources[0]
        else:
            return os.path.join('/media/', 'default_news.jpg')

    def get_related_articles(self):
        return News.objects.select_related('category', 'created_by', 'author').filter(
            tags__in=self.tags.all()).distinct()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news-detail', args=[str(self.slug)])

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name_plural = _('News')
