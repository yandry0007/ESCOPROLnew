from django.shortcuts import render_to_response
from django.template import RequestContext
from escoprolAPP.materias.forms import ContactForm, LoginForm
from django.contrib.auth import login,logout,authenticate

#PAGINACION
from django.core.paginator import Paginator,EmptyPage,InvalidPage

from escoprolAPP.materias.forms import addProductForm
from escoprolAPP.materias.models import Materia
from django.http import HttpResponseRedirect, HttpResponse
import simplejson

def index_view(request):
	return render_to_response('materias/index.html', context_instance=RequestContext(request))

	
def about_view(request):
	mensaje = "Este es un msj desde la vista"
	ctx = {'msg':mensaje}
	return render_to_response('materias/about.html',ctx, context_instance=RequestContext(request))


def add_materia_view(request):
	info = "Inicializando"
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProductForm(request.POST, request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				num_horas = form.cleaned_data['num_horas']
				descripcion = form.cleaned_data['descripcion']
				foto = form.cleaned_data['foto'] #se obtine con request.FILES
				m = Materia()
				if foto: #Validar la imagen
					m.foto = foto

				m.nombre = nombre
				m.num_horas = num_horas
				m.descripcion = descripcion
				m.foto = foto
				m.save()
				info = "se ha guardado satisfactoriamente"
 			else:
 				info = "informacion con datos incorrecto"
 		form =addProductForm()
 		ctx ={'form':form, 'informacion':info}	
 		return render_to_response('materias/addMateria.html',ctx, context_instance=RequestContext(request))	
 	else:
 		return HttpResponseRedirect('/')


def search_materia_view(request,nombre):
	#resultado = Materia.objects.get(nombre=nombre)
	resultado=Materia.objects.filter(nombre__icontains=nombre).all()
	
	ctx = {'resultado':resultado}
	return render_to_response('materias/listaMaterias.html',ctx,context_instance=RequestContext(request))
		




def materias_view(request,pagina):
	if request.method == "POST":
		if "materia_id" in request.POST:
			try:
				id_mat = request.POST['materia_id']
				m = Materia.objects.get(pk=id_mat )
				mensaje = {"num_horas":"64","materia_id":m.id}
				m.delete() #Eliminar MAterias
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"num_horas":"120"}
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	


	lista_mat = Materia.objects.get_query_set() #Algo asi como select * from materias where horas=64
	paginator = Paginator(lista_mat,5) #Cuantos elementos quieres por pagina = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		listaMaterias = paginator.page(page)
	except (EmptyPage,InvalidPage):
		listaMaterias = paginator.page(paginator.num_pages)

	ctx = {'listaMaterias':listaMaterias}
	return render_to_response('materias/listaMaterias.html', ctx, context_instance=RequestContext(request))

def singleMateria_view(request,id_mat):
	mat = Materia.objects.get(id=id_mat)
	ctx = {'materia':mat}
	return render_to_response('materias/SingleMateria.html',ctx,context_instance=RequestContext(request))



def contacto_view(request):
	info_enviado = False #definir si se envio la info
	
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

	else:

		formulario = ContactForm()
	ctx = {'form':formulario, 'email':email, 'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado }
	return render_to_response('materias/contacto.html', ctx, context_instance=RequestContext(request))


def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')
	else:
		# Ingresar roles
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/index/')
				else:
					mensaje = "usuario y/o password incorrectos"
		form = LoginForm()
		ctx = {'form':form,'mensaje': mensaje}
		return render_to_response('usuarios/index.html' ,ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def edit_materia_view(request,id_mat):
	m = Materia.objects.get(id=id_mat)
	if request.method == 'POST':
		form = addProductForm(request.POST,request.FILES)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			num_horas = form.cleaned_data['num_horas']
			descripcion = form.cleaned_data['descripcion']
			foto = form.cleaned_data['foto']
			m.nombre = nombre
			m.num_horas = num_horas
			m.descripcion = descripcion

			if foto: 			#verifica q la imagen sea correcta
				m.foto = foto

			m.save() #guardamos la info editada
			return  HttpResponseRedirect('/materia/%s'%m.id)


	if request.method == "GET":
		form = addProductForm(initial={
					'nombre':m.nombre,
					'num_horas':m.num_horas,
					'descripcion':m.descripcion,
					'foto':m.foto,

			})
	ctx = {'form':form, 'Materia':m}
	return render_to_response('materias/editMateria.html',ctx,context_instance=RequestContext(request))