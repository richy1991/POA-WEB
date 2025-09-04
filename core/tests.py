from django.test import TestCase
from .models import Entidad, Gestion, TipoUnidad, UnidadSolicitante, Responsable, PartidaPresupuestaria

class CoreModelTest(TestCase):
    def setUp(self):
        self.entidad = Entidad.objects.create(nombre="UABJB-Test")
        self.gestion = Gestion.objects.create(año=2025)
        self.tipo_unidad = TipoUnidad.objects.create(nombre="Test-Unidad")
        self.responsable = Responsable.objects.create(nombre="Test Responsable", cargo="Test Cargo")
        self.unidad_solicitante = UnidadSolicitante.objects.create(
            tipo=self.tipo_unidad,
            nombre="Unidad Solicitante de Prueba",
            responsable=self.responsable
        )
        self.partida = PartidaPresupuestaria.objects.create(codigo="12345", nombre="Partida de Prueba")

    def test_entidad_str(self):
        self.assertEqual(str(self.entidad), "UABJB-Test")

    def test_gestion_str(self):
        self.assertEqual(str(self.gestion), "2025")

    def test_tipo_unidad_str(self):
        self.assertEqual(str(self.tipo_unidad), "Test-Unidad")

    def test_unidad_solicitante_str(self):
        self.assertEqual(str(self.unidad_solicitante), "Unidad Solicitante de Prueba (Test-Unidad)")

    def test_responsable_str(self):
        self.assertEqual(str(self.responsable), "Test Responsable (Test Cargo)")

    def test_partida_presupuestaria_str(self):
        self.assertEqual(str(self.partida), "12345 - Partida de Prueba")
