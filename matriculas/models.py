from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# ============================================================================
# MODELOS PARAMETRIZADOS (Configuración base)
# ============================================================================

class SGM_P_Pais(models.Model):
    """Modelo para países"""
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        db_table = "SGM_P_Pais"
    
    def __str__(self):
        return self.nombre


class SGM_P_Division_Politica(models.Model):
    """Modelo para divisiones políticas (provincias, estados, etc.)"""
    nombre = models.CharField(max_length=100)
    id_pais = models.ForeignKey(SGM_P_Pais, on_delete=models.CASCADE, related_name='divisiones')
    
    class Meta:
        verbose_name = "División Política"
        verbose_name_plural = "Divisiones Políticas"
        db_table = "SGM_P_Division_Politica"
        unique_together = ('nombre', 'id_pais')
    
    def __str__(self):
        return f"{self.nombre}, {self.id_pais.nombre}"


class SGM_P_Ciudad(models.Model):
    """Modelo para ciudades"""
    nombre = models.CharField(max_length=100)
    id_division = models.ForeignKey(SGM_P_Division_Politica, on_delete=models.CASCADE, related_name='ciudades')
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        db_table = "SGM_P_Ciudad"
        unique_together = ('nombre', 'id_division')
    
    def __str__(self):
        return f"{self.nombre}, {self.id_division.nombre}"


class SGM_P_Campo_Estudio(models.Model):
    """Modelo para campos de estudio"""
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Campo de Estudio"
        verbose_name_plural = "Campos de Estudio"
        db_table = "SGM_P_Campo_Estudio"
    
    def __str__(self):
        return self.nombre


class SGM_P_Modalidad(models.Model):
    """Modelo para modalidades de estudio"""
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"
        db_table = "SGM_P_Modalidad"
    
    def __str__(self):
        return self.nombre


class SGM_P_Periodo_Academico(models.Model):
    """Modelo para períodos académicos"""
    nombre = models.CharField(max_length=50, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    inicio_matricula = models.DateField()
    fin_matricula = models.DateField()
    
    class Meta:
        verbose_name = "Período Académico"
        verbose_name_plural = "Períodos Académicos"
        db_table = "SGM_P_Periodo_Academico"
    
    def __str__(self):
        return self.nombre
    
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.fecha_inicio >= self.fecha_fin:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de fin")
        if self.inicio_matricula >= self.fin_matricula:
            raise ValidationError("El inicio de matrícula debe ser anterior al fin de matrícula")


class SGM_P_Estado_Matricula(models.Model):
    """Modelo para estados de matrícula"""
    ESTADOS = [
        ('ACTIVA', 'Activa'),
        ('INACTIVA', 'Inactiva'),
        ('CANCELADA', 'Cancelada'),
        ('SUSPENDIDA', 'Suspendida'),
    ]
    
    descripcion = models.CharField(max_length=50, choices=ESTADOS, unique=True)
    
    class Meta:
        verbose_name = "Estado de Matrícula"
        verbose_name_plural = "Estados de Matrícula"
        db_table = "SGM_P_Estado_Matricula"
    
    def __str__(self):
        return self.get_descripcion_display()


class SGM_P_Metodo_Pago(models.Model):
    """Modelo para métodos de pago"""
    METODOS = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta de Crédito/Débito'),
        ('TRANSFERENCIA', 'Transferencia Bancaria'),
        ('CHEQUE', 'Cheque'),
    ]
    
    descripcion = models.CharField(max_length=50, choices=METODOS, unique=True)
    
    class Meta:
        verbose_name = "Método de Pago"
        verbose_name_plural = "Métodos de Pago"
        db_table = "SGM_P_Metodo_Pago"
    
    def __str__(self):
        return self.get_descripcion_display()


