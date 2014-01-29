from escoprolAPP.alumnos.models import Alumno
from django.forms import ModelForm


class AlumnoForm(ModelForm):
	class Meta:
		model=Alumno


class EditarAlumno(ModelForm):
    class Meta:
        model = Alumno

