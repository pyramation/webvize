from django.conf.urls.defaults import *

urlpatterns = patterns('cms.views.pages',
        url(r'^pages/(?P<page_id>\d+)/edit/$', 'edit', name='edit_page'),
        url(r'^pages/(?P<page_id>\d+)/$', 'show', name='page'),
        url(r'^pages/create/$', 'create', name='create_page'),
        url(r'^pages/$', 'index', name='pages'),
)

