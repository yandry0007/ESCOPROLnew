from escoprolAPP.cursos.models import Curso
from django.forms import ModelForm

class CursoForm(ModelForm):
	class Meta:
		model=Curso