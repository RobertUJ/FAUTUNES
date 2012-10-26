from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('djapp.apps.users.views',
	url(r'^petition/$','petitions',name='petitions_view'),
	url(r'^dj/$','get_peticiones',name='get_peticiones_view'),
)
