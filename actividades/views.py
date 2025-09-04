# actividades/views.py
from rest_framework import viewsets
from .models import Actividad, Indicador
from .serializers import ActividadSerializer, IndicadorSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class ActividadFilter(django_filters.FilterSet):
    estado = django_filters.ChoiceFilter(choices=Actividad.ESTADO_CHOICES)
    gestion = django_filters.NumberFilter(field_name='gestion__año')
    programa = django_filters.CharFilter(field_name='objetivo_especifico__programa__codigo')
    unidad = django_filters.NumberFilter(field_name='unidad_solicitante__id')
    responsable = django_filters.NumberFilter(field_name='responsable__id')

    class Meta:
        model = Actividad
        fields = ['estado', 'gestion', 'programa', 'unidad', 'objetivo_especifico', 'responsable']

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.select_related(
        'objetivo_especifico__programa',
        'unidad_solicitante',
        'responsable',
        'gestion'
    ).prefetch_related('indicadores').all()
    serializer_class = ActividadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ActividadFilter

class IndicadorFilter(django_filters.FilterSet):
    actividad_estado = django_filters.ChoiceFilter(
        field_name='actividad__estado',
        choices=Actividad.ESTADO_CHOICES
    )
    gestion = django_filters.NumberFilter(field_name='actividad__gestion__año')

    class Meta:
        model = Indicador
        fields = ['actividad', 'actividad_estado', 'gestion']

class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.select_related('actividad', 'actividad__gestion').all()
    serializer_class = IndicadorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = IndicadorFilter