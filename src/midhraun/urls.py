from django.conf.urls import patterns, include, url
from django.contrib import admin

import ui.urls

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(ui.urls)),
)
