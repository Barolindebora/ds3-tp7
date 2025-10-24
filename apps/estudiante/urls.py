from django.urls import path
from .views import lista_estudiantes, obtener_estudiante_por_id, vista_inicial
from .. import estudiante

app_name = 'estudiante'




urlpatterns = [
    path('',vista_inicial, name='vista_inicial'),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/', obtener_estudiante_por_id, name='obtener_estudiante_por_id'),
]
