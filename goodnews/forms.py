from django import forms
from . import models

class Newsform(forms.ModelForm):

	class Meta:
		model = models.News
		fields = ('titulo', 'descricao', 'tipo', 'image',)