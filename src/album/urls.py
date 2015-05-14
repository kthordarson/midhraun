from django.conf.urls import patterns, url


urlpatterns = patterns('album.views',
    url(r'^$', 'list_all'),
)
