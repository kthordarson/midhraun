from django.conf.urls import patterns, url


urlpatterns = patterns('ui.views',
    url(r'^home/$', 'home'),
    url(r'^categories/$', 'categories'),
    url(r'^horses/new$', 'new_horse'),
    url(r'^$', 'index'),
)
