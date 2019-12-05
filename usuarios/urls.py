from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [

    path('usuario_create/', views.usuario_create, name = 'usuario_create'),
    path('usuario_list/', views.usuario_list, name = 'usuario_list'),
]