class SGM_P_Tipo_Evaluacion(models.Model):
    """Modelo para tipos de evaluación"""
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Tipo de Evaluación"
        verbose_name_plural = "Tipos de Evaluación"
        db_table = "SGM_P_Tipo_Evaluacion"
    
    def __str__(self):
        return self.nombre


class SGM_P_Jornada(models.Model):
    """Modelo para jornadas"""
    JORNADAS = [
        ('INTENSO', 'Intenso'),
        ('NORMAL', 'Normal'),
        ('FIN_DE_SEMANA', 'Fin de Semana'),
    ]
    
    nombre = models.CharField(max_length=50, choices=JORNADAS, unique=True)
    
    class Meta:
        verbose_name = "Jornada"
        verbose_name_plural = "Jornadas"
        db_table = "SGM_P_Jornada"
    
    def __str__(self):
        return self.get_nombre_display()


class SGM_P_Paralelo(models.Model):
    """Modelo para paralelos"""
    nombre = models.CharField(max_length=10)  # A, B, C, etc.
    id_jornada = models.ForeignKey(SGM_P_Jornada, on_delete=models.CASCADE, related_name='paralelos')
    
    class Meta:
        verbose_name = "Paralelo"
        verbose_name_plural = "Paralelos"
        db_table = "SGM_P_Paralelo"
        unique_together = ('nombre', 'id_jornada')
    
    def __str__(self):
        return f"{self.nombre} - {self.id_jornada.nombre}"


class SGM_P_Tipo_Asignatura(models.Model):
    """Modelo para tipos de asignatura"""
    TIPOS = [
        ('OBLIGATORIA', 'Obligatoria'),
        ('OPTATIVA', 'Optativa'),
        ('ELECTIVA', 'Electiva'),
    ]
    
    descripcion = models.CharField(max_length=50, choices=TIPOS, unique=True)
    
    class Meta:
        verbose_name = "Tipo de Asignatura"
        verbose_name_plural = "Tipos de Asignatura"
        db_table = "SGM_P_Tipo_Asignatura"
    
    def __str__(self):
        return self.get_descripcion_display()


class SGM_P_Tipo_Aula(models.Model):
    """Modelo para tipos de aula"""
    TIPOS = [
        ('TEORICA', 'Teórica'),
        ('LABORATORIO', 'Laboratorio'),
        ('TALLER', 'Taller'),
        ('AUDITORIO', 'Auditorio'),
    ]
    
    descripcion = models.CharField(max_length=50, choices=TIPOS, unique=True)
    
    class Meta:
        verbose_name = "Tipo de Aula"
        verbose_name_plural = "Tipos de Aula"
        db_table = "SGM_P_Tipo_Aula"
    
    def __str__(self):
        return self.get_descripcion_display()


