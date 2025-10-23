from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from apps.estudiante.models import Estudiante


# Create your views here.
def vista_inicial (request):
    return HttpResponse("<h1>Inicialización de estudiantes</h1>")

def estudiantes_lista(request):
    estudiantes = Estudiante.objects.all()
    return render(request,'estudiante/lista.html', {'estudiantes':estudiantes})


