from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djapp.views.home', name='home'),
    # url(r'^djapp/', include('djapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^',include('djapp.apps.home.urls')),
    url(r'^',include('djapp.apps.users.urls')),
    # url(r'^',include('djapp.apps.dj.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
