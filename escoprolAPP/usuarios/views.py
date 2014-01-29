# Create your views here.

from django.views.generic import CreateView

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.views.generic import FormView
from .form import UserForm
from .models import Perfiles


class Registrarse(FormView):
	template_name = 'usuarios/registrarUsuario.html' #envio una variable a registrarse y tengo q recogerla ahi
	form_class = UserForm
	success_url = reverse_lazy('registrarsee')

	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.user = user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse , self).form_valid(form)



"""
class RegistrarUsuario(CreateView):
	template_name = 'usuarios/registrarUsuario.html'
	model = Usuario #Vista tipo Autor se cargan todos los atributos de la clase autor 
	success_url = reverse_lazy('registrar_a')
 	
 	def post(self, request, *args, **kwargs):
		estado = False
		autor = Usuario()
		autor.nombre = request.POST['nombre']
		autor.pais = request.POST['pais']
		autor.descripcion = request.POST['descripcion']
		autor.foto =request.FILES['foto']
		autor.save()
		estado = True
		dic = {'estado': estado}
		return render_to_response('usuarios/registrarUsuario.html',dic, context_instance=RequestContext(request))
"""