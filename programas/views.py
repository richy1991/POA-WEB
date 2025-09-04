# programas/views.py
from rest_framework import viewsets
from .models import Programa, ObjetivoEspecifico
from .serializers import ProgramaSerializer, ObjetivoEspecificoSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class ProgramaFilter(django_filters.FilterSet):
    gestion = django_filters.NumberFilter(field_name='gestion__año')

    class Meta:
        model = Programa
        fields = ['gestion', 'codigo']

class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.select_related('gestion').all()
    serializer_class = ProgramaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProgramaFilter

class ObjetivoEspecificoFilter(django_filters.FilterSet):
    programa_codigo = django_filters.CharFilter(field_name='programa__codigo')
    gestion = django_filters.NumberFilter(field_name='programa__gestion__año')

    class Meta:
        model = ObjetivoEspecifico
        fields = ['programa', 'programa_codigo', 'gestion']

class ObjetivoEspecificoViewSet(viewsets.ModelViewSet):
    queryset = ObjetivoEspecifico.objects.select_related('programa', 'programa__gestion').all()
    serializer_class = ObjetivoEspecificoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ObjetivoEspecificoFilter