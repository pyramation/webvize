from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
        (r'^login/$', 'cms.views.users.userLogin'),
        (r'', include('cms.urls')),
)

