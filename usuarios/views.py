# usuarios/views.py
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import PerfilUsuario
from .serializers import PerfilUsuarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PerfilUsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API para gestionar los perfiles de usuario.
    Incluye un endpoint para obtener el perfil del usuario autenticado.
    """
    queryset = PerfilUsuario.objects.select_related('user', 'unidad').all()
    serializer_class = PerfilUsuarioSerializer
    filterset_fields = ['unidad', 'cargo']

    @action(detail=False, methods=['get'])
    def mi_perfil(self, request):
        """
        Retorna el perfil del usuario autenticado.
        Útil para el frontend para cargar datos del usuario logueado.
        """
        perfil = self.get_queryset().get(user=request.user)
        serializer = self.get_serializer(perfil)
        return Response(serializer.data)