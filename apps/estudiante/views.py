from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import EstudianteForm
from .models import Curso

from .models import Estudiante


# Create your views here.
def vista_inicial (request):
    return HttpResponse("<h1>Inicialización de estudiantes</h1>")

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.prefetch_related('cursos').all()
    return render(request, 'estudiante/lista.html', {'estudiantes': estudiantes})


def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudiante/estudianteId.html', {'estudiante': estudiante})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()  # guarda el nuevo estudiante con los cursos seleccionados
            return render(request, 'estudiante/confirmacion.html', {'form': form})
    else:
        form = EstudianteForm()

    return render(request, 'estudiante/agregar.html', {'form': form})

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    estudiantes = curso.estudiantes.all()
    return render(request, 'estudiante/detalle_curso.html', {
        'curso': curso,
        'estudiantes': estudiantes
    })
