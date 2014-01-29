from django.conf.urls import patterns, url


urlpatterns = patterns('escoprolAPP.alumnos.views',

	url(r'^add/alumno_nuevo/$' , 'nuevo_alumno' , name='nuevos_alumnos'),
    url(r'^add/alumno/$' , 'nuevo_alumno' , name='nuevos_alumnos'),
    url(r'^lista/alumnos/$' , 'lista_alumnos' , name='lista_alumno'),

)