from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from lxml import html
from django.db.models import Q

from django.core.cache import cache


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_topic_count(self):
        return self.news.all().count()


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    show_in_menu = models.BooleanField(default=True)

    @classmethod
    def menus(cls):
        cached = cache.get('menu')
        if not cached:
            categories = Category.objects.filter(show_in_menu=True)
            cache.set('menu', categories, timeout=None)
            return categories
        return cached

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.set('menu', Category.objects.filter(show_in_menu=True), timeout=None)


class News(models.Model):
    headline = models.CharField(max_length=500)
    article = models.TextField()
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, related_name='news')
    created_by = models.ForeignKey(User)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_thumbnail(self):
        xhtml = html.fromstring(self.article)
        img_sources = xhtml.xpath('//img/@src')
        if img_sources:
            return img_sources[0]
        else:
            # todo return default image
            return None

    def get_related_articles(self):
        return News.objects.filter(tags__in=self.tags.all()).distinct()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news-detail', args=[str(self.id)])

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name_plural = _('News')
