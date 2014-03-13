# Create your views here.
from escoprolAPP.alumnos.models import Alumno
from escoprolAPP.matriculas.models import Matricula
from escoprolAPP.alumnos.forms import AlumnoForm, EditarAlumno
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
#PAGINACION
from django.core.paginator import Paginator,EmptyPage,InvalidPage
import simplejson

 
def alumnos_view(request,pagina):
	if request.method == "POST": 
		if "alumno_id" in request.POST:
			try:
				id_alu = request.POST['alumno_id']
				a = Alumno.objects.get(pk=id_alu )
				mensaje = {"num_horas":"64","alumno_id":a.id}
				a.delete() #Eliminar Alumnos
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"num_horas":"120"}
				return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	


	lista_alu = Alumno.objects.filter().all() #Algo asi como select * from materias where horas=64
	paginator = Paginator(lista_alu,5) #Cuantos elementos quieres por pagina = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		listaAlumnos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		listaAlumnos = paginator.page(paginator.num_pages)

	ctx = {'listaAlumnos':listaAlumnos}
	return render_to_response('alumnos/lista_alumnos.html', ctx, context_instance=RequestContext(request))






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
				return HttpResponseRedirect('/listaAlumnos/page/1/')
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