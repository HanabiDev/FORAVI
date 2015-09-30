from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^', include('frontend.urls', 'frontend')),
    url(r'^admin', include('backend.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^clientes/', include('clients.urls')),
    url(r'^django-admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
