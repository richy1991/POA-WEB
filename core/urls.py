# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'entidades', views.EntidadViewSet)
router.register(r'gestiones', views.GestionViewSet)
router.register(r'tipos-unidad', views.TipoUnidadViewSet)
router.register(r'unidades', views.UnidadSolicitanteViewSet)
router.register(r'responsables', views.ResponsableViewSet)
router.register(r'partidas', views.PartidaPresupuestariaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]