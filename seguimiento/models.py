# seguimiento/models.py
from django.db import models
from actividades.models import Indicador

class SeguimientoIndicador(models.Model):
    """
    Registro del avance de un indicador por trimestre.
    Permite monitorear el cumplimiento de metas a lo largo del año.
    """
    indicador = models.ForeignKey(
        Indicador,
        on_delete=models.CASCADE,
        related_name='seguimientos',
        help_text="Indicador al que se refiere este seguimiento"
    )
    trimestre = models.CharField(
        max_length=3,
        choices=[
            ('I', 'I'),
            ('II', 'II'),
            ('III', 'III'),
            ('IV', 'IV')
        ],
        help_text="Trimestre de seguimiento"
    )
    meta_programada = models.CharField(
        max_length=50,
        help_text="Meta programada para este trimestre"
    )
    ejecutado = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Avance físico registrado (puede ser número, porcentaje, etc.)"
    )
    medio_verificacion = models.TextField(
        blank=True,
        null=True,
        help_text="Documento o evidencia que verifica el cumplimiento (informe, acta, etc.)"
    )
    fecha_registro = models.DateField(
        auto_now_add=True,
        help_text="Fecha en que se registró el avance"
    )

    class Meta:
        verbose_name = "Seguimiento de Indicador"
        verbose_name_plural = "Seguimientos de Indicadores"
        # Evita que un indicador tenga dos registros para el mismo trimestre
        unique_together = ('indicador', 'trimestre')
        ordering = ['indicador', 'trimestre']

    def __str__(self):
        return f"{self.indicador.descripcion} - {self.trimestre} ({self.ejecutado or 'Pendiente'})"