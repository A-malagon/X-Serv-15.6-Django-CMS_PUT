from django.shortcuts import render
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

@csrf_exempt
def mostrar(request, recurso):
    if request.method == "GET":
        #MUESTRO DE LA BD
        try:
            fila = Pages.objects.get(name=recurso)
            return HttpResponse(request.method + " " + str(fila.id) +
                                " " + fila.name + " " + fila.page)
        except Pages.DoesNotExist:
            return HttpResponseNotFound("Pagina no encontrada:" +
                                        " " + recurso)
    elif request.method == "PUT":
        #GUARDO EN LA BD
        nuevoRecurso = Pages(name=recurso, page=request.body)
        nuevoRecurso.save()
        return HttpResponse("Recurso guardado")
