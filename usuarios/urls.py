from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [

    path('usuario_create/', views.usuario_create, name = 'usuario_create'),
    path('usuario_list/', views.usuario_list, name = 'usuario_list'),
    path('usuario_edit/<int:pk>/', views.usuario_edit, name = 'usuario_edit'),
    path('usuario_delete/<int:pk>/', views.usuario_delete, name = 'usuario_delete'),
]
