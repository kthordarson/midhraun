from django.conf.urls import patterns, url


urlpatterns = patterns('ui.views',
    url(r'^home/$', 'home'),
    url(r'^$', 'index'),
)
