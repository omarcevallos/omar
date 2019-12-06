from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('categoria_create/', views.CategoriaCreate.as_view(), name = 'categoria_create'),
    path('categoria_list/', views.CategoriaList.as_view(), name = 'categoria_list'),
	path('categoria_update/<int:pk>/', views.CategoriaUpdate.as_view(), name = 'categoria_update'),
	path('categoria_delete/<int:pk>/delete/', views.CategoriaDelete.as_view(), name='categoria_delete'),
]
