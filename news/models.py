from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    headline = models.CharField(max_length=500)
    article = models.TextField()
    category = models.ForeignKey(Category)
    reporter = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name_plural = _('News')
