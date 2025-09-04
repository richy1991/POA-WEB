# core/views.py
from rest_framework import viewsets
from .models import (
    Entidad,
    Gestion,
    TipoUnidad,
    UnidadSolicitante,
    Responsable,
    PartidaPresupuestaria
)
from .serializers import (
    EntidadSerializer,
    GestionSerializer,
    TipoUnidadSerializer,
    UnidadSolicitanteSerializer,
    ResponsableSerializer,
    PartidaPresupuestariaSerializer
)


class EntidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer


class GestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gestion.objects.all()
    serializer_class = GestionSerializer


class TipoUnidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoUnidad.objects.all()
    serializer_class = TipoUnidadSerializer


class UnidadSolicitanteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UnidadSolicitante.objects.select_related('tipo', 'responsable')
    serializer_class = UnidadSolicitanteSerializer
    filterset_fields = ['tipo']


class ResponsableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Responsable.objects.all()
    serializer_class = ResponsableSerializer


class PartidaPresupuestariaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartidaPresupuestaria.objects.all()
    serializer_class = PartidaPresupuestariaSerializer