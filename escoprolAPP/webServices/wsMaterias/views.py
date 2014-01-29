# Create your views here.
from django.http import HttpResponse
from escoprolAPP.materias.models import Materia
#Integramos la serializacion de objetos
from django.core import serializers

def wsMaterias_view(request):
	data = serializers.serialize("json", Materia.objects.get_query_set())
	#retorna la info en formato json
	return HttpResponse(data,mimetype='aplication/json')
