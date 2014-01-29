from escoprolAPP.docentes.forms import ProfesorForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from escoprolAPP.docentes.models import Profesor

def nuevo_profesor(request):
		if request.user.is_authenticated():
			if request.method=='POST':
				formulario=ProfesorForm(request.POST, request.FILES)
				if formulario.is_valid():
					formulario.save()
					return HttpResponseRedirect('/lista/profesores')
			else:
				formulario=ProfesorForm()
			return render_to_response('docentes/profesorform.html',{'formulario':formulario}, context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/index/')

def lista_profesores(request):
	profesores = Profesor.objects.all()
	return render_to_response('docentes/lista_profesores.html',{'profesores':profesores},context_instance = RequestContext(request))
