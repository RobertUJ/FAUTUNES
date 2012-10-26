from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('djapp.apps.dj.views',
	url(r'^accounts/login/$','login_view',name='view_login'),
)
