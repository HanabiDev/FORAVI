from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'frontend.views.home', name='home'),

    url(r'contacto/$', 'frontend.views.send_webmail', name='send_mail'),

    url(r'servicios/simuladores/$', 'frontend.views.show_simulators', name='simulators'),
    url(r'servicios/(?P<service>[-\w]+)/$', 'frontend.views.service', name='services'),

    url(r'noticias/$', 'frontend.views.index_news', name='news_index'),
    url(r'noticias/(?P<slug>[-\w]+)/$', 'frontend.views.show_post', name='post'),
    url(r'normatividad/$', 'frontend.views.index_documents', name='docs_index'),
    url(r'normatividad/(?P<slug>[-\w]+)/$', 'frontend.views.show_document', name='doc'),
    url(r'comentar/(?P<content_id>\d+)/$', 'frontend.views.add_comment', name='send_comment'),
    url(r'editar-comentario/(?P<comment_id>\d+)/$', 'frontend.views.update_comment', name='edit_comment'),
    url(r'eliminar-comentario/(?P<comment_id>\d+)/$', 'frontend.views.delete_comment', name='remove_comment'),

    url(r'(?P<page>[-\w]+)/$', 'frontend.views.load_static_page', name='static_page'),
]


