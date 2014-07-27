from django.conf.urls import patterns, url


urlpatterns = patterns('escoprolAPP.docentes.views',

    url(r'^add/profesor/$' , 'nuevo_profesor' , name='nuevos_profesores'),
    url(r'^lista/profesores/$' , 'lista_profesores' , name='lista_profesor'),

) 