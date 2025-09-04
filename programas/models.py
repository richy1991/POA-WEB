# programas/models.py
from django.db import models
from core.models import Gestion

class Programa(models.Model):
    """
    Programa institucional (ej: 100 - Formación Profesional)
    """
    codigo = models.CharField(
        max_length=10,
        unique=True,
        help_text="Código del programa (ej: 100, 510, 610)"
    )
    nombre = models.CharField(
        max_length=200,
        help_text="Nombre del programa (ej: Gestión de la Formación de Pregrado)"
    )
    objetivo_institucional = models.TextField(
        help_text="Objetivo estratégico de gestión institucional"
    )
    gestion = models.ForeignKey(
        'core.Gestion',
        on_delete=models.CASCADE,
        help_text="Gestión a la que pertenece el programa"
    )

    class Meta:
        verbose_name = "Programa Institucional"
        verbose_name_plural = "Programas Institucionales"
        ordering = ['codigo']
        

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class ObjetivoEspecifico(models.Model):
    """
    Objetivo Específico (OE) dentro de un programa
    """
    programa = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name='objetivos_especificos'
    )
    codigo = models.CharField(
        max_length=20,
        unique=True,
        help_text="Código jerárquico (ej: 100-0-1)"
    )
    descripcion = models.TextField(
        help_text="Descripción del objetivo específico"
    )

    class Meta:
        verbose_name = "Objetivo Específico"
        verbose_name_plural = "Objetivos Específicos"
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"