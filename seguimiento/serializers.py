# seguimiento/serializers.py
from rest_framework import serializers
from .models import SeguimientoIndicador

class SeguimientoIndicadorSerializer(serializers.ModelSerializer):
    indicador_descripcion = serializers.CharField(source='indicador.descripcion', read_only=True)
    actividad_nombre = serializers.CharField(source='indicador.actividad.nombre', read_only=True)
    programa = serializers.CharField(source='indicador.actividad.objetivo_especifico.programa.nombre', read_only=True)
    unidad = serializers.CharField(source='indicador.actividad.unidad_solicitante.nombre', read_only=True)

    class Meta:
        model = SeguimientoIndicador
        fields = '__all__'

    def validate(self, data):
        # Opcional: Validar que el ejecutado no sea mayor que la meta programada (si es numérico)
        # Esto se puede hacer en el frontend o con una señal
        return data