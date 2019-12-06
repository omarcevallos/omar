from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import Group

from .models import *
from usuarios.forms import UserForm, UserInscripcion

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
