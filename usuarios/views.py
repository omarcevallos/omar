from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def usuario_create(request):
    form = UserForm()
    if request.method == 'POST':
        form= UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('usuarios:usuario_list')
    else:
        context = {
            'form': form,
            'titulo': 'Crear Usuario'
        }

    return render(request, 'usuarios/usuario_create.html', context)


def usuario_list(request):
    usuarios = User.objects.all()
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'usuarios/usuario_list.html', context)

def usuario_edit(request, pk):
    usuario = User.objects.get(pk=pk)
    usuario_form = UserForm(instance = usuario)
    if request.method == "POST":
        usuario_form = UserForm(request.POST, instance=usuario)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('usuarios:usuarios_list')
    context = {
        'form': usuario_form,
        'titulo': 'Editar Usuario'
    }

    return render(request, 'usuarios/usuario_create.html', context)


def usuario_delete(request, pk):
    usuario = User.objects.get(pk=pk)
    usuario.delete()
    return redirect('usuarios:usuario_list')
