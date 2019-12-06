from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
    	return self.nombre

class Curso(models.Model):
    categoria = models.ForeignKey(Categoria,  on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    resumen = models.TextField()
    requisitos = models.TextField()
    image = models.ImageField(upload_to = 'static/img/curso')
    profesor = models.ForeignKey(User,  on_delete=models.CASCADE)
    fecha = models.DateField()
    cupos = models.IntegerField()
    inscritos = models.ManyToManyField(User, related_name="inscritos")

    def __str__(self):
    	return self.titulo

class Inscripcion(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,  on_delete=models.CASCADE)

    def __str__(self):
    	return self.user
