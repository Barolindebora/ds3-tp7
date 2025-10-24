
1.Crear un directorio donde se creara el entorno virtual, posicionarse en el directorio ejecutar: python -m venv nombre_del_entorno (se sugiere que tenga el mismo nombre que el proyecto)...

2.A continuacion activar el entorno virtual ejecutando: nombre_del_entorno\Scripts\activate

3.Instalar setuptools con: pip install setuptools

4.Instalar django con: pip install django

Finalizadas las instalaciones, volvemos al directorio raiz y creamos un proyecto de django

Ejecutar: django-admin startproject nombre_del_proyecto

No olvidar hacer un .gitignore Contenido sugerido: venv/ env/ entorno_virtual/ (el nombre que tenga tu entorno vitual) */pycache/ *.py[cod]

Base de datos local
*.sqlite3

Configuración sensible
.env

###Archivos del sistema .DS_Store Thumbs.db

Configuración del IDE
.idea/ .vscode/

Archivos de migraciones (opcional)
*/migrations/pycache/

BASE DE DATOS--
Instalar el conector de PostgreSQL en tu entorno virtual

Abrí la terminal de PyCharm (asegurate de tener activado tu entorno virtual) y ejecutá:

pip install psycopg2-binary

Este paquete es el driver que Django usa para conectarse con PostgreSQL.

Configurar la base de datos en sttings.py

DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'gestor_estudiantes_db', # nombre de la base que creaste 'USER': 'postgres', # tu usuario de PostgreSQL 'PASSWORD': 'contraseña', # la contraseña que usás en pgAdmin 'HOST': 'localhost', # servidor local 'PORT': '5432', # puerto por defecto de PostgreSQL } } para mandar la info se hace python manage.py migrate

PARA GUARDAR LOS REQUERIMIENTOS
pip freeze y cuando clonamos hacemos pip install -r requirements.txt

DESACOPLAR LAS VARIABLES
pip install python-decouple

agregar a los requerimientos

en settings.py importar: from decouple import config Y HACER LAS CONEXIONES ENTRE EL ENV Y EL SETTINGS.PY

CORRER EL SERVIDOR
python manage.py runserver

CREAR UNA APP
Ejecutar: python manage.py startapp nombre_app

En cada app hay un archivo models.py donde se crean los modelos.

si ponemos una columna fecha podemos poner models.DateTimeField(auto_now_add=True)

CREAR UN USUARIO ANTES DE HACER LA PRIMERA MIGRATION
Cuando haces un usuario personalizado tenes que poner en settings lo siguiente para que tome el modelo personalizado y no el implicito de usuario

AUTH_USER_MODEL= 'aplicacion.modelo'

La clase usuario hereda de abstractUser no me models como cuando creas un modelo

MODELOS
Relaciones 1 a 1 - 1 a muchos - muchos a muchos: en el modelo es 🔹 Relación 1 a 1

👉 Un registro se asocia con uno solo en la otra tabla. 📘 Ejemplo: un estudiante tiene un solo perfil.

perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)

🔹 Relación 1 a muchos

👉 Un registro puede tener muchos relacionados, pero cada uno pertenece a uno solo. 📘 Ejemplo: un curso tiene muchos estudiantes.

curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

🔹 Relación muchos a muchos

👉 Varios registros pueden estar relacionados entre sí en ambos sentidos. 📘 Ejemplo: un estudiante puede estar en varios cursos, y un curso tener varios estudiantes.

cursos = models.ManyToManyField(Curso)

on_delete=models.SET_NULL para que no se elimine su relacion on_delete=models.CASCADE se elimina todo-

LA RELACION SE PONE EN EL LADO DE UNO EN UNO A MUCHOS

las migraciones se hacen con los dos comandos

hay que salir de la consola para hacer las migraciones. 

python manage.py makemigrations python manage.py migrate

CONSULTAS
Abrir la consola:
python manage.py shell

Dentro del shell hay que importar los modelos para trabajar

from apps.aplicacion.models import Modelo, Modelo1, etc

## CREAR: 
Forma 1= 

curso1 = Curso.objects.create(nombre="Historia", cantidad_horas=30)


Forma 2= 

curso1 = Curso(nombre="Matemática", cantidad_horas=40)
curso1.save()

# CREAR UNA ENTIDAD RELACIONADA 

est1 = Estudiante(nombre="Ana", apellido="Pérez", edad=20, nota_curso=8.75)
est1.save()

o 

est1= Estudiante.objects.create(nombre="Ana", apellido="Pérez", edad=20, nota_curso=8.75)

Agregar Relacion: 

est1.cursos.add(curso1)

# VISTAS TEMPLATE
Sintaxis de la views.py

ref home_view(request como minimo) return HhtpResponse

Hacer un archivo urls.py path -- import djangourlpath

Generar una lista con las urls

# MODELO VISTA TEMPLATES



Crear archivo en la aplicacion que se llame urls.py para generar las urls de mi app

En urls.py del proyecto hay que linkear las urls de la app una sola vez 

ejemplo:

"""esto es en el proyecto- urls.py

from django.contrib import admin

from django.urls import path

from django.urls.conf import include

from apps.estudiante.urls import *
app_name = 'estudiante' //poner el nombre de la appa
urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('apps.estudiante.urls', namespace='estudiante')),]


# EJEMPLO DE  UNA VISTA QUE DEVUELVE TODOS LOS REGISTROS DE UN MODELO:
en views.py
from django.shortcuts import render

from django.urls import path

from .models import Estudiante

from .views import vista_inicial 



def lista_estudiantes(request):

    estudiantes = Estudiante.objects.all()
    return render(request,'estudiantes/lista_estudiantes.html',{'estudiantes':estudiantes})

# Funcion para obtener por id un elemento or pk (primary key)

def obtener_estudiante_por_id(request, pk): 
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudiante/estudiante.html', {'estudiante': estudiante})

# TEMPLATES

## CONFIGURACIONES NECESARIAS: 

Dentro de la app crear una carpeta llamada templates y dentro de esa carpeta crear otra carpeta que se llame igual que la app 

para que django reconozca de que app proviene el template}

configurar el template en settings.py del proyecto

 'DIRS': [os.path.join(BASE_DIR), 'templates'],


tiene que quedar asi:
STATIC_URL = 'static/'

STATIC_FILES_DIRS=(os.path.join(BASE_DIR, 'static'),)
 
importar os = import os
 
en el directorio raiz crear una carpeta static