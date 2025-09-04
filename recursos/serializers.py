# recursos/serializers.py
from rest_framework import serializers
from .models import CatalogoRecurso, RecursoSolicitado

class CatalogoRecursoSerializer(serializers.ModelSerializer):
    partida_nombre = serializers.CharField(source='partida_presupuestaria.nombre', read_only=True)
    partida_codigo = serializers.CharField(source='partida_presupuestaria.codigo', read_only=True)

    class Meta:
        model = CatalogoRecurso
        fields = '__all__'


class RecursoSolicitadoSerializer(serializers.ModelSerializer):
    actividad_nombre = serializers.CharField(source='actividad.nombre', read_only=True)
    programa = serializers.CharField(source='actividad.objetivo_especifico.programa.nombre', read_only=True)
    partida_descripcion = serializers.CharField(source='partida_presupuestaria.nombre', read_only=True)

    class Meta:
        model = RecursoSolicitado
        fields = '__all__'
        read_only_fields = ['costo_total']

    def validate(self, data):
        if data['cantidad_requerida'] <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor a 0.")
        if data['costo_unitario'] < 0:
            raise serializers.ValidationError("El costo unitario no puede ser negativo.")
        return data