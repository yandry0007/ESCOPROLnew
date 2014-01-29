from django.db import models
from escoprolAPP.docentes.models import Profesor

# Create your models here.
class Curso(models.Model):
	nombre = models.CharField(max_length=50)
	num_creditos=models.IntegerField()

	def __unicode__(self):
		return self.nombre


class Dictar(models.Model):
	fecha_ini = models.DateField() 
	fecha_ter = models.DateField() 
	profesor =models.ForeignKey(Profesor)
	curso =models.ForeignKey(Curso)

	def __unicode__(self):
		return '%s y %s' %(self.profesor,self.curso)
