# informes/views.py
from django.shortcuts import render
from django.db.models import Q, Sum
from actividades.models import Actividad

def reporte_poa(request):
    """
    Vista principal para mostrar el reporte del POA con filtros.
    """
    # Obtener todas las actividades
    actividades = Actividad.objects.select_related(
        'objetivo_especifico__programa',
        'unidad_solicitante',
        'responsable',
        'gestion'
    ).prefetch_related('indicadores', 'recursos_solicitados').all()

    # Aplicar filtros
    filtros_aplicados = {}

    gestion_id = request.GET.get('gestion')
    if gestion_id:
        actividades = actividades.filter(gestion__id=gestion_id)
        filtros_aplicados['gestion'] = gestion_id

    programa_id = request.GET.get('programa')
    if programa_id:
        actividades = actividades.filter(objetivo_especifico__programa__id=programa_id)
        filtros_aplicados['programa'] = programa_id

    unidad_id = request.GET.get('unidad')
    if unidad_id:
        actividades = actividades.filter(unidad_solicitante__id=unidad_id)
        filtros_aplicados['unidad'] = unidad_id

    estado = request.GET.get('estado')
    if estado:
        actividades = actividades.filter(estado=estado)
        filtros_aplicados['estado'] = estado

    # Calcular totales
    total_actividades = actividades.count()
    total_monto = actividades.aggregate(total=Sum('monto_asignado'))['total'] or 0

    # Datos para el template
    context = {
        'actividades': actividades,
        'total_actividades': total_actividades,
        'total_monto': total_monto,
        'filtros_aplicados': filtros_aplicados,

        # Opciones para los filtros
        'gestiones': actividades.values('gestion__id', 'gestion__año').distinct().order_by('-gestion__año'),
        'programas': actividades.values(
            'objetivo_especifico__programa__id',
            'objetivo_especifico__programa__codigo',
            'objetivo_especifico__programa__nombre'
        ).distinct().order_by('objetivo_especifico__programa__codigo'),
        'unidades': actividades.values(
            'unidad_solicitante__id',
            'unidad_solicitante__nombre'
        ).distinct().order_by('unidad_solicitante__nombre'),
        'estados': Actividad.ESTADO_CHOICES,
    }
    return render(request, 'informes/reporte_poa.html', context)