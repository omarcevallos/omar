from django.shortcuts import render
from django.shortcuts import render, redirect

from cursos.models import Curso

# Create your views here.
def index_page(request):
    cursos = Curso.objects.all()
    context = {
               'cursos': cursos,
    }
    return render(request, 'frontend/index.html',context)

def inicio(request):

    return render(request, 'backend/index.html')
