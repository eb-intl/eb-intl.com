from django.conf.urls import url, include

urlpatterns = [
    url(r'^blogs/', include('apps.blogs.urls', 'blogs')),
    url(r'^clients/', include('apps.clients.urls', 'clients')),
    url(r'^factories/', include('apps.factories.urls', 'factories')),
    url(r'^feeds/', include('apps.feeds.urls', 'feeds')),
    url(r'^products/', include('apps.products.urls', 'products')),
    url(r'^services/', include('apps.services.urls', 'services')),
    url(r'^resources/', include('apps.resources.urls', 'resources')),
]
