# Create your views here.
from escoprolAPP.alumnos.models import Alumno
from escoprolAPP.cursos.models import Curso
from escoprolAPP.docentes.models import Profesor
from escoprolAPP.matriculas.forms import MatriculaForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def nueva_matricula(request):
	if request.user.is_authenticated():
		alumnos=Alumno.objects.all()
		cursos=Curso.objects.all()
		if request.method=='POST':
			formulario=MatriculaForm(request.POST, request.FILES)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect('/lista/matriculas')
		else: 
			formulario=MatriculaForm()
		return render_to_response('matriculas/matriculaform.html',{'formulario':formulario,'alumnos':alumnos,'cursos':cursos}, context_instance=RequestContext(request))
	else:
 		return HttpResponseRedirect('/')

def lista_matriculas(request):
	profesores = Profesor.objects.all()
	return render_to_response('matriculas/lista_matriculas.html',{'profesores':profesores},context_instance = RequestContext(request))