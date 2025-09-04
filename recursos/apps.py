# recursos/apps.py
from django.apps import AppConfig


class RecursosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recursos'
    verbose_name = "Recursos Físicos y Financieros"