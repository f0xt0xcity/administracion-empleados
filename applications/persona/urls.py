from django.urls import path
from .views import EmpleadoCreateView, EmpleadoDeleteView, EmpleadoDetailView, EmpleadoUpdateView, ListAllEmpleados, ListAllEmpleadosAdmin, ListByArea, ListByJob, ListEmpleadosByKword, ListHabilidadesEmpleado, SuccessView


app_name = "persona_app"

urlpatterns = [
    path(
        'listar_todo/', 
        ListAllEmpleados.as_view(),
        name="listar_todo"
        ),
    path(
        'listar_admin/', 
        ListAllEmpleadosAdmin.as_view(),
        name="listar_admin"
        ),
    path(
        'listar_by_area/<shorname>/', 
        ListByArea.as_view(),
        name = "empleados_area"
        ),
    path('listar_by_job/<job>/', ListByJob.as_view()),
    path('buscar-empleado/', ListEmpleadosByKword.as_view()),
    path('habilidades-empleado/', ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', EmpleadoDetailView.as_view(), name="detalle_empleado"),
    path(
        'add-empleado/', 
        EmpleadoCreateView.as_view(),
        name="create"
        ),
    path(
        'delete-empleado/<pk>/',
        EmpleadoDeleteView.as_view(),
        name = "delete",
        ),
    path(
        'update-empleado/<pk>/', 
        EmpleadoUpdateView.as_view(), 
        name = "update"
    ),
    path(
        'success/', 
        SuccessView.as_view(), 
        name="correcto"
        ),
]