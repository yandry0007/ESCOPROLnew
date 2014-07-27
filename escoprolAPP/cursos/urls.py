from django.conf.urls import patterns, url


urlpatterns = patterns('escoprolAPP.cursos.views',

	url(r'^add/curso_nuevo/$' , 'nuevo_curso' , name='nuevos_cursos'),
    url(r'^add/curso/$' , 'nuevo_curso' , name='nuevos_cursos'),
    url(r'^lista/cursos/$' , 'lista_cursos' , name='lista_curso'),

)