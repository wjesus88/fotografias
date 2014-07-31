from django.forms import ModelForm
from django import forms
from principal.models import Fotografia,Comentario


class FotografiaForm(ModelForm):
	class Meta:
		model=Fotografia