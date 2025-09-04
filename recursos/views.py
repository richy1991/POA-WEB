# recursos/views.py
from rest_framework import viewsets
from .models import CatalogoRecurso, RecursoSolicitado
from .serializers import CatalogoRecursoSerializer, RecursoSolicitadoSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class CatalogoRecursoFilter(django_filters.FilterSet):
    tipo = django_filters.ChoiceFilter(choices=CatalogoRecurso.TIPO_CHOICES)
    partida = django_filters.CharFilter(field_name='partida_presupuestaria__codigo')

    class Meta:
        model = CatalogoRecurso
        fields = ['tipo', 'partida']

class CatalogoRecursoViewSet(viewsets.ModelViewSet):
    queryset = CatalogoRecurso.objects.select_related('partida_presupuestaria').all()
    serializer_class = CatalogoRecursoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CatalogoRecursoFilter
    search_fields = ['descripcion', 'codigo_interno']


class RecursoSolicitadoFilter(django_filters.FilterSet):
    actividad = django_filters.NumberFilter(field_name='actividad__id')
    gestion = django_filters.NumberFilter(field_name='actividad__gestion__año')
    programa = django_filters.CharFilter(field_name='actividad__objetivo_especifico__programa__codigo')
    partida = django_filters.CharFilter(field_name='partida_presupuestaria__codigo')

    class Meta:
        model = RecursoSolicitado
        fields = ['actividad', 'gestion', 'programa', 'partida_presupuestaria']

class RecursoSolicitadoViewSet(viewsets.ModelViewSet):
    queryset = RecursoSolicitado.objects.select_related(
        'actividad',
        'actividad__gestion',
        'partida_presupuestaria'
    ).all()
    serializer_class = RecursoSolicitadoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecursoSolicitadoFilter