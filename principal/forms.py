from django.forms import ModelForm
from django import forms
from principal.models import Fotografia,Comentario


class FotografiaForm(ModelForm):
	class Meta:
		model=Fotografia

class ContactoForm(forms.Form):
	correo=forms.EmailField(label='Tu correo electronico')
	mensaje=forms.CharField(widget=forms.Textarea)