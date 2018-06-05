from django.conf.urls import url


urlpatterns = [
    # list of all bookmarks from a particular person
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),
    # simple list view of all public bookmarks
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list')
]
