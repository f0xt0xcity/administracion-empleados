from django.shortcuts import render, HttpResponse

# Create your views here.
def prueba(request):
    return  HttpResponse("<h1>Departamento</h1>")