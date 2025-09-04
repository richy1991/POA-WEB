# programas/serializers.py
from rest_framework import serializers
from .models import Programa, ObjetivoEspecifico

class ProgramaSerializer(serializers.ModelSerializer):
    gestion_año = serializers.IntegerField(source='gestion.año', read_only=True)

    class Meta:
        model = Programa
        fields = '__all__'


class ObjetivoEspecificoSerializer(serializers.ModelSerializer):
    programa_codigo = serializers.CharField(source='programa.codigo', read_only=True)
    programa_nombre = serializers.CharField(source='programa.nombre', read_only=True)
    gestion = serializers.IntegerField(source='programa.gestion.año', read_only=True)

    class Meta:
        model = ObjetivoEspecifico
        fields = '__all__'