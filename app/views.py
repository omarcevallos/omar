from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
def index_page(request):
    return render(request, 'frontend/index.html', {})
