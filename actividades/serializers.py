# actividades/serializers.py
from rest_framework import serializers
from .models import Actividad, Indicador

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    objetivo_especifico_codigo = serializers.CharField(source='objetivo_especifico.codigo', read_only=True)
    objetivo_especifico_descripcion = serializers.CharField(source='objetivo_especifico.descripcion', read_only=True)
    programa = serializers.CharField(source='objetivo_especifico.programa.nombre', read_only=True)
    unidad_nombre = serializers.CharField(source='unidad_solicitante.nombre', read_only=True)
    responsable_nombre = serializers.CharField(source='responsable.nombre', read_only=True)
    indicadores = IndicadorSerializer(many=True, read_only=True)

    class Meta:
        model = Actividad
        fields = '__all__'

    def validate_monto_asignado(self, value):
        if value < 0:
            raise serializers.ValidationError("El monto asignado no puede ser negativo.")
        return value