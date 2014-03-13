from django.db import models

# Create your models here.

class Alumno(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=100)
	telefono = models.DecimalField(max_digits=6,decimal_places=0)
	correo= models.EmailField()
 
	def __unicode__(self):
		return self.nombre