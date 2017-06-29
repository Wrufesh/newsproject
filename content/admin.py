from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from solo.admin import SingletonModelAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import AboutUs, OfficeStaff, StaffMessage


class SingletonSummernoteAdmin(SingletonModelAdmin, SummernoteModelAdmin):
    pass


admin.site.register(AboutUs, SingletonSummernoteAdmin)


class OfficeStaffAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['name', 'designation']
    list_display = ['name', 'designation', '_photo', 'special']
    list_filter = ['special', ]

    def _photo(self, obj):
        return mark_safe('<img src="%s" alt="Photo"/ height="100">' % obj.photo.url)

    _photo.admin_order_field = 'photo'


class StaffMessageAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['staff__name', 'staff__designation', 'content']
    list_display = ['_staff_name', '_staff_designation', '_photo']
    list_filter = ['staff__special', ]

    def get_queryset(self, request):
        return super(StaffMessageAdmin, self).get_queryset(request).select_related('staff')

    def _staff_name(self, obj):
        return obj.staff.name

    _staff_name.admin_order_field = 'staff__name'

    def _staff_designation(self, obj):
        return obj.staff.designation

    _staff_designation.admin_order_field = 'staff__designation'

    def _photo(self, obj):
        if obj.staff.photo:
            return mark_safe('<img src="%s" alt="Photo"/ height="100">' % obj.staff.photo.url)
        else:
            return '-'

    _photo.admin_order_field = 'staff__photo'


admin.site.register(OfficeStaff, OfficeStaffAdmin)
admin.site.register(StaffMessage, StaffMessageAdmin)
