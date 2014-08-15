from principal.models import Fotografia,Comentario
from principal.forms import FotografiaForm,ContactoForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def inicio(request):
	fotos=Fotografia.objects.all()
	return render_to_response('inicio.html',{'fotos':fotos},context_instance=RequestContext(request))


def lista_fotografias(request):
	fotografias=Fotografia.objects.all()
	return render_to_response('fotografias.html',{'datos':fotografias},context_instance=RequestContext(request))


def nueva_fotografia(request):
	if request.method=='POST':
		formulario=FotografiaForm(request.POST,request.FILES)
		print formulario
		
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/fotografias')
	else:
		formulario=FotografiaForm()
	return render_to_response('fotografiaform.html',{'formulario':formulario},context_instance=RequestContext(request))


def detalle_fotografia(request, id_fotografia):
    dato = get_object_or_404(Fotografia, pk=id_fotografia)
    comentarios = Comentario.objects.filter(fotografia=dato)
    return render_to_response('fotografia.html',{'fotografia':dato,'comentarios':comentarios}, context_instance=RequestContext(request))


# def delete_fotografia(request, id_fotografia):
def delete(request, id):
    Fotografia.objects.get(id=id).delete()
    #return list(request, message="Link deleted!") 
    return HttpResponseRedirect('/fotografias')


def edit(request, id):
    foto = Fotografia.objects.get(id=id)
    return render_to_response(
        'editarfotografia.html',
        {'action': 'update/' + id,
        'button': 'Update',
        'descripcion': foto.descripcion,
        'titulo': foto.titulo
        },context_instance=RequestContext(request)
    )


def update(request, id):
    foto = Fotografia.objects.get(id=id)
 
    foto.descripcion = request.POST["description"]
    foto.titulo = request.POST["titulo"]
    print foto
    #foto.save()
    return list(request, message='foto')


def contacto(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje desde el recetario de Maestros del Web'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to=['destinatario@email.com'])
			correo.send()			
			return 	HttpResponseRedirect('/')
	else:
		formulario=ContactoForm()

	return render_to_response('contactoform.html',{'formulario':formulario},context_instance=RequestContext(request))


