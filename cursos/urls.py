from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('inscripcion_curso/<int:pk>/', views.inscripcion_curso, name = 'inscripcion_curso'),
]
