# seguimiento/views.py
from rest_framework import viewsets
from .models import SeguimientoIndicador
from .serializers import SeguimientoIndicadorSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class SeguimientoIndicadorFilter(django_filters.FilterSet):
    indicador = django_filters.NumberFilter(field_name='indicador__id')
    actividad = django_filters.NumberFilter(field_name='indicador__actividad__id')
    gestion = django_filters.NumberFilter(field_name='indicador__actividad__gestion__año')
    programa = django_filters.CharFilter(field_name='indicador__actividad__objetivo_especifico__programa__codigo')
    trimestre = django_filters.ChoiceFilter(choices=SeguimientoIndicador._meta.get_field('trimestre').choices)

    class Meta:
        model = SeguimientoIndicador
        fields = ['indicador', 'actividad', 'gestion', 'programa', 'trimestre']

class SeguimientoIndicadorViewSet(viewsets.ModelViewSet):
    queryset = SeguimientoIndicador.objects.select_related(
        'indicador',
        'indicador__actividad',
        'indicador__actividad__gestion',
        'indicador__actividad__objetivo_especifico__programa'
    ).all()
    serializer_class = SeguimientoIndicadorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SeguimientoIndicadorFilter