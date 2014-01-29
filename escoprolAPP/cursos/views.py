# Create your views here.

from escoprolAPP.cursos.models import Curso
from escoprolAPP.matriculas.models import Matricula
from escoprolAPP.cursos.forms import CursoForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def lista_cursos(request):
	cursos = Curso.objects.all()
	return render_to_response('cursos/lista_cursos.html',{'cursos':cursos},context_instance = RequestContext(request))


def dato_curso(request, id_curso):
	dato = Curso.objects.get(pk=id_curso)
	dato2 = Matricula.objects.filter(curso=id_curso)	
	return render_to_response('cursos/dato_curso.html',{'curso':dato,'alumnos_matriculados':dato2},context_instance = RequestContext(request))


def nuevo_curso(request):
	if request.method=='POST':
		formulario=CursoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/add/curso/')
	else: 
		formulario=CursoForm()
	return render_to_response('cursos/cursoform.html',{'formulario':formulario}, context_instance=RequestContext(request))