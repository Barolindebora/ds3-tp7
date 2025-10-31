from django.contrib import admin

from .models import Estudiante, Curso


# Register your models here.
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre',)
    list_filter = ('apellido',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_horas')
    search_fields = ('nombre',)