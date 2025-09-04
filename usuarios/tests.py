from django.test import TestCase
from django.contrib.auth.models import User
from .models import PerfilUsuario
from core.models import UnidadSolicitante, TipoUnidad, Responsable

class UsuariosModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        tipo_unidad = TipoUnidad.objects.create(nombre="Test-Unidad")
        responsable = Responsable.objects.create(nombre="Test Responsable", cargo="Test Cargo")
        self.unidad = UnidadSolicitante.objects.create(
            tipo=tipo_unidad,
            nombre="Unidad Solicitante de Prueba",
            responsable=responsable
        )

    def test_perfil_usuario_creado_con_signal(self):
        self.assertTrue(PerfilUsuario.objects.filter(user=self.user).exists())

    def test_perfil_usuario_str(self):
        perfil = PerfilUsuario.objects.get(user=self.user)
        perfil.cargo = "Test Cargo"
        perfil.save()
        self.assertEqual(str(perfil), "testuser - Test Cargo")

    def test_perfil_usuario_str_sin_cargo(self):
        perfil = PerfilUsuario.objects.get(user=self.user)
        self.assertEqual(str(perfil), "testuser - Sin cargo")

    def test_asignar_unidad_a_perfil(self):
        perfil = PerfilUsuario.objects.get(user=self.user)
        perfil.unidad = self.unidad
        perfil.save()
        self.assertEqual(perfil.unidad, self.unidad)
