from django.db import models
from escoprolAPP.cursos.models import Curso
from escoprolAPP.alumnos.models import Alumno
# Create your models here.

class Matricula(models.Model):

	IMP_CHOICES=(
			('1','REGULAR'),
			('2','INRREGULAR'),
			('3','REPETIDOR'), 
		)

	fecha = models.DateField() 
	tipo = models.CharField(max_length=10,choices=IMP_CHOICES)
	alumno =models.ForeignKey(Alumno)
	curso =models.ForeignKey(Curso)

	def __unicode__(self):
		return '%s y %s' %(self.alumno,self.curso)