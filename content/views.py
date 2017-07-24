from django.shortcuts import render
from django.views.generic import ListView

from news.models import News, Category
from .models import AboutUs


def home(request):
    news = News.objects.order_by('-published_date')
    context = dict()
    context['latest_news'] = news[:10]
    context['top_news'] = news[:3]

    news_by_category = []

    for category in Category.menus():
        news_by_category.append((category, News.objects.filter(category=category).order_by('-published_date')[:3]))

    context['news_by_category'] = news_by_category

    return render(request, 'index.html', context)


# class OfficeStaffList(ListView):
#     model = OfficeStaff
#     template_name = 'content/office_staff.html'
#     queryset = OfficeStaff.objects.filter(special=False)
#
#     def get_context_data(self, **kwargs):
#         data = super(OfficeStaffList, self).get_context_data(**kwargs)
#         data['specials'] = OfficeStaff.objects.filter(special=True)
#         return data


def about_us(request):
    ctx = {
        'about_us': AboutUs.get_solo(),
        # 'members': OfficeStaff.objects.filter(special=False).order_by('order'),
        # 'specials': OfficeStaff.objects.filter(special=True).order_by('order'),
        # 'staff_messages': StaffMessage.objects.all()
    }
    return render(request, 'content/about_us.html', ctx)


def credits(request):
    ctx = {}
    return render(request, 'content/credits.html', ctx)
