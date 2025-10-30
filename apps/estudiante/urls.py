from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, vista_inicial, agregar_estudiante, detalle_curso
from .. import estudiante

app_name = 'estudiante'




urlpatterns = [
    path('',vista_inicial, name='vista_inicial'),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/',detalle_estudiante, name='detalle_estudiante'),
    path('estudiantes/agregar/', agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/curso/<int:pk>/', detalle_curso, name='detalle_curso'),  # vista del curso
]
