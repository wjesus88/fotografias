from django.forms import ModelForm
from django import forms
from principal.models import Fotografia,Comentario,Album


class FotografiaForm(forms.ModelForm):
	class Meta:
		model=Fotografia
		exclude = ("votos","usuario")

class AlbumForm(forms.ModelForm):
	class Meta:
		model=Album

class ContactoForm(forms.Form):
	correo=forms.EmailField(label='Tu correo electronico')
	mensaje=forms.CharField(widget=forms.Textarea)

