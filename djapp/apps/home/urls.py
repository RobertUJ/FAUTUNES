from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('djapp.apps.home.views',
	url(r'^$','home',name='home_view'),
)
