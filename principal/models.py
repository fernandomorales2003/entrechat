#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Indumentaria(models.Model):
  titulo = models.CharField(max_length=100, unique=True)
  color = models.CharField(max_length=100, unique=False)
  descripcion = models.TextField(help_text='descripcion')
  imagen = models.ImageField(upload_to='indumentaria', verbose_name='Imagen')
  tiempo_registro = models.DateTimeField(auto_now=True)
  usuario = models.ForeignKey(User)

  def __unicode__(self):
    return self.titulo

class Calzado(models.Model):
  titulo = models.CharField(max_length=100, unique=True)
  color = models.CharField(max_length=100, unique=False)
  descripcion = models.TextField(help_text='descripcion')
  imagen = models.ImageField(upload_to='calzado', verbose_name='Imagen')
  tiempo_registro = models.DateTimeField(auto_now=True)
  usuario = models.ForeignKey(User)

  def __unicode__(self):
    return self.titulo

#class ContacForm(forms.Form):
#  correo =forms.EmailField(label='entrechat.2013@gmail.com')
#  mensaje = forms.CharField(widget=forms.Textarea)