from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField((""))


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    profesion = models.CharField(max_length=50)


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField((""), auto_now=False, auto_now_add=False)
    entregado = models.BooleanField()
