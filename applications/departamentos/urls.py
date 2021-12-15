from django.urls import path
from .views import ListaDepartamentoView, NewDepartamentoView, prueba

app_name = "departamento_app"
urlpatterns = [
    path('', prueba),
    path(
        'lista-departamentos/', 
        ListaDepartamentoView.as_view(), 
        name="lista_departamentos"
    ),
    path(
        'new_departamento/', 
        NewDepartamentoView.as_view(), 
        name="nuevo_departamento"
        ),
]