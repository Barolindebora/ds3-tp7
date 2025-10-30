from django import forms
from .models import Estudiante, Curso

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'edad', 'nota_curso', 'cursos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota_curso': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cursos': forms.CheckboxSelectMultiple(),  # para seleccionar varios cursos
        }