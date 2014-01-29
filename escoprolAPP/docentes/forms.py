from escoprolAPP.docentes.models import Profesor
from django.forms import ModelForm

class ProfesorForm(ModelForm):
	class Meta:
		model=Profesor

