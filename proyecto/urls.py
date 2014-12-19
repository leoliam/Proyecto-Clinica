from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.inicio.urls')),
    url(r'^', include('apps.logistica.urls')),
    url(r'^', include('apps.rr_hh.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, } ),
    )
