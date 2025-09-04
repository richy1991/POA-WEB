# usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import PerfilUsuario

# Define un Inline para mostrar el PerfilUsuario en el admin de User
class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'Perfiles'

# Define un nuevo UserAdmin
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilUsuarioInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'unidad', 'cargo']
    list_filter = ['unidad', 'cargo']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'cargo']
    autocomplete_fields = ['unidad']