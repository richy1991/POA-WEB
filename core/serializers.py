# core/serializers.py
from rest_framework import serializers
from .models import (
    Entidad,
    Gestion,
    TipoUnidad,
    UnidadSolicitante,
    Responsable,
    PartidaPresupuestaria
)


class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = '__all__'


class GestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestion
        fields = '__all__'


class TipoUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUnidad
        fields = '__all__'


class UnidadSolicitanteSerializer(serializers.ModelSerializer):
    tipo_nombre = serializers.CharField(source='tipo.nombre', read_only=True)
    responsable_nombre = serializers.CharField(source='responsable.nombre', read_only=True)

    class Meta:
        model = UnidadSolicitante
        fields = '__all__'


class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = '__all__'


class PartidaPresupuestariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidaPresupuestaria
        fields = '__all__'