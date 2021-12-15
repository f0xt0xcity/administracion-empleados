from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
class EmpleadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    def full_name(self, obj):
        #Toda la operación necesaria
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name', 'last_name')
    list_filter = ('job','habilidades','departamento')

    filter_horizontal = ('habilidades',) #Solo funciona para campos muchos a muchos

admin.site.register(Empleado, EmpleadAdmin)
admin.site.register(Habilidades)