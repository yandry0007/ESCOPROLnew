from escoprolAPP.matriculas.models import Matricula
from django.forms import ModelForm

class MatriculaForm(ModelForm):
	class Meta:
		model=Matricula