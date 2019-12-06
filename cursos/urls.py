from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('categoria_create/', views.CategoriaCreate.as_view(), name = 'categoria_create'),
    path('categoria_list/', views.CategoriaList.as_view(), name = 'categoria_list'),
	path('categoria_update/<int:pk>/', views.CategoriaUpdate.as_view(), name = 'categoria_update'),
	path('categoria_delete/<int:pk>/delete/', views.CategoriaDelete.as_view(), name='categoria_delete'),
    path('curso_create/', views.curso_create, name = 'curso_create'),
    path('curso_list/', views.CursoList.as_view(), name = 'curso_list'),
	path('curso_update/<int:pk>/', views.CursoUpdate.as_view(), name = 'curso_update'),
	path('curso_delete/<int:pk>/delete/', views.CursoDelete.as_view(), name='curso_delete'),
    path('inscripcion_curso/<int:pk>/', views.inscripcion_curso, name = 'inscripcion_curso'),
]
