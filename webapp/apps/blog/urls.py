from django.conf.urls import url

from .views import ArticleList, ArticleDetail

urlpatterns = [
    url(r'^$',
        ArticleList.as_view(), name='blog-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]*)/$',
        ArticleDetail.as_view(), name='blog-detail'),
]
