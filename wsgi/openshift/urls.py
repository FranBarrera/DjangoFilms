from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '../static/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'openshift.DjangoFilms.views.register'),
    url(r'^$', 'openshift.DjangoFilms.views.login'),
    url(r'^check/$', 'openshift.DjangoFilms.views.check'),
    url(r'^pelicula/$', 'openshift.DjangoFilms.views.info'),
    url(r'^peliculas/(?P<api>[0-9]{0,9})/$', 'openshift.DjangoFilms.views.envia_info_peli'),
    url(r'^series/(?P<api>[0-9]{0,9})/$', 'openshift.DjangoFilms.views.envia_info_serie'),
    url(r'^series/(?P<api>[0-9]{0,9})/(?P<season>[0-9]{0,9})/$', 'openshift.DjangoFilms.views.envia_seasons'),


#    url(r'^peliculas/(?P<api>[0-9]{0,9})/vista$', 'openshift.DjangoFilms.views.insert_media'),
    url(r'^peliculas/(?P<api>[0-9]{0,9})/vista$', 'openshift.DjangoFilms.views.vista'),
    url(r'^peliculas/(?P<api>[0-9]{0,9})/pendiente$', 'openshift.DjangoFilms.views.pendiente'),
    url(r'^peliculas/vistas$', 'openshift.DjangoFilms.views.user_vistas'),
    url(r'^peliculas/pendientes$', 'openshift.DjangoFilms.views.user_pendientes'),


 #   url(r'^peliculas/245891/$', 'openshift.DjangoFilms.views.info_peli'),



)
