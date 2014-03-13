# Create your views here.
from escoprolAPP.alumnos.models import Alumno
from escoprolAPP.matriculas.models import Matricula
from escoprolAPP.cursos.models import Curso
from escoprolAPP.docentes.models import Profesor
from escoprolAPP.matriculas.forms import MatriculaForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
#PAGINACION
from django.core.paginator import Paginator,EmptyPage,InvalidPage
import simplejson

def nueva_matricula(request): 
	alumnos=Alumno.objects.all()
	cursos=Curso.objects.all()
	if request.method=='POST':
		formulario=MatriculaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/listaMatriculas/page/1/')
	else: 
		formulario=MatriculaForm()
	return render_to_response('matriculas/matriculaform.html',{'formulario':formulario,'alumnos':alumnos,'cursos':cursos}, context_instance=RequestContext(request))






def lista_matriculas(request):
	profesores = Profesor.objects.all()
	return render_to_response('matriculas/lista_matriculas.html',{'profesores':profesores},context_instance = RequestContext(request))

def matriculas_view(request,pagina):
	if request.method == "POST":
		if "matricula_id" in request.POST:
			try:
				id_matri = request.POST['matricula_id']
				m = Matricula.objects.get(pk=id_matri )
				mensaje = {"num_horas":"64","matricula_id":m.id}
				m.delete() #Eliminar Matricula
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"num_horas":"120"}
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	


	lista_matri = Matricula.objects.filter().all() #Algo asi como select * from materias where horas=64
	paginator = Paginator(lista_matri,5) #Cuantos elementos quieres por pagina = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		listaMatriculas = paginator.page(page)
	except (EmptyPage,InvalidPage):
		listaMatriculas = paginator.page(paginator.num_pages)

	ctx = {'listaMatriculas':listaMatriculas}
	return render_to_response('matriculas/lista_matriculas.html', ctx, context_instance=RequestContext(request))
