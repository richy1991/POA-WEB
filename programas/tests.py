from django.test import TestCase
from .models import Programa, ObjetivoEspecifico
from core.models import Gestion

class ProgramasModelTest(TestCase):
    def setUp(self):
        self.gestion = Gestion.objects.create(año=2025)
        self.programa = Programa.objects.create(
            codigo="999",
            nombre="Programa de Prueba",
            objetivo_institucional="Objetivo de prueba",
            gestion=self.gestion
        )
        self.objetivo_especifico = ObjetivoEspecifico.objects.create(
            programa=self.programa,
            codigo="999-9-9",
            descripcion="Objetivo Específico de Prueba"
        )

    def test_programa_str(self):
        self.assertEqual(str(self.programa), "999 - Programa de Prueba")

    def test_objetivo_especifico_str(self):
        self.assertEqual(str(self.objetivo_especifico), "999-9-9 - Objetivo Específico de Prueba")
