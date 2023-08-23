from django.shortcuts import render
from django.http import HttpResponse
from .forms import (
    Profesoresform,
    Cursoform,
    Estudiantesform,
    Entregableform,
    Contactoform,
)
from .models import Curso, Estudiante, Profesor, Entregable, Contacto


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
    if request.method == "POST":
        form = Contactoform(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            asunto = info["asunto"]
            correo = info["correo"]

            contacto = Contacto(nombre=nombre, asunto=asunto, correo=correo)

            contacto.save()

            return render(
                request, "Appcoder/inicio.html", {"mensaje": "estudiante creado"}
            )
        else:
            return render(
                request, "Appcoder/inicio.html", {"mensaje": "Datos no validos"}
            )

    else:
        contacto_formulario = Contactoform()

    context = {"formulario": contacto_formulario}

    return render(request, "Appcoder/inicio.html", context)


def profesores(request):
    profesores = Profesor.objects.all()

    if request.method == "POST":
        form = Profesoresform(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            correo = info["correo"]
            profesion = info["profesion"]
            profesor = Profesor(
                nombre=nombre, apellido=apellido, correo=correo, profesion=profesion
            )
            profesor.save()
            return render(
                request, "Appcoder/profesores.html", {"mensaje": "Profesore creado"}
            )
        else:
            return render(
                request, "Appcoder/profesores.html", {"mensaje": "Datos no validos"}
            )

    else:
        formulario_profesor = Profesoresform()

    context = {"formulario": formulario_profesor, "profesores": profesores}

    return render(request, "Appcoder/profesores.html", context)


def estudiantes(request):
    estudiantes = Estudiante.objects.all()

    if request.method == "POST":
        form = Estudiantesform(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            correo = info["correo"]

            estudiante = Estudiante(nombre=nombre, apellido=apellido, correo=correo)

            estudiante.save()

            return render(
                request, "Appcoder/estudiantes.html", {"mensaje": "estudiante creado"}
            )
        else:
            return render(
                request, "Appcoder/estudiantes.html", {"mensaje": "Datos no validos"}
            )

    else:
        estudiante_formulario = Estudiantesform()

    context = {"formulario": estudiante_formulario, "estudiantes": estudiantes}

    return render(request, "Appcoder/estudiantes.html", context)


def cursos(request):
    cursos = Curso.objects.all()

    if request.method == "POST":
        form = Cursoform(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            comision = info["comision"]

            curso = Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "Appcoder/cursos.html", {"mensaje": "curso creado"})
        else:
            return render(
                request, "Appcoder/cursos.html", {"mensaje": "Datos no validos"}
            )

    else:
        curso_formulario = Cursoform()

    context = {"formulario": curso_formulario, "cursos": cursos}

    return render(request, "Appcoder/cursos.html", context)


def entregables(request):
    if request.method == "POST":
        form = Entregableform(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            fecha_entrega = info["fecha_entrega"]
            entregado = info["entregado"]

            entregable = Entregable(
                nombre=nombre, fecha_entrega=fecha_entrega, entregado=entregado
            )
            entregable.save()
            return render(
                request, "Appcoder/entregables.html", {"mensaje": "entregable creado"}
            )
        else:
            return render(
                request, "Appcoder/entregables.html", {"mensaje": "Datos no validos"}
            )

    else:
        entregable_formulario = Entregableform()

    context = {"formulario": entregable_formulario}

    return render(request, "Appcoder/entregables.html", context)
