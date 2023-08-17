from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso


def crear_curso(request):
    nombre_curso = "R2"
    comision_curso = 38988
    print("Creando curso")
    curso = Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta = f"Curso creado: {nombre_curso}-{comision_curso}"
    return HttpResponse(respuesta)


def lista_cursos(request):
    cursos = Curso.objects.all()
    respuesta = ""
    for curso in cursos:
        respuesta += f"{curso.nombre}-{curso.comision}<br>"
    return HttpResponse(respuesta)


# Create your views here.
