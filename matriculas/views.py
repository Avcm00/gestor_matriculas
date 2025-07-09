import json
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
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
        queryset = SGM_M_Estudiante.objects.select_related('id_ciudad__id_division__id_pais').order_by('apellido', 'nombre')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(cedula__icontains=query) |
                Q(id_ciudad__nombre__icontains=query) |
                Q(apellido__icontains=query)
            )
        return queryset


class EstudianteCreateView(CreateView):
    model = SGM_M_Estudiante
    form_class = EstudianteForm
    template_name = "matriculas/estudiante_form.html"
    success_url = reverse_lazy('estudiante_list')
class EstudianteUpdateView(UpdateView):
    model = SGM_M_Estudiante
    form_class = EstudianteForm
    template_name = "matriculas/estudiante_form.html"
    success_url = reverse_lazy('estudiante_list')


class EstudianteDeleteView(DeleteView):
    model = SGM_M_Estudiante
    template_name = "matriculas/delete.html"
    success_url = reverse_lazy('estudiante_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', self.success_url)
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        return next_url or str(self.success_url)

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

class PeriodoUpdateView(UpdateView):
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
class CarreraUpdateView(UpdateView):
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
class MatriculaCreateFromEstudianteView(CreateView):
    model = SGM_T_Matricula  # Cambia por tu modelo real
    form_class = MatriculaForm
    template_name = 'matriculas/matricula_form.html'
    success_url = reverse_lazy('matricula_list')

    def get_initial(self):
        initial = super().get_initial()
        estudiante_id = self.kwargs.get('pk')
        if estudiante_id:
            initial['id_estudiante'] = estudiante_id
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Deshabilitar selección del estudiante
        estudiante_id = self.kwargs.get('pk')
        if estudiante_id and 'id_estudiante' in form.fields:
            form.fields['id_estudiante'].queryset = SGM_M_Estudiante.objects.filter(pk=estudiante_id)
            form.fields['id_estudiante'].initial = estudiante_id
            form.fields['id_estudiante'].disabled = True  # hace que el campo sea visible pero no editable
        return form


class MatriculaCreateView(CreateView):
    model = SGM_T_Matricula
    form_class = MatriculaForm
    template_name = "matriculas/matricula_form.html"
    success_url = reverse_lazy('matricula_list')
    def get_initial(self):
        initial = super().get_initial()
        estudiante_id = self.kwargs.get('pk')
        if estudiante_id:
            initial['estudiante'] = estudiante_id
        return initial
    
class MatriculaListView(ListView):
    model = SGM_T_Matricula
    template_name = "matriculas/matricula_list.html"
    context_object_name = 'matriculas'
    paginate_by = 20

    def get_queryset(self):
        queryset = SGM_T_Matricula.objects.select_related(
            'id_estudiante',
            'id_periodo',
            'id_estado',
        ).order_by('-fecha_matricula')

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(id_estudiante__nombre__icontains=search_query) |
                Q(id_estudiante__apellido__icontains=search_query) |
                Q(id_estudiante__cedula__icontains=search_query) |
                Q(id_estado__descripcion__icontains=search_query)
            )

        return queryset

class MatriculaUpdateView(UpdateView):
    model = SGM_T_Matricula
    form_class = MatriculaForm
    template_name = "matriculas/matricula_form.html"
    success_url = reverse_lazy('matricula_list')


class MatriculaDeleteView(DeleteView):
    model = SGM_T_Matricula
    template_name = "matriculas/delete.html"
    success_url = reverse_lazy('matricula_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', self.success_url)
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        return next_url or str(self.success_url)
    
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

class PagoUpdateView(UpdateView):
    model = SGM_T_Pago
    form_class = PagoForm
    template_name = "matriculas/pago_form.html"
    success_url = reverse_lazy('pago_list')

class PagoDeleteView(DeleteView):
    model = SGM_T_Pago
    template_name = "matriculas/delete.html"
    success_url = reverse_lazy('pago_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', self.success_url)
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        return next_url or str(self.success_url)
    

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

class PaisUpdateView(UpdateView):
    model = SGM_P_Pais
    form_class = PaisForm
    template_name = "matriculas/pais_form.html"
    success_url = reverse_lazy('pais_list')

class PaisDeleteView(DeleteView):
    model = SGM_P_Pais
    template_name = "matriculas/delete.html"
    success_url = reverse_lazy('pais_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', self.success_url)
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        return next_url or str(self.success_url)
    

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

class DivisionPoliticaUpdateView(UpdateView):
    model = SGM_P_Division_Politica
    form_class = DivisionPoliticaForm
    template_name = "matriculas/divisionpolitica_form.html"
    success_url = reverse_lazy('division_list')

