from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import (
    SGM_P_Campo_Estudio,
    SGM_P_Ciudad,
    SGM_P_Division_Politica,
    SGM_M_Estudiante,
    SGM_P_Pais,
    SGM_P_Periodo_Academico,
    SGM_P_Estado_Matricula,
    SGM_M_Carrera,
    SGM_P_Modalidad,
    SGM_T_Matricula,
    SGM_P_Metodo_Pago,
    SGM_T_Pago,
    SGM_M_Docente,
    SGM_M_Aula,
    SGM_P_Asignatura,
    SGM_M_Curso,
    SGM_T_Oferta_Curso_Periodo,
)
from .forms import (
    CampoEstudioForm,
    CiudadForm,
    DivisionPoliticaForm,
    EstudianteForm,
    MatriculaForm,
    PaisForm,
    PeriodoAcademicoForm,
    EstadoMatriculaForm,
    CarreraForm,
    ModalidadForm,
    MetodoPagoForm,
    PagoForm,
    DocenteForm,
    AulaForm,
    AsignaturaForm,
    CursoForm,
    OfertaCursoPeriodoForm,
)

# ——— Estudiantes ———
class EstudianteListView(ListView):
    model = SGM_M_Estudiante
    template_name = "matriculas/estudiante_list.html"
    context_object_name = 'estudiantes'
    paginate_by = 20

    def get_queryset(self):
        return SGM_M_Estudiante.objects.select_related('id_ciudad__id_division__id_pais').order_by('apellido', 'nombre')

class EstudianteCreateView(CreateView):
    model = SGM_M_Estudiante
    form_class = EstudianteForm
    template_name = "matriculas/estudiante_form.html"
    success_url = reverse_lazy('estudiante_list')


# ——— Períodos Académicos ———
class PeriodoListView(ListView):
    model = SGM_P_Periodo_Academico
    template_name = "matriculas/periodoacademico_list.html"
    context_object_name = 'periodos'

class PeriodoCreateView(CreateView):
    model = SGM_P_Periodo_Academico
    form_class = PeriodoAcademicoForm
    template_name = "matriculas/periodoacademico_form.html"
    success_url = reverse_lazy('periodo_list')


# ——— Estados de Matrícula ———
class EstadoMatriculaListView(ListView):
    model = SGM_P_Estado_Matricula
    template_name = "matriculas/estadomatricula_list.html"
    context_object_name = 'estados'

class EstadoMatriculaCreateView(CreateView):
    model = SGM_P_Estado_Matricula
    form_class = EstadoMatriculaForm
    template_name = "matriculas/estadomatricula_form.html"
    success_url = reverse_lazy('estado_list')


# ——— Carreras ———
class CarreraListView(ListView):
    model = SGM_M_Carrera
    template_name = "matriculas/carrera_list.html"
    context_object_name = 'carreras'

    def get_queryset(self):
        return SGM_M_Carrera.objects.select_related('id_campo').order_by('nombre')

class CarreraCreateView(CreateView):
    model = SGM_M_Carrera
    form_class = CarreraForm
    template_name = "matriculas/carrera_form.html"
    success_url = reverse_lazy('carrera_list')


# ——— Modalidades ———
class ModalidadListView(ListView):
    model = SGM_P_Modalidad
    template_name = "matriculas/modalidad_list.html"
    context_object_name = 'modalidades'

class ModalidadCreateView(CreateView):
    model = SGM_P_Modalidad
    form_class = ModalidadForm
    template_name = "matriculas/modalidad_form.html"
    success_url = reverse_lazy('modalidad_list')


# ——— Matrículas ———
class MatriculaCreateView(CreateView):
    model = SGM_T_Matricula
    form_class = MatriculaForm
    template_name = "matriculas/matricula_form.html"
    success_url = reverse_lazy('matricula_list')

class MatriculaListView(ListView):
    model = SGM_T_Matricula
    template_name = "matriculas/matricula_list.html"
    context_object_name = 'matriculas'
    paginate_by = 20
    
    def get_queryset(self):
        return SGM_T_Matricula.objects.select_related(
            'id_estudiante', 
            'id_modalidad_carrera__id_carrera', 
            'id_modalidad_carrera__id_modalidad',
            'id_periodo',
            'id_estado'
        ).order_by('-fecha_matricula')


# ——— Métodos de Pago ———
class MetodoPagoListView(ListView):
    model = SGM_P_Metodo_Pago
    template_name = "matriculas/metodopago_list.html"
    context_object_name = 'metodos'

class MetodoPagoCreateView(CreateView):
    model = SGM_P_Metodo_Pago
    form_class = MetodoPagoForm
    template_name = "matriculas/metodopago_form.html"
    success_url = reverse_lazy('metodopago_list')


# ——— Pagos ———
class PagoListView(ListView):
    model = SGM_T_Pago
    template_name = "matriculas/pago_list.html"
    context_object_name = 'pagos'

    def get_queryset(self):
        return SGM_T_Pago.objects.select_related(
            'id_matricula__id_estudiante',
            'id_metodo'
        ).order_by('-fecha_pago')

