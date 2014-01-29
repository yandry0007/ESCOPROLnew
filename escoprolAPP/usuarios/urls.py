from django.conf.urls import patterns, include, url

from .views import Registrarse


urlpatterns = patterns('',

 url(r'^$' , 'django.contrib.auth.views.login',
        {'template_name':'usuarios/index.html'}, name = 'login'),

    url(r'^registrar/$' , Registrarse.as_view() , name='registrarsee'),

)
