from django.conf.urls.defaults import *

urlpatterns = patterns('ajax.views.pages',
    url(r'^pages/create/$', 'create', name='ajax_create_page'),
    url(r'^pages/delete/$', 'delete', name='ajax_delete_page'),
    url(r'^pages/edit/$', 'edit', name='ajax_edit_page'),
)

