from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import CategoriaForm
# Create your views here.
class CategoriaCreate(CreateView):
	model = Categoria
	form_class = CategoriaForm
	success_url = reverse_lazy('cursos:categoria_list')


class CategoriaList(ListView):
	model = Categoria


class CategoriaUpdate(UpdateView):
	model = Categoria
	form_class = CategoriaForm
	success_url = reverse_lazy('cursos:categoria_list')

class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy('cursos:categoria_list')
