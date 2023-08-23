from django import forms


class Profesoresform(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    correo = forms.EmailField()
    profesion = forms.CharField(max_length=50)


class Cursoform(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()


class Estudiantesform(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    correo = forms.EmailField()


class Entregableform(forms.Form):
    nombre = forms.CharField(max_length=50)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()


class Contactoform(forms.Form):
    nombre = forms.CharField(max_length=50)
    asunto = forms.CharField(max_length=50)
    correo = forms.EmailField()
