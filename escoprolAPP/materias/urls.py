from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('escoprolAPP.materias.views',

	
    url(r'^listaMaterias/page/(?P<pagina>.*)/$' , 'materias_view', name='vista_materias'),
    url(r'^materia/(?P<id_mat>.*)/$', 'singleMateria_view', name='vista_single_materia'),
    url(r'^add/materia/$','add_materia_view', name='vista_agregar_materia'),
    url(r'^edit/materia/(?P<id_mat>.*)/$','edit_materia_view', name='vista_edit_materia'),
    #url(r'^materias/listaMaterias/(?P<nombre>.*)/$','search_materia_view', name='vista_buscar_materia'),

    url(r'^buscar/materias/(?P<nombre>.*)/$','search_materia_view', name='vista_buscar_materia'),

    url(r'^index/$' , 'index_view', name='vista_principal'),
    url(r'^about/$' , 'about_view', name='vista_about'),
    url(r'^contacto/$' , 'contacto_view', name='vista_contacto'),	
    url(r'^login/$' , 'login_view', name='vista_login'),
    url(r'^logout/$' , 'logout_view', name='vista_logout'),
  	
    )