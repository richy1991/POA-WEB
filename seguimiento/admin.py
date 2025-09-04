# seguimiento/admin.py
from django.contrib import admin
from .models import SeguimientoIndicador

@admin.register(SeguimientoIndicador)
class SeguimientoIndicadorAdmin(admin.ModelAdmin):
    list_display = [
        'indicador',
        'trimestre',
        'meta_programada',
        'ejecutado',
        'fecha_registro'
    ]
    list_filter = [
        'trimestre',
        'fecha_registro',
        'indicador__actividad__gestion',
        'indicador__actividad__objetivo_especifico__programa'
    ]
    search_fields = [
        'indicador__descripcion',
        'indicador__actividad__nombre',
        'medio_verificacion'
    ]
    autocomplete_fields = ['indicador']
    readonly_fields = ['fecha_registro']
    fieldsets = (
        (None, {
            'fields': ('indicador', 'trimestre')
        }),
        ('Metas y Avance', {
            'fields': ('meta_programada', 'ejecutado')
        }),
        ('Verificación', {
            'fields': ('medio_verificacion',),
            'classes': ('collapse',),
        }),
    )
    ordering = ['indicador', 'trimestre']