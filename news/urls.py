from django.conf.urls import url

from news.views import NewsListView, NewsDetailView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news-list'),
    url(r'^(?P<pk>[0-9]+)/$', NewsDetailView.as_view(), name='news-detail'),
]
