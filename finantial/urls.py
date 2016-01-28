from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'finantial.views.home', name='finantial_home'),

    url(r'^cargar/$', 'finantial.views.load_reports', name='load'),
    url(r'^cargar-asociados/$', 'finantial.views.load_clients', name='load_clients'),
    url(r'^cargar-prestamos/$', 'finantial.views.load_credits', name='load_credits'),
    url(r'^cargar-depositos/$', 'finantial.views.load_deposits', name='load_deposits'),
    url(r'^consultar/$', 'finantial.views.query', name='query'),
    url(r'^consultar/(?P<client_dni>\d+)/$', 'finantial.views.show_client_report', name='client_report'),
]
