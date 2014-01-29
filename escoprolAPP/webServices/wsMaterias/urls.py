from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('escoprolAPP.webServices.wsMaterias.views',
    url(r'^ws/materias/$' , 'wsMaterias_view', name='ws_materias_url'), #especificar el nombre del metodo de la vista creada
    ) 