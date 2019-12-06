from django.contrib import admin

from .models import *

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = (
                    'id',
                    'categoria',
                    'titulo',
                    'image',
                    'profesor',
                    'fecha',
                    'cupos'
                    )
admin.site.register(Curso, CursoAdmin)

class CateroriaAdmin(admin.ModelAdmin):
    list_display = (
                    'nombre',
                    'activo'
    )
admin.site.register(Categoria, CateroriaAdmin)
