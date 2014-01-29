from django.db import models

class Materia(models.Model):

	def url(self, filename):
		ruta = "Fotos/Materias/%s/%s"%(self.nombre,str(filename))
		return ruta


	nombre = models.CharField(max_length=200)
	num_horas = models.CharField(max_length=10)
	descripcion = models.TextField(max_length=100)
	foto = models.ImageField(upload_to = url, null=True, blank=True)

	def __unicode__(self):
		return self.nombre