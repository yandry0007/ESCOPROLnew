from django.db import models
from escoprolAPP.matriculas.models import Matricula
# Create your models here.
class Nota(models.Model):
	IMP_CHOICES=(
			('1','PARCIAL I'),
			('2','PARCIAL II'),
			('3','PARCIAL III'),
		)
	valor =models.IntegerField()
	fecha = models.DateField() 
	trimestre= models.CharField(max_length=5,choices=IMP_CHOICES)
	matricula=models.ForeignKey(Matricula)

	def __unicode__(self):
		return '%s y %s' %(self.valor,self.trimestre)
