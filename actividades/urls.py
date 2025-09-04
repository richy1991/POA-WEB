# actividades/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'actividades', views.ActividadViewSet)
router.register(r'indicadores', views.IndicadorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]