class DivisionPoliticaDeleteView(DeleteView):
    model = SGM_P_Division_Politica
    template_name = "matriculas/delete.html"
    success_url = reverse_lazy('division_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', self.success_url)
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        return next_url or str(self.success_url)
    

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

class CiudadUpdateView(UpdateView):
    model = SGM_P_Ciudad
    form_class = CiudadForm
    template_name = "matriculas/ciudad_form.html"
    success_url = reverse_lazy('ciudad_list')

class CiudadDeleteView(DeleteView):
    model = SGM_P_Ciudad
    template_name = "matriculas/delete.html"
    success_url = reverse_lazy('ciudad_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', self.success_url)
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        return next_url or str(self.success_url)
    


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
class CampoEstudioUpdateView(UpdateView):
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
class OfertaCursoListView(ListView): 
    model = SGM_T_Oferta_Curso_Periodo
    template_name = 'matriculas/oferta_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset().select_related(
            'id_curso', 'id_docente', 'id_periodo', 'id_paralelo'
        )
        curso = self.request.GET.get('curso', '').strip()
        docente = self.request.GET.get('docente', '').strip()
        estado = self.request.GET.get('estado', '').strip()
        periodo = self.request.GET.get('periodo', '').strip()

        if curso:
            queryset = queryset.filter(id_curso_id=curso)

        if docente:
            # Fetch IDs of docentes matching the search criteria
            docentes_ids = SGM_M_Docente.objects.filter(
                Q(nombre__icontains=docente) |
                Q(correo__icontains=docente) |
                Q(celular__icontains=docente) |
                Q(id_titulo_descripcion_icontains=docente) |
                Q(id_ciudad_nombre_icontains=docente)
            ).values_list('id', flat=True)

            queryset = queryset.filter(id_docente_id__in=docentes_ids)

        if estado:
            queryset = queryset.filter(estado=estado)

        if periodo:
            queryset = queryset.filter(id_periodo_id=periodo)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtros'] = {
            'curso': self.request.GET.get('curso', ''),
            'docente': self.request.GET.get('docente', ''),
            'estado': self.request.GET.get('estado', ''),
            'periodo': self.request.GET.get('periodo', ''),
        }
        context['cursos'] = SGM_M_Curso.objects.all()
        context['estados'] = SGM_T_Oferta_Curso_Periodo.ESTADOS
        context['periodos'] = SGM_P_Periodo_Academico.objects.all()
        return context


class OfertaCursoCreateView(CreateView):
    model = SGM_T_Oferta_Curso_Periodo
    form_class = OfertaCursoPeriodoForm
    template_name = 'matriculas/oferta_form.html'
    success_url = reverse_lazy('oferta_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        docentes = list(
            SGM_M_Docente.objects.select_related('id_titulo', 'id_ciudad').values(
            'id', 'nombre', 'correo', 'celular', 'direccion',
            'id_titulo__descropcion',
            'id_ciudad__nombre'
        )
    )
        context['docentes_info'] = json.dumps(docentes, cls=DjangoJSONEncoder)
        return context

class OfertaCursoUpdateView(UpdateView):
    model = SGM_T_Oferta_Curso_Periodo
    form_class = OfertaCursoPeriodoForm
    template_name = 'matriculas/oferta_form.html'
    success_url = reverse_lazy('oferta_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        docentes = list(
            SGM_M_Docente.objects.select_related('id_titulo', 'id_ciudad').values(
            'id', 'nombre', 'correo', 'celular', 'direccion',
            'id_titulo__descripcion',
            'id_ciudad__nombre'
        )
    )
        context['docentes_info'] = json.dumps(docentes, cls=DjangoJSONEncoder)
        return context

class OfertaCursoDeleteView(DeleteView):
    model = SGM_T_Oferta_Curso_Periodo
    template_name = 'matriculas/delete.html'
    success_url = reverse_lazy('oferta_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', self.success_url)
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        return next_url or str(self.success_url)
    
# ——— Cursos ———
class CursoListView(ListView):
    model = SGM_M_Curso
    template_name = 'matriculas/curso_list.html'
    context_object_name = 'object_list'

class CursoCreateView(CreateView):
    model = SGM_M_Curso
    form_class = CursoForm
    template_name = 'matriculas/curso_form.html'
    success_url = reverse_lazy('curso_list')

class CursoUpdateView(UpdateView):
    model = SGM_M_Curso
    form_class = CursoForm
    template_name = 'matriculas/curso_form.html'
    success_url = reverse_lazy('curso_list')

class CursoDeleteView(DeleteView):
    model = SGM_M_Curso
    template_name = 'matriculas/delete.html'
    success_url = reverse_lazy('curso_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', self.success_url)
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        return next_url or str(self.success_url)