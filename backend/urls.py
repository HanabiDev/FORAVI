from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'backend.views.home', name='backend_home'),
    url(r'^cms/', include('cms.urls', 'cms')),
    url(r'^financiero/', include('clients.urls')),
]
