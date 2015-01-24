from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'openshift.DjangoFilms.views.register'),
    url(r'^ok/$', 'openshift.DjangoFilms.views.ok'),
    url(r'^login/$', 'openshift.DjangoFilms.views.login'),
    url(r'^comprobar/$', 'openshift.DjangoFilms.views.comprobar'),

)
