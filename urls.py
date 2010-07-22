import os

from django.conf.urls.defaults import *
from django.contrib import admin

from django.conf import settings

import views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^openid/', include('django_openid_auth.urls')),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
    (r'^private/$', views.require_authentication),
)

urlpatterns += patterns('openidtest.main.views',
    url(r'^$',          'index'),
    url(r'^private/$',  'require_authentication'),
)

# For Debugging
if settings.DEBUG:
  urlpatterns += patterns('',
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
  )
