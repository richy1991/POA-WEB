from django.test import TestCase
from .models import CatalogoRecurso, RecursoSolicitado
from actividades.models import Actividad
from core.models import Gestion, UnidadSolicitante, TipoUnidad, Responsable, PartidaPresupuestaria
from programas.models import Programa, ObjetivoEspecifico
from decimal import Decimal

class RecursosModelTest(TestCase):
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
        actividad = Actividad.objects.create(
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
        self.partida = PartidaPresupuestaria.objects.create(codigo="12345", nombre="Partida de Prueba")
        self.catalogo_recurso = CatalogoRecurso.objects.create(
            tipo='material',
            descripcion='Recurso de prueba',
            partida_presupuestaria=self.partida
        )
        self.recurso_solicitado = RecursoSolicitado.objects.create(
            actividad=actividad,
            detalle="Detalle de prueba",
            unidad_medida="Unidad",
            partida_presupuestaria=self.partida,
            cantidad_requerida=10,
            costo_unitario=Decimal('12.50')
        )

    def test_catalogo_recurso_str(self):
        self.assertEqual(str(self.catalogo_recurso), "S/C - Recurso de prueba...")

    def test_recurso_solicitado_str(self):
        self.assertEqual(str(self.recurso_solicitado), "Detalle de prueba - 125.00 Bs.")

    def test_recurso_solicitado_costo_total(self):
        self.assertEqual(self.recurso_solicitado.costo_total, Decimal('125.00'))
