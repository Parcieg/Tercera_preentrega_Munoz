from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Estudiante, Profesor, Entregable


def lista_profesores(request):
    profesores = Profesor.objects.all()
    respuesta = ""
    for profesor in profesores:
        respuesta += f"{profesor.nombre} {profesor.apellido}-{profesor.profesion} <br>"
    return HttpResponse(respuesta)


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


def inicio(request):
    return render(request, "Appcoder/inicio.html")


def profesores(request):
    return render(request, "Appcoder/profesores.html")


def estudiantes(request):
    return render(request, "Appcoder/estudiantes.html")


def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "Appcoder/cursos.html", {"cursos": cursos})


def entregables(request):
    return render(request, "Appcoder/entregables.html")


# Create your views here.
