from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'clients.views.home', name='home'),
]
