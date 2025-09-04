# core/admin.py
from django.contrib import admin
from .models import (
    Entidad,
    Gestion,
    TipoUnidad,
    UnidadSolicitante,
    Responsable,
    PartidaPresupuestaria
)


@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']


@admin.register(Gestion)
class GestionAdmin(admin.ModelAdmin):
    list_display = ['año']
    search_fields = ['año']
    ordering = ['-año']


@admin.register(TipoUnidad)
class TipoUnidadAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']


@admin.register(UnidadSolicitante)
class UnidadSolicitanteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'codigo_interno']
    list_filter = ['tipo']
    search_fields = ['nombre', 'codigo_interno']
    autocomplete_fields = ['responsable']


@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cargo']
    search_fields = ['nombre', 'cargo']


@admin.register(PartidaPresupuestaria)
class PartidaPresupuestariaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']
    search_fields = ['codigo', 'nombre']
    ordering = ['codigo']