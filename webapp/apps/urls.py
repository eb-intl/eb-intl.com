from django.conf.urls import url, include

from views import Index
from blog import urls as blog_urls


urlpatterns = [

    url(r'^news/', include(blog_urls, namespace='blog')),


]
'''
url(r'^$', Index.as_view(), name='index'),

url(r'^clients/', include('apps.clients.urls', 'clients')),
url(r'^factories/', include('apps.factories.urls', 'factories')),
url(r'^feeds/', include('apps.feeds.urls', 'feeds')),
url(r'^products/', include('apps.products.urls', 'products')),
url(r'^resources/', include('apps.resources.urls', 'resources')),
'''