class PagoCreateView(CreateView):
    model = SGM_T_Pago
    form_class = PagoForm
    template_name = "matriculas/pago_form.html"
    success_url = reverse_lazy('pago_list')


# ——— Países ———
class PaisListView(ListView):
    model = SGM_P_Pais
    template_name = "matriculas/pais_list.html"
    context_object_name = 'paises'

class PaisCreateView(CreateView):
    model = SGM_P_Pais
    form_class = PaisForm
    template_name = "matriculas/pais_form.html"
    success_url = reverse_lazy('pais_list')


# ——— Divisiones Políticas ———
class DivisionPoliticaListView(ListView):
    model = SGM_P_Division_Politica
    template_name = "matriculas/divisionpolitica_list.html"
    context_object_name = 'divisiones'

    def get_queryset(self):
        return SGM_P_Division_Politica.objects.select_related('id_pais').order_by('id_pais__nombre', 'nombre')

class DivisionPoliticaCreateView(CreateView):
    model = SGM_P_Division_Politica
    form_class = DivisionPoliticaForm
    template_name = "matriculas/divisionpolitica_form.html"
    success_url = reverse_lazy('division_list')


# ——— Ciudades ———
class CiudadListView(ListView):
    model = SGM_P_Ciudad
    template_name = "matriculas/ciudad_list.html"
    context_object_name = 'ciudades'

    def get_queryset(self):
        return SGM_P_Ciudad.objects.select_related('id_division__id_pais').order_by('id_division__id_pais__nombre', 'id_division__nombre', 'nombre')

class CiudadCreateView(CreateView):
    model = SGM_P_Ciudad
    form_class = CiudadForm
    template_name = "matriculas/ciudad_form.html"
    success_url = reverse_lazy('ciudad_list')


# ——— Campos de Estudio ———
class CampoEstudioListView(ListView):
    model = SGM_P_Campo_Estudio
    template_name = "matriculas/campoestudio_list.html"
    context_object_name = 'campos'

class CampoEstudioCreateView(CreateView):
    model = SGM_P_Campo_Estudio
    form_class = CampoEstudioForm
    template_name = "matriculas/campoestudio_form.html"
    success_url = reverse_lazy('campo_list')


# ——— Docentes ———
class DocenteListView(ListView):
    model = SGM_M_Docente
    template_name = "matriculas/docente_list.html"
    context_object_name = 'docentes'

    def get_queryset(self):
        return SGM_M_Docente.objects.select_related('id_titulo', 'id_ciudad').order_by('nombre')

class DocenteCreateView(CreateView):
    model = SGM_M_Docente
    form_class = DocenteForm
    template_name = "matriculas/docente_form.html"
    success_url = reverse_lazy('docente_list')


# ——— Aulas ———
class AulaListView(ListView):
    model = SGM_M_Aula
    template_name = "matriculas/aula_list.html"
    context_object_name = 'aulas'

    def get_queryset(self):
        return SGM_M_Aula.objects.select_related('id_tipo_aula', 'id_edificio').order_by('id_edificio__nombre', 'numero_aula')

class AulaCreateView(CreateView):
    model = SGM_M_Aula
    form_class = AulaForm
    template_name = "matriculas/aula_form.html"
    success_url = reverse_lazy('aula_list')


# ——— Asignaturas ———
class AsignaturaListView(ListView):
    model = SGM_P_Asignatura
    template_name = "matriculas/asignatura_list.html"
    context_object_name = 'asignaturas'

    def get_queryset(self):
        return SGM_P_Asignatura.objects.select_related('id_tipo', 'id_asignatura_prerrequisito').order_by('nivel', 'nombre')

class AsignaturaCreateView(CreateView):
    model = SGM_P_Asignatura
    form_class = AsignaturaForm
    template_name = "matriculas/asignatura_form.html"
    success_url = reverse_lazy('asignatura_list')


# ——— Cursos ———
class CursoListView(ListView):
    model = SGM_M_Curso
    template_name = "matriculas/curso_list.html"
    context_object_name = 'cursos'

    def get_queryset(self):
        return SGM_M_Curso.objects.select_related('id_asignatura').order_by('nombre')

class CursoCreateView(CreateView):
    model = SGM_M_Curso
    form_class = CursoForm
    template_name = "matriculas/curso_form.html"
    success_url = reverse_lazy('curso_list')


# ——— Ofertas de Cursos ———
class OfertaCursoListView(ListView):
    model = SGM_T_Oferta_Curso_Periodo
    template_name = "matriculas/ofertacurso_list.html"
    context_object_name = 'ofertas'

    def get_queryset(self):
        return SGM_T_Oferta_Curso_Periodo.objects.select_related(
            'id_curso__id_asignatura',
            'id_periodo',
            'id_docente',
            'id_paralelo__id_jornada'
        ).order_by('-id_periodo__fecha_inicio', 'id_curso__nombre')

class OfertaCursoCreateView(CreateView):
    model = SGM_T_Oferta_Curso_Periodo
    form_class = OfertaCursoPeriodoForm
    template_name = "matriculas/ofertacurso_form.html"
    success_url = reverse_lazy('oferta_list')