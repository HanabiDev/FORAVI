from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'cms.views.home', name='home'),
    url(r'^articulos/$', 'cms.views.index_posts', name='posts_index'),
    url(r'^articulos/buscar/$', 'cms.views.search_posts', name='search_posts'),
    url(r'^articulos/nuevo/$', 'cms.views.create_post', name='new_post'),
    url(r'^articulos/editar/(?P<post_id>\d+)/$', 'cms.views.update_post', name='edit_post'),
    url(r'^articulos/publicar/(?P<post_id>\d+)/$', 'cms.views.publish_post', name='publish_post'),
    url(r'^articulos/despublicar/(?P<post_id>\d+)/$', 'cms.views.unpublish_post', name='hide_post'),
    url(r'^articulos/eliminar/(?P<post_id>\d+)/$', 'cms.views.delete_post', name='remove_post'),
]
