# backend_django/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # <-- Aquí está la corrección

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('api/programas/', include('programas.urls')),
    path('api/actividades/', include('actividades.urls')),
    path('api/recursos/', include('recursos.urls')),
    path('api/seguimiento/', include('seguimiento.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path('reporte/', include('informes.urls')),

    # Redirigir la raíz a /reporte/
    path('', lambda request: redirect('reporte_poa', permanent=False)),
]