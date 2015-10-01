from django.conf.urls import include, url

urlpatterns = [
    url(r'^/$', 'backend.views.home', name='backend_home'),
    url(r'^/login/$', 'backend.views.login_user', name='backend_login'),
    url(r'^/logout/$', 'backend.views.logout_user', name='backend_logout'),
    url(r'^/cuenta/$', 'backend.views.manage_account', name='account'),
    url(r'^/cuenta/cambiar-clave/$', 'backend.views.update_password', name='update_password'),
    url(r'^/recuperar-clave/$', 'backend.views.restore_password', name='restore_password'),
    url(r'^/cms/', include('cms.urls', 'cms')),
    url(r'^/financiero', include('clients.urls')),
    url(r'^/usuarios', include('users.urls','users')),
]
