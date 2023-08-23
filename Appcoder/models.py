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

    def __str__(self):
        return "{self.nombre} {self.apellido}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    correo = models.EmailField()
