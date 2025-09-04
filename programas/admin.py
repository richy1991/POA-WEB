# programas/admin.py
from django.contrib import admin
from .models import Programa, ObjetivoEspecifico

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'gestion']
    list_filter = ['gestion', 'codigo']
    search_fields = ['codigo', 'nombre', 'objetivo_institucional']
    ordering = ['codigo']
    fieldsets = (
        (None, {
            'fields': ('codigo', 'nombre', 'gestion')
        }),
        ('Objetivo Institucional', {
            'fields': ('objetivo_institucional',)
        }),
    )


@admin.register(ObjetivoEspecifico)
class ObjetivoEspecificoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'programa', 'descripcion_resumida']
    list_filter = ['programa__codigo', 'programa__gestion']
    search_fields = ['codigo', 'descripcion']
    autocomplete_fields = ['programa']
    ordering = ['codigo']

    def descripcion_resumida(self, obj):
        return obj.descripcion[:100] + "..." if len(obj.descripcion) > 100 else obj.descripcion
    descripcion_resumida.short_description = "Descripción"