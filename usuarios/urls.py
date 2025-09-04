# usuarios/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'perfiles', views.PerfilUsuarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]