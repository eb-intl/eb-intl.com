from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),

    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),

    url(r'^apps/', include('apps.urls', 'apps')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
