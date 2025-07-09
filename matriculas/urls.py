from django.urls import path
from .views import (
    CampoEstudioUpdateView,
    CarreraUpdateView,
    CiudadDeleteView,
    CiudadUpdateView,
    CursoCreateView,
    CursoDeleteView,
    CursoListView,
    CursoUpdateView,
    DivisionPoliticaDeleteView,
    DivisionPoliticaUpdateView,
    EstudianteDeleteView,
    EstudianteListView,
    EstudianteCreateView,
    EstudianteUpdateView,
    MatriculaCreateFromEstudianteView,
    MatriculaCreateView,
    MatriculaListView,
    MatriculaUpdateView,
    MatriculaDeleteView,
    OfertaCursoCreateView,
    OfertaCursoDeleteView,
    OfertaCursoListView,
    OfertaCursoUpdateView,
    PagoDeleteView,
    PagoUpdateView,
    PaisDeleteView,
    PaisUpdateView,
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
    PeriodoUpdateView,
)

urlpatterns = [
    # — Estudiantes y Matrículas —
    path('', EstudianteListView.as_view(), name='estudiante_list'),
    path('estudiantes/nuevo/', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('estudiantes/editar/<int:pk>/', EstudianteUpdateView.as_view(), name='estudiante_update'),
    path('estudiantes/eliminar/<int:pk>/', EstudianteDeleteView.as_view(), name='estudiante_delete'),

    path('matriculas/crear/estudiante/<int:pk>/', MatriculaCreateFromEstudianteView.as_view(), name='matricula_create_from_estudiante'),

    path('matriculas/', MatriculaListView.as_view(), name='matricula_list'),
    path('matriculas/crear/', MatriculaCreateView.as_view(), name='matricula_create'),
    path('matriculas/editar/<int:pk>/', MatriculaUpdateView.as_view(), name='matricula_update'),
    path('matriculas/eliminar/<int:pk>/', MatriculaDeleteView.as_view(), name='matricula_delete'),
    
    # — Períodos Académicos —
    path('periodos/', PeriodoListView.as_view(), name='periodo_list'),
    path('periodos/nuevo/', PeriodoCreateView.as_view(), name='periodo_create'),
    path('periodos/editar/<int:pk>/', PeriodoUpdateView.as_view(), name='periodo_update'),

    # — Estados de Matrícula —
    path('estados/', EstadoMatriculaListView.as_view(), name='estado_list'),
    path('estados/nuevo/', EstadoMatriculaCreateView.as_view(), name='estado_create'),
# — Cursos —
    path('cursos/', CursoListView.as_view(), name='curso_list'),
    path('cursos/nuevo/', CursoCreateView.as_view(), name='curso_create'),
    path('cursos/<int:pk>/editar/', CursoUpdateView.as_view(), name='curso_update'),
    path('cursos/<int:pk>/eliminar/', CursoDeleteView.as_view(), name='curso_delete'),
    # — Ofertas de Cursos por Período —
    path('ofertas/', OfertaCursoListView.as_view(), name='oferta_list'),
    path('ofertas/nueva/', OfertaCursoCreateView.as_view(), name='oferta_create'),
    path('ofertas/<int:pk>/editar/', OfertaCursoUpdateView.as_view(), name='oferta_update'),
    path('ofertas/<int:pk>/eliminar/', OfertaCursoDeleteView.as_view(), name='oferta_delete'),
    # — Carreras —
    path('carreras/', CarreraListView.as_view(), name='carrera_list'),
    path('carreras/nuevo/', CarreraCreateView.as_view(), name='carrera_create'),
    path('carreras/editar/<int:pk>/', CarreraUpdateView.as_view(), name='carrera_update'),

    # — Modalidades —
    path('modalidades/', ModalidadListView.as_view(), name='modalidad_list'),
    path('modalidades/nuevo/', ModalidadCreateView.as_view(), name='modalidad_create'),

    # — Métodos de Pago —
    path('metodos_pago/', MetodoPagoListView.as_view(), name='metodopago_list'),
    path('metodos_pago/nuevo/', MetodoPagoCreateView.as_view(), name='metodopago_create'),

    # — Pagos —
    path('pagos/', PagoListView.as_view(), name='pago_list'),
    path('pagos/nuevo/', PagoCreateView.as_view(), name='pago_create'),
    path('pagos/<int:pk>/editar/', PagoUpdateView.as_view(), name='pago_update'),
    path('pagos/<int:pk>/eliminar/', PagoDeleteView.as_view(), name='pago_delete'),
     
     # URLs para Países
    path('paises/', PaisListView.as_view(), name='pais_list'),
    path('paises/nuevo/', PaisCreateView.as_view(), name='pais_create'),
    path('paises/<int:pk>/editar/', PaisUpdateView.as_view(), name='pais_update'),
    path('paises/<int:pk>/eliminar/', PaisDeleteView.as_view(), name='pais_delete'),
    
    # URLs para Divisiones Políticas
    path('divisiones/', DivisionPoliticaListView.as_view(), name='division_list'),
    path('divisiones/nueva/', DivisionPoliticaCreateView.as_view(), name='division_create'),
    path('division/<int:pk>/editar/', DivisionPoliticaUpdateView.as_view(), name='division_update'),
    path('division/<int:pk>/eliminar/', DivisionPoliticaDeleteView.as_view(), name='division_delete'),
    # URLs para Ciudades
    path('ciudades/', CiudadListView.as_view(), name='ciudad_list'),
    path('ciudades/nueva/', CiudadCreateView.as_view(), name='ciudad_create'),
    path('ciudad/<int:pk>/editar/', CiudadUpdateView.as_view(), name='ciudad_update'),
    path('ciudad/<int:pk>/eliminar/', CiudadDeleteView.as_view(), name='ciudad_delete'),
    
    # URLs para Campos de Estudio
    path('campos/', CampoEstudioListView.as_view(), name='campo_list'),
    path('campos/nuevo/', CampoEstudioCreateView.as_view(), name='campo_create'),
    path('campos/editar/<int:pk>/', CampoEstudioUpdateView.as_view(), name='campo_update'),
]
