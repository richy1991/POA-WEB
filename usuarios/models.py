# usuarios/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import UnidadSolicitante

class PerfilUsuario(models.Model):
    """
    Perfil personalizado para extender el modelo de usuario de Django.
    Asocia un usuario con una unidad y un cargo.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil',
        help_text="Usuario de Django asociado a este perfil"
    )
    unidad = models.ForeignKey(
        UnidadSolicitante,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Unidad académica o administrativa a la que pertenece"
    )
    cargo = models.CharField(
        max_length=100,
        blank=True,
        help_text="Cargo del usuario (Director, Coordinador, etc.)"
    )

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

    def __str__(self):
        return f"{self.user.username} - {self.cargo or 'Sin cargo'}"