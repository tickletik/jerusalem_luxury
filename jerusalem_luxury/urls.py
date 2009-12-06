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
        (r'^block_view/(?P<object_id>\d+)/$', 'building.views.edit_block'),

        (r'^test/block/(?P<object_id>\d+)/$', 'building.views.edit_block'),
        (r'^test/block/add/$', 'building.views.add_block'),

        (r'^admin/building/block/(?P<object_id>\d+)/$', 'building.views.edit_block'),
        (r'^admin/building/block/add/$', 'building.views.add_block'),

        (r'^admin/nested/lower2/(?P<id_lower>\d+)/$', 'nested.admin_views.lower'),
        (r'^admin/nested/lower2/add/$', 'nested.admin_views.lower'),
)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
