from django.db import models

# Create your models here.
from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_horas = models.IntegerField()

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    nota_curso = models.DecimalField(max_digits=4, decimal_places=2)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"