from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'cms.views.home', name='home'),

    url(r'^articulos$', 'cms.views.index_posts', name='posts_index'),
    url(r'^articulos/buscar/$', 'cms.views.search_posts', name='search_posts'),
    url(r'^articulos/nuevo/$', 'cms.views.create_post', name='new_post'),
    url(r'^articulos/editar/(?P<post_id>\d+)/$', 'cms.views.update_post', name='edit_post'),
    url(r'^articulos/publicar/(?P<post_id>\d+)/$', 'cms.views.publish_post', name='publish_post'),
    url(r'^articulos/despublicar/(?P<post_id>\d+)/$', 'cms.views.unpublish_post', name='hide_post'),
    url(r'^articulos/eliminar/(?P<post_id>\d+)/$', 'cms.views.delete_post', name='remove_post'),

    url(r'^documentos/$', 'cms.views.index_docs', name='docs_index'),
    url(r'^documentos/buscar/$', 'cms.views.search_docs', name='search_docs'),
    url(r'^documentos/nuevo/$', 'cms.views.create_doc', name='new_doc'),
    url(r'^documentos/editar/(?P<doc_id>\d+)/$', 'cms.views.update_doc', name='edit_doc'),
    url(r'^documentos/publicar/(?P<doc_id>\d+)/$', 'cms.views.publish_doc', name='publish_doc'),
    url(r'^documentos/despublicar/(?P<doc_id>\d+)/$', 'cms.views.unpublish_doc', name='hide_doc'),
    url(r'^documentos/eliminar/(?P<doc_id>\d+)/$', 'cms.views.delete_doc', name='remove_doc'),
]
