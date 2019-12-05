from django.urls import path, include
from app import views

urlpatterns = [
    # Index landing page
    path('', views.index_page, name='index'),
]
