from django.urls import path
from .views import lista_estudiantes
from .. import estudiante

app_name = 'estudiante'
urlpatterns =[
    path('',lista_estudiantes , name='Lista_estudiantes'),
    path('<int:pk>',lista_estudiantes, name='Lista_estudiantes_pk'),
]

