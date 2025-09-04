# usuarios/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PerfilUsuario
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """
    Crea un PerfilUsuario automáticamente cuando se crea un nuevo User.
    """
    if created:
        PerfilUsuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    """
    Guarda el PerfilUsuario cuando se guarda el User.
    """
    try:
        instance.perfil.save()
    except PerfilUsuario.DoesNotExist:
        # Si el perfil no existe (por alguna razón), créalo.
        PerfilUsuario.objects.create(user=instance)