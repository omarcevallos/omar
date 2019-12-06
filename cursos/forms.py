from django import forms
from .models import *

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        # fields = '__all__'
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        # fields = '__all__'
        fields = '__all__'
        widgets = {
            'resumen': forms.Textarea(attrs={'rows':2}),
            'requisitos':forms.Textarea(attrs={'rows':2}),
            'fecha': forms.DateInput(attrs = {'type':"date"})
        }
