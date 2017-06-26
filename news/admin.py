from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import News, Category, Author, Tag


class SomeModelAdmin(SummernoteModelAdmin):
    pass


admin.site.register(News, SomeModelAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tag)
