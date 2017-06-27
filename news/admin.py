from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import News, Category, Author, Tag


class SomeModelAdmin(SummernoteModelAdmin):
    exclude = ('created_by',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(News, SomeModelAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tag)
