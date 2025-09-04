# recursos/models.py
from django.db import models
from actividades.models import Actividad
from core.models import PartidaPresupuestaria

class CatalogoRecurso(models.Model):
    """
    Catálogo maestro de ítems institucionales (materiales, servicios, equipos, etc.)
    Basado en el archivo 'items para el Sistema POA.xlsx'
    """
    TIPO_CHOICES = [
        ('material', 'Material'),
        ('servicio', 'Servicio'),
        ('equipo', 'Equipo'),
        ('insumo', 'Insumo'),
        ('otro', 'Otro'),
    ]

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        help_text="Tipo de recurso"
    )
    codigo_interno = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        help_text="Código interno del ítem (NRO del Excel)"
    )
    descripcion = models.TextField(
        help_text="Descripción detallada del recurso"
    )
    partida_presupuestaria = models.ForeignKey(
        PartidaPresupuestaria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Partida presupuestaria asociada"
    )
    unidad_medida_sugerida = models.CharField(
        max_length=50,
        blank=True,
        help_text="Unidad de medida sugerida (ej: Unidad, Litro, Galón)"
    )

    class Meta:
        verbose_name = "Catálogo de Recurso"
        verbose_name_plural = "Catálogo de Recursos"
        ordering = ['tipo', 'descripcion']

    def __str__(self):
        return f"{self.codigo_interno or 'S/C'} - {self.descripcion[:80]}..."


class RecursoSolicitado(models.Model):
    """
    Recurso solicitado para una actividad específica (Formulario Nro. 3)
    """
    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE,
        related_name='recursos_solicitados',
        help_text="Actividad del POA a la que pertenece este recurso"
    )
    detalle = models.CharField(
        max_length=200,
        help_text="Descripción del recurso (puede ser del catálogo o personalizado)"
    )
    unidad_medida = models.CharField(
        max_length=50,
        help_text="Unidad de medida (ej: Unidad, Caja, Litro)"
    )
    caracteristicas = models.TextField(
        blank=True,
        null=True,
        help_text="Especificaciones técnicas o adicionales"
    )
    partida_presupuestaria = models.ForeignKey(
        PartidaPresupuestaria,
        on_delete=models.PROTECT,
        help_text="Partida presupuestaria (ej: 39500 - Útiles de Oficina)"
    )
    cantidad_requerida = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Cantidad necesaria"
    )
    costo_unitario = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Precio unitario en Bolivianos (Bs.)"
    )
    costo_total = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        editable=False,
        help_text="Calculado automáticamente: cantidad × costo unitario"
    )
    mes_requerimiento = models.CharField(
        max_length=50,
        help_text="Período de requerimiento (ej: Enero-Junio)"
    )

    class Meta:
        verbose_name = "Recurso Solicitado"
        verbose_name_plural = "Recursos Solicitados"
        ordering = ['actividad__codigo']

    def save(self, *args, **kwargs):
        # Calcular costo total antes de guardar
        self.costo_total = self.cantidad_requerida * self.costo_unitario
        print(f"El costo total calculado es: {self.costo_total} Bs.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.detalle} - {self.costo_total} Bs."