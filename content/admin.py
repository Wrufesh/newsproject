from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from solo.admin import SingletonModelAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import Content


class SingletonSummernoteAdmin(SingletonModelAdmin, SummernoteModelAdmin):
    pass


admin.site.register(Content, SingletonSummernoteAdmin)

