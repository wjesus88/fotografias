from principal.models import Fotografia
from principal.forms import FotografiaForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.template import RequestContext


def inicio(request):
	fotos=Fotografia.objects.all()
	return render_to_response('inicio.html',{'fotos':fotos})


def lista_fotografias(request):
	fotografias=Fotografia.objects.all()
	return render_to_response('fotografias.html',{'datos':fotografias},context_instance=RequestContext(request))


def nueva_fotografia(request):
	if request.method=='POST':
		formulario=FotografiaForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/fotografias')
	else:
		formulario=FotografiaForm()
	return render_to_response('fotografiaform.html',{'formulario':formulario},context_instance=RequestContext(request))
