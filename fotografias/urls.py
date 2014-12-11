from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','principal.views.inicio'),
    # Examples:
    # url(r'^$', 'fotografias.views.home', name='home'),
    # url(r'^fotografias/', include('fotografias.foo.urls')),  
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^album/(\d+)$', 'principal.views.album', name='album'),
    url(r'^plus/(\d+)$', 'principal.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'principal.views.minus', name='minus'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
    url(r'^album/nueva/$','principal.views.nueva_album'),  
    url(r'^fotografia/nueva/$','principal.views.nueva_fotografia'),
    url(r'^fotografias/$','principal.views.lista_fotografias'),
    url(r'^contacto/$','principal.views.contacto'),
    url(r'^fotografia/(?P<id_fotografia>\d+)$','principal.views.detalle_fotografia'),
    url(r'^fotografia/delete/(?P<id>\d+)', 'principal.views.delete'),
    url(r'^fotografia/edit/(?P<id>\d+)', 'principal.views.edit'),
    url(r'^fotografia/update/(?P<id>\d+)', 'principal.views.update'),
    #url(r'^update/(?P<id>\d+)$', 'update', name='update'),
    # url(r'^fotografiadelete/(?P<id_fotografia>\d+)$','principal.views.delete_fotografia'),
    url(r'^admin/', include(admin.site.urls)),
)
