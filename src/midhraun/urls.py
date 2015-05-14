from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

import ui.urls
import horses.urls
import album.urls

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^album/', include(album.urls)),
    url(r'', include(ui.urls)),
    url(r'', include(horses.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
