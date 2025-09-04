# core/models.py
from django.db import models
from django.core.validators import MinValueValidator

class Entidad(models.Model):
    """
    Entidad institucional (ej: UABJB)
    """
    nombre = models.CharField(max_length=100, default="UABJB")

    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"

    def __str__(self):
        return self.nombre


class Gestion(models.Model):
    """
    Año de gestión del POA
    """
    año = models.IntegerField(unique=True, validators=[MinValueValidator(2020)])

    class Meta:
        verbose_name = "Gestión"
        verbose_name_plural = "Gestiones"
        ordering = ['-año']

    def __str__(self):
        return str(self.año)


class TipoUnidad(models.Model):
    """
    Tipo de unidad que elabora el POA (Carrera, Instituto, Unidad Administrativa, etc.)
    """
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Tipo de Unidad"
        verbose_name_plural = "Tipos de Unidad"

    def __str__(self):
        return self.nombre


class UnidadSolicitante(models.Model):
    """
    Unidad que elabora el POA (Carrera, Instituto, etc.)
    """
    tipo = models.ForeignKey(TipoUnidad, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=200, help_text="Nombre oficial de la unidad (ej: Carrera de Ingeniería de Sistemas)")
    codigo_interno = models.CharField(max_length=50, blank=True, null=True, help_text="Código interno (opcional)")
    responsable = models.ForeignKey(
        'Responsable',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='unidades_responsables'
    )

    class Meta:
        verbose_name = "Unidad Solicitante"
        verbose_name_plural = "Unidades Solicitantes"
        ordering = ['tipo__nombre', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({self.tipo.nombre})"


class Responsable(models.Model):
    """
    Responsable de una actividad o unidad
    """
    nombre = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Responsables"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.cargo})" if self.cargo else self.nombre


class PartidaPresupuestaria(models.Model):
    """
    Partida presupuestaria (ej: 39500 - Útiles de Oficina)
    """
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Partida Presupuestaria"
        verbose_name_plural = "Partidas Presupuestarias"
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} - {self.nombre or 'Sin nombre'}"