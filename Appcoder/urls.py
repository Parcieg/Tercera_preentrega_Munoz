from django.urls import path
from Appcoder import views
from .views import (
    crear_curso,
    lista_cursos,
    profesores,
    estudiantes,
    cursos,
    entregables,
)


urlpatterns = [
    path("crearcurso/", crear_curso),
    path("Listacursos/", lista_cursos),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("cursos/", cursos, name="cursos"),
    path("entregables/", entregables, name="entregables"),
]
