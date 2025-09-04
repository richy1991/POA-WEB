# recursos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'catalogo-recursos', views.CatalogoRecursoViewSet)
router.register(r'recursos-solicitados', views.RecursoSolicitadoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]