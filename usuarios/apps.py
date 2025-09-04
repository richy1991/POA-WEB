# usuarios/apps.py
from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'
    verbose_name = "Gestión de Usuarios"

    def ready(self):
        """
        Importa las señales cuando la app está lista.
        Esto asegura que el perfil se cree automáticamente al crear un usuario.
        """
        import usuarios.signals