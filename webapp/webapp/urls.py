from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings




urlpatterns = [
    url(r'^', include('apps.urls', 'apps')),

    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),


    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT}),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
