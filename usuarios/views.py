from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def usuario_create(request):
    form = UserForm()

    context = {
        'form': form,
    }

    return render(request, 'usuarios/usuario_create.html', context)


def usuario_list(request):
    usuarios = User.objects.all()
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'usuarios/usuario_list.html', context)
