from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from applications.persona.models import Empleado
from .models import Departamentos
from applications.departamentos.forms import NewDepartamentoForm

# Create your views here.

class ListaDepartamentoView(ListView):
    template_name = 'departamentos/listar_departamento.html'
    model = Departamentos
    context_object_name = "Departamentos"
    ordering = ['name']

class ListarEmpleadosPorArea(ListView):
    template_name = "departamentos/empleados_area.html"
    model = Empleado


def prueba(request):
    return  HttpResponse("<h1>Departamento</h1>")

class NewDepartamentoView(FormView):
    template_name = "departamentos/new_departamento.html"
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        depa = Departamentos(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname'],
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name =nombre,
            last_name = apellido,
            job = '1',
            departamento = depa,
        )
        print((nombre))
        return super(NewDepartamentoView, self).form_valid(form)