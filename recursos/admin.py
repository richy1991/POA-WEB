# recursos/admin.py
from django.contrib import admin
from .models import CatalogoRecurso, RecursoSolicitado

@admin.register(CatalogoRecurso)
class CatalogoRecursoAdmin(admin.ModelAdmin):
    list_display = [
        'codigo_interno',
        'tipo',
        'descripcion_resumida',
        'partida_presupuestaria',
        'unidad_medida_sugerida'
    ]
    list_filter = ['tipo', 'partida_presupuestaria']
    search_fields = ['codigo_interno', 'descripcion']
    ordering = ['tipo', 'descripcion']
    fieldsets = (
        (None, {
            'fields': ('tipo', 'codigo_interno', 'descripcion')
        }),
        ('Detalles', {
            'fields': ('unidad_medida_sugerida', 'caracteristicas'),
            'classes': ('collapse',),
        }),
        ('Presupuesto', {
            'fields': ('partida_presupuestaria',)
        }),
    )

    def descripcion_resumida(self, obj):
        return obj.descripcion[:100] + "..." if len(obj.descripcion) > 100 else obj.descripcion
    descripcion_resumida.short_description = "Descripción"


@admin.register(RecursoSolicitado)
class RecursoSolicitadoAdmin(admin.ModelAdmin):
    list_display = [
        'actividad',
        'detalle',
        'unidad_medida',
        'cantidad_requerida',
        'costo_unitario',
        'costo_total',
        'mes_requerimiento'
    ]
    list_filter = [
        'actividad__gestion',
        'actividad__objetivo_especifico__programa',
        'partida_presupuestaria',
        'mes_requerimiento'
    ]
    search_fields = [
        'detalle',
        'actividad__nombre',
        'actividad__codigo'
    ]
    autocomplete_fields = ['actividad', 'partida_presupuestaria']
    readonly_fields = ['costo_total']

    fieldsets = (
        ('Actividad Asociada', {
            'fields': ('actividad',)
        }),
        ('Descripción del Recurso', {
            'fields': ('detalle', 'unidad_medida', 'caracteristicas')
        }),
        ('Presupuesto', {
            'fields': (
                'partida_presupuestaria',
                'cantidad_requerida',
                'costo_unitario',
                'costo_total'
            )
        }),
        ('Programación', {
            'fields': ('mes_requerimiento',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Edición
            return self.readonly_fields + ['actividad', 'partida_presupuestaria']
        return self.readonly_fields