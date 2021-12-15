from django.shortcuts import render
from .models import Prueba
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import PruebaForm

# Create your views here.
class PruebaView(TemplateView):
    template_name = "home/prueba.html"

class ResumeFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"

class PruebaListView(ListView):
    template_name ="home/lista.html"
    context_object_name = 'listaNumeros'
    queryset =  ['0','1','10','20','30']

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = "/"