from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import News


class SomeModelAdmin(SummernoteModelAdmin):
    pass


admin.site.register(News, SomeModelAdmin)
