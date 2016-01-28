from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin', include('backend.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^clientes/', include('clients.urls', 'clients')),
    url(r'^', include('frontend.urls', 'frontend')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
