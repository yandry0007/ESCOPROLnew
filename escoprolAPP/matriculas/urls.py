from django.conf.urls import patterns, url


urlpatterns = patterns('escoprolAPP.matriculas.views',

    url(r'^add/matricula/$' , 'nueva_matricula' , name='nueva_matricula'),
    url(r'^lista/matriculas/$' , 'lista_matriculas' , name='lista_matricula'),

)