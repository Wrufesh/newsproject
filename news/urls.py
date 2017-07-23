from django.conf.urls import url

from news.views import NewsListView, NewsDetailView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news-list'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', NewsListView.as_view(), name='news-list'),
    url(r'^author/(?P<author_slug>[\w-]+)/$', NewsListView.as_view(), name='news-list'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', NewsListView.as_view(), name='news-list'),

    url(r'^(?P<slug>[\w-]+)/$', NewsDetailView.as_view(), name='news-detail'),
]
