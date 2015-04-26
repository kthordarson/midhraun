from django.conf.urls import patterns, url


urlpatterns = patterns('horses.views',
    url(r'log/(?P<horse_id>[0-9]+)/$', 'log'),
    url(r'^horses/new$', 'new_horse'),
)
