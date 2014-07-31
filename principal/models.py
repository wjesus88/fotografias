#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Fotografia(models.Model):
	titulo = models.CharField(max_length=100, verbose_name='Título', unique=True)
	descripcion = models.TextField(help_text='Redacta la descripcion')	
	imagen = models.ImageField(upload_to='fotografias', verbose_name='Imágen')
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
    fotografia = models.ForeignKey(Fotografia)
    texto = models.TextField(help_text='Tu comentario', verbose_name='Comentario')

    def __unicode__(self):
        return self.texto
