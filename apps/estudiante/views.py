from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Estudiante


# Create your views here.
def vista_inicial (request):
    return HttpResponse("<h1>Inicialización de estudiantes</h1>")

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request,'estudiante/lista.html', {'estudiantes':estudiantes})


def obtener_estudiante_por_id(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudiante/estudianteId.html', {'estudiante': estudiante})

