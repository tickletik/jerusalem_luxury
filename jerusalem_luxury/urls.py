from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('main.views',
    # Example:
    # (r'^jerusalem_luxury/', include('jerusalem_luxury.foo.urls')),
    (r'^$', 'index'),
    (r'^test/$', 'test'),
    (r'^testimage/(?P<image_name>\w+)/$', 'testimage'),

)

urlpatterns += patterns('rotating_gallery.views',
    (r'^rotating/image_list/(?P<section>\w+)/$', 'image_list'),
)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
