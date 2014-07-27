from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ESCOPROL.views.home', name='home'),
    # url(r'^ESCOPROL/', include('ESCOPROL.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    #ADMIN
    url(r'^admin/', include(admin.site.urls)),


    #ALUMNOS
    url(r'^',include('escoprolAPP.alumnos.urls')),

    #CURSOS
    url(r'^',include('escoprolAPP.cursos.urls')),

    #DOCENTES
    url(r'^',include('escoprolAPP.docentes.urls')),

    #MATERIAS
    url(r'^',include('escoprolAPP.materias.urls')),

    #MATRICULAS
    url(r'^',include('escoprolAPP.matriculas.urls')),

    #USUARIOS
    url(r'^',include('escoprolAPP.usuarios.urls')),

    #WEBSERVICES
    url(r'^',include('escoprolAPP.webServices.wsMaterias.urls')),

    #MEDIA
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),


)
