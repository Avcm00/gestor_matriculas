from django.contrib import admin
from .models import (
    SGM_P_Pais,
    SGM_P_Division_Politica,
    SGM_P_Ciudad,
    SGM_P_Campo_Estudio,
    SGM_P_Modalidad,
    SGM_P_Periodo_Academico,
    SGM_P_Estado_Matricula,
    SGM_P_Metodo_Pago,
    SGM_P_Tipo_Evaluacion,
    SGM_P_Jornada,
    SGM_P_Paralelo,
    SGM_P_Tipo_Asignatura,
    SGM_P_Tipo_Aula,
    SGM_P_Edificio,
    SGM_P_Turno,
    SGM_P_Titulo,
    SGM_P_Asignatura,
    SGM_P_Carrera_Modalidad,
    SGM_P_Calificacion,
    SGM_M_Carrera,
    SGM_M_Estudiante,
    SGM_M_Docente,
    SGM_M_Aula,
    SGM_M_Horario,
    SGM_M_Curso,
    SGM_M_Detalle_Matricula,
    SGM_T_Matricula,
    SGM_T_Pago,
    SGM_T_Oferta_Curso_Periodo,
    SGM_T_Curso_Horario,
)

# ============================================================================
# MODELOS PARAMETRIZADOS (Configuración base)
# ============================================================================

@admin.register(SGM_P_Pais)
class SGM_P_PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(SGM_P_Division_Politica)
class SGM_P_DivisionPoliticaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'id_pais')
    list_filter = ('id_pais',)
    search_fields = ('nombre',)

@admin.register(SGM_P_Ciudad)
class SGM_P_CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'id_division')
    list_filter = ('id_division__id_pais',)
    search_fields = ('nombre',)

@admin.register(SGM_P_Campo_Estudio)
class SGM_P_CampoEstudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(SGM_P_Modalidad)
class SGM_P_ModalidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(SGM_P_Periodo_Academico)
class SGM_P_PeriodoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_inicio', 'fecha_fin', 'inicio_matricula', 'fin_matricula')
    list_filter = ('fecha_inicio', 'fecha_fin')
    search_fields = ('nombre',)

@admin.register(SGM_P_Estado_Matricula)
class SGM_P_EstadoMatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(SGM_P_Metodo_Pago)
class SGM_P_MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(SGM_P_Tipo_Evaluacion)
class SGM_P_TipoEvaluacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(SGM_P_Jornada)
class SGM_P_JornadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(SGM_P_Paralelo)
class SGM_P_ParaleloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'id_jornada')
    list_filter = ('id_jornada',)
    search_fields = ('nombre',)

@admin.register(SGM_P_Tipo_Asignatura)
class SGM_P_TipoAsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(SGM_P_Tipo_Aula)
class SGM_P_TipoAulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(SGM_P_Edificio)
class SGM_P_EdificioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(SGM_P_Turno)
class SGM_P_TurnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'hora_inicio', 'hora_fin')
    list_filter = ('nombre',)

@admin.register(SGM_P_Titulo)
class SGM_P_TituloAdmin(admin.ModelAdmin):
    list_display = ('id', 'descropcion')
    search_fields = ('descropcion',)

@admin.register(SGM_P_Asignatura)
class SGM_P_AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nivel', 'horas_semanales', 'creditos', 'id_tipo', 'id_asignatura_aprobada')
    list_filter = ('nivel', 'id_tipo')
    search_fields = ('nombre',)

@admin.register(SGM_P_Carrera_Modalidad)
class SGM_P_CarreraModalidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_carrera', 'id_modalidad')
    list_filter = ('id_carrera', 'id_modalidad')

@admin.register(SGM_P_Calificacion)
class SGM_P_CalificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_oferta', 'id_tipo_evaluacion', 'nota', 'fecha', 'estado_nota')
    list_filter = ('id_tipo_evaluacion', 'fecha')
    search_fields = ('id_oferta__id_curso__nombre',)

# ============================================================================
# MODELOS MAESTROS (Entidades principales)
# ============================================================================

@admin.register(SGM_M_Carrera)
class SGM_M_CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'id_campo', 'estado', 'semestres')
    list_filter = ('id_campo', 'estado')
    search_fields = ('nombre',)

@admin.register(SGM_M_Estudiante)
class SGM_M_EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'cedula', 'correo', 'id_ciudad', 'genero')
    list_filter = ('id_ciudad', 'genero')
    search_fields = ('nombre', 'apellido', 'cedula', 'correo')

@admin.register(SGM_M_Docente)
class SGM_M_DocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'id_titulo', 'id_ciudad', 'fecha_ingreso')
    list_filter = ('id_titulo', 'id_ciudad')
    search_fields = ('nombre', 'correo')

@admin.register(SGM_M_Aula)
class SGM_M_AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_aula', 'capacidad', 'id_tipo_aula', 'id_edificio')
    list_filter = ('id_tipo_aula', 'id_edificio')
    search_fields = ('numero_aula',)

@admin.register(SGM_M_Horario)
class SGM_M_HorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'dia', 'hora_inicio', 'hora_fin', 'id_turno')
    list_filter = ('dia', 'id_turno')

@admin.register(SGM_M_Curso)
class SGM_M_CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'id_asignatura')
    list_filter = ('id_asignatura',)
    search_fields = ('nombre',)

@admin.register(SGM_M_Detalle_Matricula)
class SGM_M_DetalleMatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_matricula', 'id_oferta')
    list_filter = ('id_matricula__id_periodo',)
    search_fields = ('id_matricula__id_estudiante__nombre',)

# ============================================================================
# MODELOS TRANSACCIONALES (Operaciones)
# ============================================================================

@admin.register(SGM_T_Matricula)
class SGM_T_MatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'id_estudiante', 'id_modalidad_carrera',
        'id_periodo', 'id_estado', 'fecha_matricula'
    )
    list_filter = ('id_periodo', 'id_estado')
    search_fields = ('id_estudiante__nombre', 'id_estudiante__apellido')

@admin.register(SGM_T_Pago)
class SGM_T_PagoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'id_matricula', 'fecha_pago',
        'monto', 'id_metodo', 'estado'
    )
    list_filter = ('id_metodo', 'estado')
    search_fields = ('id_matricula__id_estudiante__nombre',)

@admin.register(SGM_T_Oferta_Curso_Periodo)
class SGM_T_OfertaCursoPeriodoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'id_curso', 'id_periodo', 'id_docente',
        'id_paralelo', 'cupos_max', 'cupos_disponibles', 'estado'
    )
    list_filter = ('id_periodo', 'estado', 'id_paralelo')
    search_fields = ('id_curso__nombre', 'id_docente__nombre')

@admin.register(SGM_T_Curso_Horario)
class SGM_T_CursoHorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_oferta', 'id_horario', 'id_aula')
    list_filter = ('id_horario__dia', 'id_aula__id_edificio')
    search_fields = ('id_oferta__id_curso__nombre',)