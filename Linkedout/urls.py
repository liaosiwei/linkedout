from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'linker.views.home', name='home'),
    url(r'^setting/$', 'linker.views.setting'),
    url(r'^ajaxAddUrl/$', 'linker.views.ajaxAddUrl'),
    url(r'^ajaxDelUrl/$', 'linker.views.ajaxDelUrl'),
    url(r'^autoComplete/$', 'linker.views.autoComplete'),
    url(r'^downloadXml/$', 'linker.views.downloadXml'),
    url(r'^ajaxUpdateTips/$', 'linker.views.ajaxUpdateTips'),
    url(r'^ajaxUpdateVotes/$', 'linker.views.ajaxUpdateVotes'),
    url(r'^ajaxSearch/$', 'linker.views.ajaxSearch'),
#     url(r'^ajaxAddSearchItem', 'linker.views.ajaxAddSearchItem'),
    url(r'^', include('auths.urls')),
    # url(r'^Linkedout/', include('Linkedout.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
