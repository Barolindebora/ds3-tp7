from django.urls import path
from apps.estudiante.views import vista_inicial, vista_estudiantes



urlpatterns =[
    path('', vista_inicial, name='home'),

]
