from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'frontend.views.home', name='home'),
    url(r'^noticias/$', 'frontend.views.index_news', name='news_index'),
    url(r'^noticias/(?P<slug>[-\w]+)/$', 'frontend.views.show_post', name='post'),
]
