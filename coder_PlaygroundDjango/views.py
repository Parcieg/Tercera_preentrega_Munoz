from django.http import HttpResponse


def contar(request):
    contado = "aqui te cuento una historia"
    return HttpResponse(contado)
