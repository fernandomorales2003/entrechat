from principal.models import Indumentaria, Calzado
#from principal.forms import ContactForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.mail import EmailMessage

def inicio(request):
	Indumentarias = Indumentaria.objects.all()
	Calzados = Calzado.objects.all()
	return render_to_response('inicio.html',{'Indumentarias':Indumentarias,'Calzados':Calzados})

def indumentarias (request):
	Indumentarias = Indumentaria.objects.all()
	return render_to_response('indumentaria.html',{'Indumentarias':Indumentarias})

def calzados(request):
	Calzados = Calzado.objects.all()
	return render_to_response('calzado.html',{'Calzados':Calzados})

#def Contacto(request):
#	if request.method == 'POST'L
#		formulario = ContactForm(request.POST)
#		if formulario.is.valid():
#			titulo = 'Mensaje desde WEB ENTRECHAT'
#			contenido = formulario.cleaned_data['mensaje'] + "\n"
#			contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
#			correo = EmailMessage(titulo,contenido,to = [entrechat.2013@gmail])
#			correo.send()
#			return HttpResponseRedirect('/')
#	else:
#		formulario = ContactoForm()
#	return render_to_response('contactoform.html',{'formulario':formulario},context_instance=RequestContext(request)
