from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'clients.views.home', name='home'),
    url(r'^login/$', 'clients.views.login_client', name='login'),
    url(r'^logout/$', 'clients.views.logout_client', name='logout'),
    url(r'^cuenta/$', 'clients.views.manage_account', name='account'),
    url(r'^cuenta/cambiar-clave/$', 'clients.views.update_password', name='update_password'),
    url(r'^recuperar-clave/$', 'clients.views.restore_password', name='restore_password'),
    url(r'^simuladores/$', 'clients.views.simulators', name='simulators'),
    url(r'^enviar-pqr/$', 'clients.views.send_request', name='send_request'),
]