from django.core.cache import cache
from django.db import models
from solo.models import SingletonModel



class AboutUs(SingletonModel):
    content = models.TextField(blank=True, null=True)


# class PurchaseInstruction(SingletonModel):
#     content = models.TextField(blank=True, null=True)
#
#     @staticmethod
#     def get():
#         cached = cache.get('purchase_instruction')
#         if cached:
#             return cached
#         content = PurchaseInstruction.get_solo().content
#         cache.set('purchase_instruction', content, timeout=None)
#         return content
#
#     def save(self, *args, **kwargs):
#         super(PurchaseInstruction, self).save(*args, **kwargs)
#         cache.set('purchase_instruction', self.content, timeout=None)


class OfficeStaff(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='staff_photos/')
    special = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('order',)


class StaffMessage(models.Model):
    staff = models.ForeignKey(OfficeStaff)
    content = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.staff.name

    class Meta:
        ordering = ('order',)
