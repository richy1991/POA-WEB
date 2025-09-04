# actividades/admin.py
from django.contrib import admin
from .models import Actividad, Indicador

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = [
        'codigo',
        'nombre',
        'objetivo_especifico',
        'estado',
        'gestion',
        'unidad_solicitante',
        'monto_asignado'
    ]
    list_filter = [
        'estado',
        'gestion',
        'objetivo_especifico__programa',
        'unidad_solicitante',
        'mes_inicio',
        'mes_fin'
    ]
    search_fields = ['codigo', 'nombre', 'producto_esperado']
    autocomplete_fields = ['objetivo_especifico', 'responsable', 'unidad_solicitante']
    readonly_fields = ['fecha_actualizacion']
    fieldsets = (
        ('Información Principal', {
            'fields': ('codigo', 'nombre', 'objetivo_especifico', 'gestion')
        }),
        ('Unidad y Responsable', {
            'fields': ('unidad_solicitante', 'responsable')
        }),
        ('Planificación', {
            'fields': ('producto_esperado', 'mes_inicio', 'mes_fin')
        }),
        ('Presupuesto y Estado', {
            'fields': ('monto_asignado', 'estado', 'fecha_actualizacion')
        }),
    )
    ordering = ['codigo']


@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'actividad', 'unidad_medida', 'linea_base', 'meta']
    list_filter = ['actividad__objetivo_especifico__programa', 'actividad__gestion']
    search_fields = ['descripcion', 'actividad__nombre']
    autocomplete_fields = ['actividad']