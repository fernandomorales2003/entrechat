from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'entrechat.views.home', name='home'),
    # url(r'^entrechat/', include('entrechat.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','principal.views.inicio'),
    url(r'^indumentarias/$','principal.views.indumentarias'),
    url(r'^calzados/$','principal.views.calzados'),
    url(r'^contacto/', include('contact_form.urls')),
)