class SGM_P_Edificio(models.Model):
    """Modelo para edificios"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, blank=True)
    ubicacion = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Edificio"
        verbose_name_plural = "Edificios"
        db_table = "SGM_P_Edificio"
    
    def __str__(self):
        return self.nombre


class SGM_P_Turno(models.Model):
    """Modelo para turnos"""
    TURNOS = [
        ('MATUTINO', 'Matutino'),
        ('VESPERTINO', 'Vespertino'),
        ('NOCTURNO', 'Nocturno'),
    ]
    
    nombre = models.CharField(max_length=50, choices=TURNOS, unique=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
        db_table = "SGM_P_Turno"
    
    def __str__(self):
        return f"{self.get_nombre_display()} ({self.hora_inicio} - {self.hora_fin})"


class SGM_P_Titulo(models.Model):
    """Modelo para títulos académicos"""
    descropcion = models.CharField(max_length=200, unique=True)  # Mantengo el typo del esquema original
    
    class Meta:
        verbose_name = "Título"
        verbose_name_plural = "Títulos"
        db_table = "SGM_P_Titulo"
    
    def __str__(self):
        return self.descropcion


class SGM_P_Asignatura(models.Model):
    """Modelo para asignaturas - CON RECURSIVIDAD"""
    NIVELES = [
        ('1', 'Primer Nivel'),
        ('2', 'Segundo Nivel'),
        ('3', 'Tercer Nivel'),
        ('4', 'Cuarto Nivel'),
        ('5', 'Quinto Nivel'),
        ('6', 'Sexto Nivel'),
        ('7', 'Séptimo Nivel'),
        ('8', 'Octavo Nivel'),
        ('9', 'Noveno Nivel'),
        ('10', 'Décimo Nivel'),
    ]
    
    nombre = models.CharField(max_length=200)
    horas_semanales = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    creditos = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    nivel = models.CharField(max_length=2, choices=NIVELES)
    id_tipo = models.ForeignKey(SGM_P_Tipo_Asignatura, on_delete=models.CASCADE, related_name='asignaturas')
    
    # RECURSIVIDAD: Asignatura prerrequisito
    id_asignatura_aprobada = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='asignaturas_dependientes',
        help_text="Asignatura que debe ser aprobada antes de cursar esta"
    )
    
    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        db_table = "SGM_P_Asignatura"
        unique_together = ('nombre', 'nivel')
    
    def __str__(self):
        return f"{self.nombre} - Nivel {self.nivel}"
    
    def get_prerrequisitos_completos(self):
        """Obtiene todos los prerrequisitos en cadena"""
        prerrequisitos = []
        asignatura_actual = self.id_asignatura_aprobada
        
        while asignatura_actual:
            prerrequisitos.append(asignatura_actual)
            asignatura_actual = asignatura_actual.id_asignatura_aprobada
        
        return prerrequisitos
    def puede_inscribirse(estudiante, asignatura):
        prerrequisitos = asignatura.get_prerrequisitos_completos()
        
        aprobadas = SGM_T_Matricula.objects.filter(
            estudiante=estudiante,
            asignatura__in=prerrequisitos,
            estado='Aprobado'
        ).values_list('asignatura', flat=True)
        
        return len(aprobadas) == len(prerrequisitos)


class SGM_P_Carrera_Modalidad(models.Model):
    """Modelo para la relación muchos a muchos entre Carrera y Modalidad"""
    id_carrera = models.ForeignKey('SGM_M_Carrera', on_delete=models.CASCADE, related_name='modalidades')
    id_modalidad = models.ForeignKey(SGM_P_Modalidad, on_delete=models.CASCADE, related_name='carreras')
    
    class Meta:
        verbose_name = "Carrera-Modalidad"
        verbose_name_plural = "Carreras-Modalidades"
        db_table = "SGM_P_Carrera_Modalidad"
        unique_together = ('id_carrera', 'id_modalidad')
    
    def __str__(self):
        return f"{self.id_carrera.nombre} - {self.id_modalidad.nombre}"


class SGM_P_Calificacion(models.Model):
    """Modelo para calificaciones"""
    id_oferta = models.ForeignKey('SGM_T_Oferta_Curso_Periodo', on_delete=models.CASCADE, related_name='calificaciones')
    id_tipo_evaluacion = models.ForeignKey(SGM_P_Tipo_Evaluacion, on_delete=models.CASCADE, related_name='calificaciones')
    nota = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    fecha = models.DateField()
    
    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
        db_table = "SGM_P_Calificacion"
        unique_together = ('id_oferta', 'id_tipo_evaluacion')
    
    def __str__(self):
        return f"{self.id_oferta.id_curso.nombre} - {self.nota}"
    
    @property
    def estado_nota(self):
        """Determina si la nota es aprobatoria"""
        return "APROBADO" if self.nota >= 7.0 else "REPROBADO"


# ============================================================================
# MODELOS MAESTROS (Entidades principales)
# ============================================================================

class SGM_M_Carrera(models.Model):
    """Modelo para carreras"""
    ESTADOS = [
        ('ACTIVA', 'Activa'),
        ('INACTIVA', 'Inactiva'),
        ('SUSPENDIDA', 'Suspendida'),
    ]
    
    nombre = models.CharField(max_length=200, unique=True)
    modalidad = models.CharField(max_length=50, blank=True)  # Mantengo del esquema original
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVA')
    semestres = models.CharField(max_length=10)  # "8", "10", etc.
    id_campo = models.ForeignKey(SGM_P_Campo_Estudio, on_delete=models.CASCADE, related_name='carreras')
    
    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        db_table = "SGM_M_Carrera"
    
    def __str__(self):
        return self.nombre


class SGM_M_Estudiante(models.Model):
    """Modelo para estudiantes"""
    GENEROS = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENEROS)
    celular = models.CharField(max_length=15, blank=True)
    correo = models.EmailField(unique=True)
    id_ciudad = models.ForeignKey(SGM_P_Ciudad, on_delete=models.CASCADE, related_name='estudiantes')
    direccion = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        db_table = "SGM_M_Estudiante"
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class SGM_M_Docente(models.Model):
    """Modelo para docentes"""
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    celular = models.CharField(max_length=15, blank=True)
    id_titulo = models.ForeignKey(SGM_P_Titulo, on_delete=models.CASCADE, related_name='docentes')
    id_ciudad = models.ForeignKey(SGM_P_Ciudad, on_delete=models.CASCADE, related_name='docentes')
    fecha_ingreso = models.DateField()
    direccion = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"
        db_table = "SGM_M_Docente"
    
    def __str__(self):
        return self.nombre


class SGM_M_Aula(models.Model):
    """Modelo para aulas"""
    capacidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    numero_aula = models.CharField(max_length=20)
    id_tipo_aula = models.ForeignKey(SGM_P_Tipo_Aula, on_delete=models.CASCADE, related_name='aulas')
    id_edificio = models.ForeignKey(SGM_P_Edificio, on_delete=models.CASCADE, related_name='aulas')
    
    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"
        db_table = "SGM_M_Aula"
        unique_together = ('numero_aula', 'id_edificio')
    
    def __str__(self):
        return f"{self.id_edificio.nombre} - {self.numero_aula}"


class SGM_M_Horario(models.Model):
    """Modelo para horarios"""
    DIAS = [
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIERCOLES', 'Miércoles'),
        ('JUEVES', 'Jueves'),
        ('VIERNES', 'Viernes'),
        ('SABADO', 'Sábado'),
        ('DOMINGO', 'Domingo'),
    ]
    
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    dia = models.CharField(max_length=10, choices=DIAS)
    id_turno = models.ForeignKey(SGM_P_Turno, on_delete=models.CASCADE, related_name='horarios')
    
    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"
        db_table = "SGM_M_Horario"
    
    def __str__(self):
        return f"{self.get_dia_display()} {self.hora_inicio} - {self.hora_fin}"


class SGM_M_Curso(models.Model):
    """Modelo para cursos"""
    nombre = models.CharField(max_length=200)
    id_asignatura = models.ForeignKey(SGM_P_Asignatura, on_delete=models.CASCADE, related_name='cursos')
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        db_table = "SGM_M_Curso"
    
    def __str__(self):
        return self.nombre


class SGM_M_Detalle_Matricula(models.Model):
    """Modelo para detalles de matrícula (cursos matriculados)"""
    id_matricula = models.ForeignKey('SGM_T_Matricula', on_delete=models.CASCADE, related_name='detalles')
    id_oferta = models.ForeignKey('SGM_T_Oferta_Curso_Periodo', on_delete=models.CASCADE, related_name='detalles_matricula')
    
    class Meta:
        verbose_name = "Detalle de Matrícula"
        verbose_name_plural = "Detalles de Matrícula"
        db_table = "SGM_M_Detalle_Matricula"
        unique_together = ('id_matricula', 'id_oferta')
    
    def __str__(self):
        return f"{self.id_matricula.id_estudiante.nombre_completo} - {self.id_oferta.id_curso.nombre}"


# ============================================================================
# MODELOS TRANSACCIONALES (Operaciones)
# ============================================================================

class SGM_T_Matricula(models.Model):
    """Modelo para matrículas"""
    id_estudiante = models.ForeignKey(SGM_M_Estudiante, on_delete=models.CASCADE, related_name='matriculas')
    id_modalidad_carrera = models.ForeignKey(SGM_P_Carrera_Modalidad, on_delete=models.CASCADE, related_name='matriculas')
    id_periodo = models.ForeignKey(SGM_P_Periodo_Academico, on_delete=models.CASCADE, related_name='matriculas')
    id_estado = models.ForeignKey(SGM_P_Estado_Matricula, on_delete=models.CASCADE, related_name='matriculas')
    fecha_matricula = models.DateField()
    
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        db_table = "SGM_T_Matricula"
        unique_together = ('id_estudiante', 'id_modalidad_carrera', 'id_periodo')
    
    def __str__(self):
        return f"{self.id_estudiante.nombre_completo} - {self.id_modalidad_carrera}"


class SGM_T_Pago(models.Model):
    """Modelo para pagos"""
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADO', 'Pagado'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    id_matricula = models.ForeignKey(SGM_T_Matricula, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    id_metodo = models.ForeignKey(SGM_P_Metodo_Pago, on_delete=models.CASCADE, related_name='pagos')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        db_table = "SGM_T_Pago"
    
    def __str__(self):
        return f"Pago {self.id} - {self.id_matricula.id_estudiante.nombre_completo}"


class SGM_T_Oferta_Curso_Periodo(models.Model):
    """Modelo para ofertas de cursos por período"""
    ESTADOS = [
        ('ACTIVA', 'Activa'),
        ('INACTIVA', 'Inactiva'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    id_curso = models.ForeignKey(SGM_M_Curso, on_delete=models.CASCADE, related_name='ofertas')
    id_periodo = models.ForeignKey(SGM_P_Periodo_Academico, on_delete=models.CASCADE, related_name='ofertas')
    id_docente = models.ForeignKey(SGM_M_Docente, on_delete=models.CASCADE, related_name='ofertas')
    id_paralelo = models.ForeignKey(SGM_P_Paralelo, on_delete=models.CASCADE, related_name='ofertas')
    cupos_max = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVA')
    
    class Meta:
        verbose_name = "Oferta de Curso"
        verbose_name_plural = "Ofertas de Cursos"
        db_table = "SGM_T_Oferta_Curso_Periodo"
        unique_together = ('id_curso', 'id_periodo', 'id_paralelo')
    
    def __str__(self):
        return f"{self.id_curso.nombre} - {self.id_periodo.nombre} - {self.id_paralelo}"
    
    @property
    def cupos_disponibles(self):
        """Calcula cupos disponibles"""
        matriculados = self.detalles_matricula.count()
        return self.cupos_max - matriculados


class SGM_T_Curso_Horario(models.Model):
    """Modelo para horarios de cursos"""
    id_oferta = models.ForeignKey(SGM_T_Oferta_Curso_Periodo, on_delete=models.CASCADE, related_name='horarios')
    id_horario = models.ForeignKey(SGM_M_Horario, on_delete=models.CASCADE, related_name='cursos')
    id_aula = models.ForeignKey(SGM_M_Aula, on_delete=models.CASCADE, related_name='horarios_curso')
    
    class Meta:
        verbose_name = "Curso-Horario"
        verbose_name_plural = "Cursos-Horarios"
        db_table = "SGM_T_Curso_Horario"
        unique_together = ('id_oferta', 'id_horario', 'id_aula')
    
    def __str__(self):
        return f"{self.id_oferta.id_curso.nombre} - {self.id_horario} - {self.id_aula}"