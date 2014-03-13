from escoprolAPP.matriculas.models import Matricula
from django.forms import ModelForm

class MatriculaForm(ModelForm):
	class Meta:
		model=Matricula


# class MatriculaForm(forms.Form):
# 	fecha = forms.CharField(widget=forms.TextInput())
# 	tipo = forms.CharField(widget=forms.TextInput())
# 	curso = forms.CharField(widget=forms.TextInput())
# 	alumno = forms.CharField(widget=forms.TextInput())
# 	def clean(self):
# 		return self.cleaned_data
