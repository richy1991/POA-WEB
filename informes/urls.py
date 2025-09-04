# informes/urls.py
from django.urls import path
from . import views

app_name = 'informes'

urlpatterns = [
    path('', views.reporte_poa, name='reporte_poa'),
]