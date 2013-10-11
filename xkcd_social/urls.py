from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xkcd_social.views.home', name='home'),
    # url(r'^xkcd_social/', include('xkcd_social.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^xkcd_social/(?P<page_id>[^/]+)/$', 'xkcd_comments.views.view_page'),
    url(r'^xkcd_social/(?P<page_id>[^/]+)/save_comment/$', 'xkcd_comments.views.save_comment'),
    url('accounts/login/$', 'xkcd_social.views.login'),
    url('accounts/logout/$', 'xkcd_social.views.logout'),
    url('accounts/auth/(?P<page_id>[^/]+)$', 'xkcd_social.views.auth_view'),
    url('accounts/loggedin/$', 'xkcd_social.views.loggedin'),
    url('accounts/invalid/$', 'xkcd_social.views.invalid_login'),
    url('accounts/register/$', 'xkcd_social.views.register_user'),
    url('accounts/register_success/$', 'xkcd_social.views.register_success'),
)
