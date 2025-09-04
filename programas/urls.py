# programas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'programas', views.ProgramaViewSet)
router.register(r'objetivos-especificos', views.ObjetivoEspecificoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]