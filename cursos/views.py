from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import Group

from .models import *
from usuarios.forms import UserForm, UserInscripcion
from .models import *
from .forms import CategoriaForm, CursoForm
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

def curso_create(request):
    form = CursoForm()
    if request.method == 'POST':
        form= CursoForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save()
            return redirect('cursos:curso_list')
    context = {
        'form': form,
    }

    return render(request, 'cursos/curso_form.html', context)
class CursoCreate(CreateView):
	model = Curso
	form_class = CursoForm
	success_url = reverse_lazy('cursos:curso_list')


class CursoList(ListView):
	model = Curso


class CursoUpdate(UpdateView):
	model = Curso
	form_class = CursoForm
	success_url = reverse_lazy('cursos:curso_list')

class CursoDelete(DeleteView):
    model = Curso
    success_url = reverse_lazy('cursos:curso_list')


# Create your views here.
@transaction.atomic
def inscripcion_curso(request, pk):
    '''Inscribe a un estudiante desde la pagina index'''
    curso = Curso.objects.get(pk = pk)
    user_form = UserInscripcion()
    if request.method == 'POST':
        user_form = UserInscripcion(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            user.groups.add(Group.objects.get(name='Estudiante'))
            curso.inscritos.add(user)

            messages.success(request, "Inscripcion guardada correctamente.")

            return redirect('index')
        else:
            print("Error Forms")
    context = {
               'curso': curso,
               'user_form': user_form,
    }
    return render(request, 'frontend/inscripcion_form.html', context)
