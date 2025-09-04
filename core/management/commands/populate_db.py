import random
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import (
    Entidad, Gestion, TipoUnidad, UnidadSolicitante, Responsable, PartidaPresupuestaria
)
from programas.models import Programa, ObjetivoEspecifico
from actividades.models import Actividad, Indicador
from recursos.models import RecursoSolicitado, CatalogoRecurso
from seguimiento.models import SeguimientoIndicador
from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario

class Command(BaseCommand):
    help = 'Populates the database with mock data for testing.'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Starting database population...")

        self.clear_data()
        self.create_core_data()
        self.create_programas_data()
        self.create_actividades_data()
        self.create_recursos_data()
        self.create_seguimiento_data()
        self.create_users_data()

        self.stdout.write(self.style.SUCCESS('Database successfully populated with mock data.'))

    def clear_data(self):
        self.stdout.write("Clearing existing data...")
        User.objects.filter(is_superuser=False).delete()
        SeguimientoIndicador.objects.all().delete()
        RecursoSolicitado.objects.all().delete()
        CatalogoRecurso.objects.all().delete()
        Indicador.objects.all().delete()
        Actividad.objects.all().delete()
        ObjetivoEspecifico.objects.all().delete()
        Programa.objects.all().delete()
        PerfilUsuario.objects.all().delete()
        UnidadSolicitante.objects.all().delete()
        TipoUnidad.objects.all().delete()
        Responsable.objects.all().delete()
        PartidaPresupuestaria.objects.all().delete()
        Gestion.objects.all().delete()
        Entidad.objects.all().delete()
        self.stdout.write("Data cleared.")

    def create_core_data(self):
        self.stdout.write("Creating core data...")
        self.entidad = Entidad.objects.create(nombre="UABJB")
        self.gestion_2023 = Gestion.objects.create(año=2023)
        self.gestion_2024 = Gestion.objects.create(año=2024)

        self.tipo_carrera = TipoUnidad.objects.create(nombre="Carrera")
        self.tipo_instituto = TipoUnidad.objects.create(nombre="Instituto")

        self.responsable1 = Responsable.objects.create(nombre="Juan Pérez", cargo="Director de Carrera")
        self.responsable2 = Responsable.objects.create(nombre="Maria Lopez", cargo="Jefe de Instituto")

        self.unidad1 = UnidadSolicitante.objects.create(
            tipo=self.tipo_carrera,
            nombre="Ingeniería de Sistemas",
            responsable=self.responsable1
        )
        self.unidad2 = UnidadSolicitante.objects.create(
            tipo=self.tipo_instituto,
            nombre="Instituto de Investigación",
            responsable=self.responsable2
        )

        self.partida1 = PartidaPresupuestaria.objects.create(codigo="39500", nombre="Útiles de Oficina")
        self.partida2 = PartidaPresupuestaria.objects.create(codigo="43100", nombre="Equipos de Computación")
        self.stdout.write("Core data created.")

    def create_programas_data(self):
        self.stdout.write("Creating programas data...")
        self.programa1 = Programa.objects.create(
            codigo="100",
            nombre="Formación Profesional",
            objetivo_institucional="Fortalecer la formación profesional.",
            gestion=self.gestion_2024
        )
        self.oe1 = ObjetivoEspecifico.objects.create(
            programa=self.programa1,
            codigo="100-0-1",
            descripcion="Mejorar el proceso de enseñanza-aprendizaje."
        )
        self.stdout.write("Programas data created.")

    def create_actividades_data(self):
        self.stdout.write("Creating actividades data...")
        self.actividad1 = Actividad.objects.create(
            objetivo_especifico=self.oe1,
            gestion=self.gestion_2024,
            unidad_solicitante=self.unidad1,
            codigo="A001",
            nombre="Capacitación docente",
            responsable=self.responsable1,
            producto_esperado="Docentes capacitados en nuevas tecnologías.",
            mes_inicio="Febrero",
            mes_fin="Marzo",
            monto_asignado=5000.00
        )
        self.indicador1 = Indicador.objects.create(
            actividad=self.actividad1,
            descripcion="N° de docentes capacitados",
            unidad_medida="Número",
            linea_base="0",
            meta="20",
            medio_verificacion="Listas de asistencia."
        )
        self.stdout.write("Actividades data created.")

    def create_recursos_data(self):
        self.stdout.write("Creating recursos data...")
        self.catalogo1 = CatalogoRecurso.objects.create(
            tipo='material',
            descripcion='Papel Bond Tamaño Carta',
            partida_presupuestaria=self.partida1,
            unidad_medida_sugerida='Paquete'
        )
        self.recurso1 = RecursoSolicitado.objects.create(
            actividad=self.actividad1,
            detalle="Compra de material de escritorio.",
            unidad_medida="Global",
            partida_presupuestaria=self.partida1,
            cantidad_requerida=1,
            costo_unitario=1500.00,
            mes_requerimiento="Febrero"
        )
        self.stdout.write("Recursos data created.")

    def create_seguimiento_data(self):
        self.stdout.write("Creating seguimiento data...")
        SeguimientoIndicador.objects.create(
            indicador=self.indicador1,
            trimestre="I",
            meta_programada="10",
            ejecutado="12"
        )
        self.stdout.write("Seguimiento data created.")

    def create_users_data(self):
        self.stdout.write("Creating users data...")
        user1 = User.objects.create_user('user1', 'user1@test.com', 'password123')
        # The signal already created a PerfilUsuario, so we get it and update it.
        perfil1 = PerfilUsuario.objects.get(user=user1)
        perfil1.unidad = self.unidad1
        perfil1.cargo = "Técnico"
        perfil1.save()
        self.stdout.write("Users data created.")
