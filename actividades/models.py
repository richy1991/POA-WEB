# actividades/models.py
from django.db import models
from core.models import Responsable
from programas.models import ObjetivoEspecifico
from core.models import Gestion, UnidadSolicitante

class Actividad(models.Model):
    """
    Actividad del Plan Operativo Anual (POA)
    """
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_curso', 'En Curso'),
        ('realizado', 'Realizado'),
        ('suspendido', 'Suspendido'),
    ]

    objetivo_especifico = models.ForeignKey(
        ObjetivoEspecifico,
        on_delete=models.CASCADE,
        related_name='actividades',
        help_text="Objetivo Específico al que pertenece esta actividad"
    )
    gestion = models.ForeignKey(
        Gestion,
        on_delete=models.CASCADE,
        help_text="Año de gestión (ej: 2026)"
    )
    unidad_solicitante = models.ForeignKey(
        UnidadSolicitante,
        on_delete=models.CASCADE,
        help_text="Unidad que elabora y ejecuta la actividad"
    )
    codigo = models.CharField(
        max_length=20,
        help_text="Código de la actividad (ej: A001)"
    )
    nombre = models.CharField(
        max_length=200,
        help_text="Nombre de la actividad"
    )
    responsable = models.ForeignKey(
        Responsable,
        on_delete=models.PROTECT,
        help_text="Responsable de la ejecución"
    )
    producto_esperado = models.TextField(
        help_text="Bien, servicio o norma esperado como resultado"
    )
    mes_inicio = models.CharField(
        max_length=20,
        help_text="Mes de inicio (ej: Enero)"
    )
    mes_fin = models.CharField(
        max_length=20,
        help_text="Mes de finalización (ej: Junio)"
    )
    monto_asignado = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0,
        help_text="Monto total asignado en Bs."
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente',
        help_text="Estado de avance de la actividad"
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        help_text="Última fecha de actualización"
    )

    class Meta:
        verbose_name = "Actividad del POA"
        verbose_name_plural = "Actividades del POA"
        ordering = ['codigo']
        unique_together = ('codigo', 'gestion')  # Evita duplicados

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Indicador(models.Model):
    """
    Indicador de gestión para una actividad
    """
    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE,
        related_name='indicadores'
    )
    descripcion = models.CharField(
        max_length=200,
        help_text="Descripción del indicador (ej: N° de estudiantes capacitados)"
    )
    unidad_medida = models.CharField(
        max_length=50,
        help_text="Unidad (ej: Número, Porcentaje, Horas)"
    )
    linea_base = models.CharField(
        max_length=50,
        help_text="Valor inicial antes de la actividad"
    )
    meta = models.CharField(
        max_length=50,
        help_text="Valor esperado al finalizar"
    )
    medio_verificacion = models.TextField(
        blank=True,
        null=True,
        help_text="Documento o evidencia que verifica el cumplimiento (informe, acta, etc.)"
    )

    class Meta:
        verbose_name = "Indicador"
        verbose_name_plural = "Indicadores"

    def __str__(self):
        return f"{self.descripcion} ({self.unidad_medida})"