from django.test import TestCase
from .models import Actividad, Indicador
from core.models import Gestion, UnidadSolicitante, TipoUnidad, Responsable
from programas.models import Programa, ObjetivoEspecifico

class ActividadesModelTest(TestCase):
    def setUp(self):
        gestion = Gestion.objects.create(año=2025)
        tipo_unidad = TipoUnidad.objects.create(nombre="Test-Unidad")
        responsable = Responsable.objects.create(nombre="Test Responsable", cargo="Test Cargo")
        unidad_solicitante = UnidadSolicitante.objects.create(
            tipo=tipo_unidad,
            nombre="Unidad Solicitante de Prueba",
            responsable=responsable
        )
        programa = Programa.objects.create(
            codigo="999",
            nombre="Programa de Prueba",
            objetivo_institucional="Objetivo de prueba",
            gestion=gestion
        )
        objetivo_especifico = ObjetivoEspecifico.objects.create(
            programa=programa,
            codigo="999-9-9",
            descripcion="Objetivo Específico de Prueba"
        )
        self.actividad = Actividad.objects.create(
            objetivo_especifico=objetivo_especifico,
            gestion=gestion,
            unidad_solicitante=unidad_solicitante,
            codigo="A999",
            nombre="Actividad de Prueba",
            responsable=responsable,
            producto_esperado="Producto de prueba",
            mes_inicio="Enero",
            mes_fin="Diciembre"
        )
        self.indicador = Indicador.objects.create(
            actividad=self.actividad,
            descripcion="Indicador de Prueba",
            unidad_medida="Unidad",
            linea_base="0",
            meta="100"
        )

    def test_actividad_str(self):
        self.assertEqual(str(self.actividad), "A999 - Actividad de Prueba")

    def test_indicador_str(self):
        self.assertEqual(str(self.indicador), "Indicador de Prueba (Unidad)")
