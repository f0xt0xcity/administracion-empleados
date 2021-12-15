from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = ['first_name']
    model = Empleado
    context_object_name = "Empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )
        return lista

class ListAllEmpleadosAdmin(ListView):
    template_name = "persona/list_all_empleados.html"
    paginate_by = 10
    ordering = ['first_name']
    model = Empleado
    context_object_name = "Empleados"


class ListByArea(ListView):
    #Listar empleados de un area
    template_name = "persona/list_by_area.html"
    context_object_name = "Empleados"

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
    )
        return lista


class ListByJob(ListView):
    template_name = "persona/list_by_job.html"

    def get_queryset(self) :
        job = self.kwargs['job']
        lista = Empleado.objects.filter(
            job = job
        )
        return lista

class ListEmpleadosByKword(ListView):
    """ Lista empleados por palabra clave """
    template_name = "persona/by_kword.html"
    context_object_name = "empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",)
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = "habilidades"

    def get_queryset(self):
        id = self.request.GET.get("empleado")
        empleado = Empleado.objects.get(id=id)
        print()
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = "persona/success.html"

class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url =reverse_lazy('persona_app:listar_admin')

    def form_valid(self, form):
        #Logica del proceso
        empleado = form.save(commit=False)
        empleado.fullname = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/actualizar.html"
    model = Empleado
    fields = [
        'first_name',
         'last_name',
         'job', 
         'departamento',
         'habilidades',
    ]
    success_url = reverse_lazy('persona_app:listar_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #Logica del proceso
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:listar_admin')