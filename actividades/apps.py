# actividades/apps.py
from django.apps import AppConfig


class ActividadesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'actividades'
    verbose_name = "Actividades del POA"