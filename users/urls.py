from django.conf.urls import url

urlpatterns = [

    url(r'^$', 'users.views.index_users', name='users_index'),
    url(r'^buscar/$', 'users.views.search_users', name='search_users'),
    url(r'^nuevo/$', 'users.views.create_user', name='new_user'),
    url(r'^editar/(?P<user_id>\d+)/$', 'users.views.update_user', name='edit_user'),
    url(r'^editar/(?P<user_id>\d+)/cambiar-clave/$', 'users.views.update_user_password', name='edit_user_password'),
    url(r'^bloquear/(?P<user_id>\d+)/$', 'users.views.disable_user', name='block_user'),
    url(r'^desbloquear/(?P<user_id>\d+)/$', 'users.views.enable_user', name='unblock_user'),
]



