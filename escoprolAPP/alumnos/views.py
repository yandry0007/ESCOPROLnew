# Create your views here.
from escoprolAPP.alumnos.models import Alumno
from escoprolAPP.matriculas.models import Matricula
from escoprolAPP.alumnos.forms import AlumnoForm, EditarAlumno
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def lista_alumnos(request):
	alumnos = Alumno.objects.all()
	return render_to_response('alumnos/lista_alumnos.html',{'alumnos':alumnos},context_instance = RequestContext(request))


def dato_alumno(request, id_alumno):	
	dato = Alumno.objects.get(pk=id_alumno)
	dato2 = Matricula.objects.filter(alumno=id_alumno)
	return render_to_response('alumnos/dato_alumno.html',{'alumno':dato,'cursos_matriculados':dato2},context_instance = RequestContext(request))

def nuevo_alumno(request):
	if request.user.is_authenticated():
		if request.method=='POST':
			formulario=AlumnoForm(request.POST, request.FILES)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect('/lista/alumnos')
		else: 
			formulario=AlumnoForm()
		return render_to_response('alumnos/alumnoform.html',{'formulario':formulario}, context_instance=RequestContext(request))
	else:
			return HttpResponseRedirect('/')


@login_required
def editar_alumno(request, object_id):
    try:
        alumno = Alumno.objects.get(id = object_id)

    except Alumno.DoesNotExist:
        pass

    if request.POST:
        form = EditarAlumno(request.POST, instance = alumno)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/alumnos/')
        else:
            form = EditarAlumno(instance = alumno)

    return render_to_response("alumnos/editar_alumno.html", {"alumno": alumno, 'form': form})