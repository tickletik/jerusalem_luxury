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

urlpatterns += patterns('slideshow.views',
    (r'^slideshow/image_list/(?P<section>\w+)/$', 'image_list'),
)

urlpatterns += patterns('',
        (r'^admin/nested/lower/(?P<id_lower>\d+)/$', 'nested.admin_views.lower'),
        (r'^admin/nested/lower/add/$', 'nested.admin_views.lower'),
)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
