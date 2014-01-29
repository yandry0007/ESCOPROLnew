from django.db import models
from django.contrib.auth.models import User


class Perfiles(models.Model):

	def url(self, filename):
		ruta = "Fotos/Perfiles/%s/%s"%(self.user.username,str(filename))
		return ruta

	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to=url)
	telefono = models.CharField(max_length=30)


	def __unicode__(self):
		return self.user.username

"""
class Usuario(models.Model):

	def url(self, filename):
		ruta = "Fotos/Users/%s/%s"%(self.nombre,str(filename))
		return ruta
	nombre = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	foto = models.ImageField(upload_to=url)

	def __unicode__(self):
		return self.nombre

"""