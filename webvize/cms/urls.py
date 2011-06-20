from django.conf.urls.defaults import *

urlpatterns = patterns('cms.views.users',
        (r'^$', 'userLogin'),
        (r'^login/$', 'userLogin'),
        (r'^users/forgot/$', 'userForgot'),
        (r'^users/signup/$', 'userSignUp'),
)

urlpatterns += patterns('cms.views.pages',
        (r'^pages/(?P<page_id>\d+)/edit/$', 'edit'),
        (r'^pages/(?P<page_id>\d+)/$', 'show'),
        (r'^pages/create/$', 'create'),
        (r'^pages/$', 'index'),
)

