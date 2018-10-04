from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
import random
from datetime import date
from django.urls import reverse_lazy

from . import models, forms


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CreateNews(generic.CreateView):
    form_class = forms.Newsform
    success_url = reverse_lazy('home')
    template_name = 'createnews.html'
    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.user = models.User.objects.get(id=self.request.user.pk)
    	obj.save()
    	return super(CreateNews, self).form_valid(form)

class Internacional(generic.ListView):
	template_name = 'internacional.html'
	def get_queryset(self):
		lista = []
		for x in models.News.objects.all():
			if(x.tipo == 2):
				lista.append(x)
		lista.reverse()
		return lista

class Regional(generic.ListView):
	template_name = 'regional.html'
	def get_queryset(self):
		lista = []
		for x in models.News.objects.all():
			if(x.tipo == 1):
				lista.append(x)
		lista.reverse()
		return lista

class Home(generic.ListView):
	template_name = 'home.html'
	def get_queryset(self):
		lista = []
		for x in models.News.objects.all():
			lista.append(x)
		lista.reverse()
		return lista