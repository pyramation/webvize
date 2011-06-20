from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
        (r'^signin/$', 'users.views.login'),
        (r'^login/$', 'users.views.login'),
        (r'^signout/$', 'users.views.logout'),
        (r'^signup/$', 'users.views.signUp'),
        (r'^terms/$', 'admin.views.terms'),
        (r'^contact/$', 'admin.views.contact'),
        (r'^$', 'users.views.login'),
        (r'', include('cms.urls')),
)
