from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('realty.views',
    (r'^$', 'index'),
)
urlpatterns += patterns('main.views',
    # Example:
    # (r'^jerusalem_luxury/', include('jerusalem_luxury.foo.urls')),
    (r'^testimage/(?P<image_name>\w+)/$', 'testimage'),

)

urlpatterns += patterns('slideshow.views',
    (r'^slideshow/image_list/(?P<section>\w+)/$', 'image_list'),
)

urlpatterns += patterns('realty.admin_views',
    (r'^admin/realty/property/(?P<property_id>\d+)/$', 'edit_property'),
    (r'^admin/realty/property/add/$', 'add_property'),
)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
