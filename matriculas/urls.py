from django.urls import path
from .views import (
    
    EstudianteDeleteView,
    EstudianteListView,
    EstudianteCreateView,
    EstudianteUpdateView,
    MatriculaCreateView,
    MatriculaListView,
    MatriculaUpdateView,
    MatriculaDeleteView,
    PeriodoListView,
    PeriodoCreateView,
    EstadoMatriculaListView,
    EstadoMatriculaCreateView,
    CarreraListView,
    CarreraCreateView,
    ModalidadListView,
    ModalidadCreateView,
    MetodoPagoListView,
    MetodoPagoCreateView,
    PagoListView,
    PagoCreateView,
    PaisListView,
    PaisCreateView,
    DivisionPoliticaListView,  
    DivisionPoliticaCreateView,
    CiudadListView,
    CiudadCreateView,
    CampoEstudioListView,
    CampoEstudioCreateView,
)

urlpatterns = [
    # — Estudiantes y Matrículas —
    path('', EstudianteListView.as_view(), name='estudiante_list'),
    path('estudiantes/nuevo/', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('estudiantes/editar/<int:pk>/', EstudianteUpdateView.as_view(), name='estudiante_update'),
    path('estudiantes/eliminar/<int:pk>/', EstudianteDeleteView.as_view(), name='estudiante_delete'),

    
    path('matriculas/', MatriculaListView.as_view(), name='matricula_list'),
    path('matriculas/crear/', MatriculaCreateView.as_view(), name='matricula_create'),
    path('matriculas/editar/<int:pk>/', MatriculaUpdateView.as_view(), name='matricula_update'),
    path('matriculas/eliminar/<int:pk>/', MatriculaDeleteView.as_view(), name='matricula_delete'),
    
    # — Períodos Académicos —
    path('periodos/', PeriodoListView.as_view(), name='periodo_list'),
    path('periodos/nuevo/', PeriodoCreateView.as_view(), name='periodo_create'),

    # — Estados de Matrícula —
    path('estados/', EstadoMatriculaListView.as_view(), name='estado_list'),
    path('estados/nuevo/', EstadoMatriculaCreateView.as_view(), name='estado_create'),

    # — Carreras —
    path('carreras/', CarreraListView.as_view(), name='carrera_list'),
    path('carreras/nuevo/', CarreraCreateView.as_view(), name='carrera_create'),

    # — Modalidades —
    path('modalidades/', ModalidadListView.as_view(), name='modalidad_list'),
    path('modalidades/nuevo/', ModalidadCreateView.as_view(), name='modalidad_create'),

    # — Métodos de Pago —
    path('metodos_pago/', MetodoPagoListView.as_view(), name='metodopago_list'),
    path('metodos_pago/nuevo/', MetodoPagoCreateView.as_view(), name='metodopago_create'),

    # — Pagos —
    path('pagos/', PagoListView.as_view(), name='pago_list'),
    path('pagos/nuevo/', PagoCreateView.as_view(), name='pago_create'),
     
    # URLs para Países
    path('paises/', PaisListView.as_view(), name='pais_list'),
    path('paises/nuevo/', PaisCreateView.as_view(), name='pais_create'),
    
    # URLs para Divisiones Políticas
    path('divisiones/', DivisionPoliticaListView.as_view(), name='division_list'),
    path('divisiones/nueva/', DivisionPoliticaCreateView.as_view(), name='division_create'),
    
    # URLs para Ciudades
    path('ciudades/', CiudadListView.as_view(), name='ciudad_list'),
    path('ciudades/nueva/', CiudadCreateView.as_view(), name='ciudad_create'),
    
    # URLs para Campos de Estudio
    path('campos/', CampoEstudioListView.as_view(), name='campo_list'),
    path('campos/nuevo/', CampoEstudioCreateView.as_view(), name='campo_create'),
]
