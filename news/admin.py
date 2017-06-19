from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import News, Category


class SomeModelAdmin(SummernoteModelAdmin):
    pass


admin.site.register(News, SomeModelAdmin)
admin.site.register(Category)
