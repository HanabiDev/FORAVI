from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'finantial.views.home', name='finantial_home'),

    url(r'^cargar/$', 'finantial.views.load_reports', name='load'),
    url(r'^cargar-asociados/$', 'finantial.views.load_clients', name='load_clients'),
    url(r'^cargar-prestamos/$', 'finantial.views.load_credits', name='load_credits'),
    url(r'^cargar-depositos/$', 'finantial.views.load_deposits', name='load_deposits'),


    url(r'^documentos/$', 'cms.views.index_docs', name='docs_index'),
    url(r'^documentos/buscar/$', 'cms.views.search_docs', name='search_docs'),
    url(r'^documentos/nuevo/$', 'cms.views.create_doc', name='new_doc'),
    url(r'^documentos/editar/(?P<doc_id>\d+)/$', 'cms.views.update_doc', name='edit_doc'),
    url(r'^documentos/publicar/(?P<doc_id>\d+)/$', 'cms.views.publish_doc', name='publish_doc'),
    url(r'^documentos/despublicar/(?P<doc_id>\d+)/$', 'cms.views.unpublish_doc', name='hide_doc'),
    url(r'^documentos/eliminar/(?P<doc_id>\d+)/$', 'cms.views.delete_doc', name='remove_doc'),
]
