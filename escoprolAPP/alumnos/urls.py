from django.conf.urls import patterns, url


urlpatterns = patterns('escoprolAPP.alumnos.views',

	url(r'^listaAlumnos/page/(?P<pagina>.*)/$' , 'alumnos_view', name='vista_alumnos'),
	url(r'^add/alumno_nuevo/$' , 'nuevo_alumno' , name='nuevos_alumnos'),
    url(r'^add/alumno/$' , 'nuevo_alumno' , name='nuevos_alumnos'),
  
) 