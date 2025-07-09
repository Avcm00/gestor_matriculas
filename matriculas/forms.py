from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import (
    SGM_M_Detalle_Matricula,
    SGM_M_Horario,
    SGM_P_Calificacion,
    SGM_P_Campo_Estudio,
    SGM_P_Ciudad,
    SGM_P_Division_Politica,
    SGM_M_Estudiante,
    SGM_P_Jornada,
    SGM_P_Pais,
    SGM_P_Periodo_Academico,
    SGM_P_Estado_Matricula,
    SGM_M_Carrera,
    SGM_P_Modalidad,
    SGM_P_Tipo_Evaluacion,
    SGM_P_Turno,
    SGM_T_Curso_Horario,
    SGM_T_Matricula,
    SGM_P_Metodo_Pago,
    SGM_T_Pago,
    SGM_M_Docente,
    SGM_M_Aula,
    SGM_P_Asignatura,
    SGM_M_Curso,
    SGM_T_Oferta_Curso_Periodo,
    SGM_P_Titulo,
    SGM_P_Tipo_Aula,
    SGM_P_Edificio,
    SGM_P_Tipo_Asignatura,
    SGM_P_Paralelo,
    SGM_P_Carrera_Modalidad,
)

# Clase base para aplicar estilos Bootstrap consistentes
class BaseModelForm(forms.ModelForm):
    """Clase base para aplicar estilos Bootstrap a todos los formularios"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Aplicar clases Bootstrap a todos los campos
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.widgets.Input):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label
                })
            elif isinstance(field.widget, forms.widgets.Select):
                field.widget.attrs.update({
                    'class': 'form-select'
                })
            elif isinstance(field.widget, forms.widgets.Textarea):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': field.label
                })
            elif isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs.update({
                    'class': 'form-check-input'
                })
            elif isinstance(field.widget, forms.widgets.DateInput):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'type': 'date'
                })
            elif isinstance(field.widget, forms.widgets.TimeInput):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'type': 'time'
                })
            elif isinstance(field.widget, forms.widgets.EmailInput):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'type': 'email',
                    'placeholder': 'ejemplo@correo.com'
                })


# ——— Formularios de Configuración Base ———
class PaisForm(BaseModelForm):
    class Meta:
        model = SGM_P_Pais
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre del País'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre del país',
                'maxlength': 100
            })
        }


class DivisionPoliticaForm(BaseModelForm):
    class Meta:
        model = SGM_P_Division_Politica
        fields = ['nombre', 'id_pais']
        labels = {
            'nombre': 'Nombre de la División Política',
            'id_pais': 'País'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Guayas, Pichincha, etc.',
                'maxlength': 100
            }),
            'id_pais': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class CiudadForm(BaseModelForm):
    class Meta:
        model = SGM_P_Ciudad
        fields = ['nombre', 'id_division']
        labels = {
            'nombre': 'Nombre de la Ciudad',
            'id_division': 'División Política'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Guayaquil, Quito, etc.',
                'maxlength': 100
            }),
            'id_division': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class CampoEstudioForm(BaseModelForm):
    class Meta:
        model = SGM_P_Campo_Estudio
        fields = ['nombre']
        labels = {
            'nombre': 'Campo de Estudio'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Ingeniería, Medicina, Educación, etc.',
                'maxlength': 100
            })
        }


class ModalidadForm(BaseModelForm):
    class Meta:
        model = SGM_P_Modalidad
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Modalidad',
            'descripcion': 'Descripción'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Presencial, Virtual, Semipresencial',
                'maxlength': 50
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Descripción detallada de la modalidad...',
                'rows': 3
            })
        }


class PeriodoAcademicoForm(BaseModelForm):
    class Meta:
        model = SGM_P_Periodo_Academico
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'inicio_matricula', 'fin_matricula']
        labels = {
            'nombre': 'Nombre del Período',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_fin': 'Fecha de Fin',
            'inicio_matricula': 'Inicio de Matrícula',
            'fin_matricula': 'Fin de Matrícula'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: 2024-1, Marzo-Agosto 2024, etc.',
                'maxlength': 50
            }),
            'fecha_inicio': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'fecha_fin': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'inicio_matricula': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'fin_matricula': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        inicio_matricula = cleaned_data.get('inicio_matricula')
        fin_matricula = cleaned_data.get('fin_matricula')

        if fecha_inicio and fecha_fin:
            if fecha_inicio >= fecha_fin:
                raise ValidationError("La fecha de inicio debe ser anterior a la fecha de fin del período.")

        if inicio_matricula and fin_matricula:
            if inicio_matricula >= fin_matricula:
                raise ValidationError("La fecha de inicio de matrícula debe ser anterior a la fecha de fin.")

        return cleaned_data


class EstadoMatriculaForm(BaseModelForm):
    class Meta:
        model = SGM_P_Estado_Matricula
        fields = ['descripcion']
        labels = {
            'descripcion': 'Estado de Matrícula'
        }
        widgets = {
            'descripcion': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class MetodoPagoForm(BaseModelForm):
    class Meta:
        model = SGM_P_Metodo_Pago
        fields = ['descripcion']
        labels = {
            'descripcion': 'Método de Pago'
        }
        widgets = {
            'descripcion': forms.Select(attrs={
                'class': 'form-select'
            })
        }


# ——— Formularios de Entidades Principales ———
class CarreraForm(BaseModelForm):
    class Meta:
        model = SGM_M_Carrera
        fields = ['nombre', 'descripcion', 'estado', 'semestres', 'id_campo']
        labels = {
            'nombre': 'Nombre de la Carrera',
            'descripcion': 'Descripción',
            'estado': 'Estado',
            'semestres': 'Número de Semestres',
            'id_campo': 'Campo de Estudio'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Ingeniería en Sistemas, Medicina, etc.',
                'maxlength': 200
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Descripción detallada de la carrera...',
                'rows': 4
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'semestres': forms.TextInput(attrs={
                'placeholder': 'Ej: 8, 10, 12',
                'maxlength': 10
            }),
            'id_campo': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class EstudianteForm(BaseModelForm):
    class Meta:
        model = SGM_M_Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'fecha_nacimiento', 'genero', 'celular', 'correo', 'id_ciudad', 'direccion']
        labels = {
            'nombre': 'Nombres',
            'apellido': 'Apellidos',
            'cedula': 'Cédula de Identidad',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'genero': 'Género',
            'celular': 'Teléfono Celular',
            'correo': 'Correo Electrónico',
            'id_ciudad': 'Ciudad',
            'direccion': 'Dirección'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombres del estudiante',
                'maxlength': 100
            }),
            'apellido': forms.TextInput(attrs={
                'placeholder': 'Apellidos del estudiante',
                'maxlength': 100
            }),
            'cedula': forms.TextInput(attrs={
                'placeholder': 'Número de cédula',
                'maxlength': 20,
                'pattern': '[0-9]{10}'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'genero': forms.Select(attrs={
                'class': 'form-select'
            }),
            'celular': forms.TextInput(attrs={
                'placeholder': 'Ej: 0999999999',
                'maxlength': 15,
                'pattern': '[0-9]{10}'
            }),
            'correo': forms.EmailInput(attrs={
                'placeholder': 'estudiante@ejemplo.com',
                'class': 'form-control'
            }),
            'id_ciudad': forms.Select(attrs={
                'class': 'form-select'
            }),
            'direccion': forms.TextInput(attrs={
                'placeholder': 'Dirección completa del estudiante',
                'maxlength': 200
            })
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if 'estudiante' in self.initial:
                self.fields['estudiante'].widget = forms.HiddenInput()

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if cedula and len(cedula) != 10:
            raise ValidationError("La cédula debe tener 10 dígitos.")
        return cedula

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha:
            today = timezone.now().date()
            age = today.year - fecha.year - ((today.month, today.day) < (fecha.month, fecha.day))
            if age < 16:
                raise ValidationError("El estudiante debe tener al menos 16 años.")
            if age > 80:
                raise ValidationError("Por favor, verifique la fecha de nacimiento.")
        return fecha


class DocenteForm(BaseModelForm):
    class Meta:
        model = SGM_M_Docente
        fields = ['nombre', 'correo', 'celular', 'id_titulo', 'id_ciudad', 'fecha_ingreso', 'direccion']
        labels = {
            'nombre': 'Nombre Completo',
            'correo': 'Correo Electrónico',
            'celular': 'Teléfono Celular',
            'id_titulo': 'Título Académico',
            'id_ciudad': 'Ciudad',
            'fecha_ingreso': 'Fecha de Ingreso',
            'direccion': 'Dirección'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre completo del docente',
                'maxlength': 100
            }),
            'correo': forms.EmailInput(attrs={
                'placeholder': 'docente@ejemplo.com',
                'class': 'form-control'
            }),
            'celular': forms.TextInput(attrs={
                'placeholder': 'Ej: 0999999999',
                'maxlength': 15
            }),
            'id_titulo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_ciudad': forms.Select(attrs={
                'class': 'form-select'
            }),
            'fecha_ingreso': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'direccion': forms.TextInput(attrs={
                'placeholder': 'Dirección completa del docente',
                'maxlength': 200
            })
        }


class AulaForm(BaseModelForm):
    class Meta:
        model = SGM_M_Aula
        fields = ['capacidad', 'numero_aula', 'id_tipo_aula', 'id_edificio']
        labels = {
            'capacidad': 'Capacidad',
            'numero_aula': 'Número de Aula',
            'id_tipo_aula': 'Tipo de Aula',
            'id_edificio': 'Edificio'
        }
        widgets = {
            'capacidad': forms.NumberInput(attrs={
                'placeholder': 'Número de estudiantes',
                'min': 1,
                'max': 500
            }),
            'numero_aula': forms.TextInput(attrs={
                'placeholder': 'Ej: 101, A-205, Lab-1',
                'maxlength': 20
            }),
            'id_tipo_aula': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_edificio': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class AsignaturaForm(BaseModelForm):
    class Meta:
        model = SGM_P_Asignatura
        fields = ['nombre', 'horas_semanales', 'creditos', 'nivel', 'id_tipo', 'id_asignatura_aprobada']
        labels = {
            'nombre': 'Nombre de la Asignatura',
            'horas_semanales': 'Horas Semanales',
            'creditos': 'Créditos',
            'nivel': 'Nivel',
            'id_tipo': 'Tipo de Asignatura',
            'id_asignatura_aprobada': 'Asignatura Prerrequisito'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre de la asignatura',
                'maxlength': 200
            }),
            'horas_semanales': forms.NumberInput(attrs={
                'placeholder': 'Horas por semana',
                'min': 1,
                'max': 20
            }),
            'creditos': forms.NumberInput(attrs={
                'placeholder': 'Número de créditos',
                'min': 1,
                'max': 10
            }),
            'nivel': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_tipo': forms.Select(attrs={
                'class': 'form-select'}),
            'id_asignatura_aprobada': forms.Select(attrs={
                'class': 'form-select'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        id_asignatura_aprobada = cleaned_data.get('id_asignatura_aprobada')
        
        # Validar que no se asigne a sí misma como prerrequisito
        if id_asignatura_aprobada and hasattr(self, 'instance') and self.instance.pk:
            if id_asignatura_aprobada.pk == self.instance.pk:
                raise ValidationError("Una asignatura no puede ser prerrequisito de sí misma.")
        
        return cleaned_data





class HorarioForm(BaseModelForm):
    class Meta:
        model = SGM_M_Horario
        fields = ['hora_inicio', 'hora_fin', 'dia', 'id_turno']
        labels = {
            'hora_inicio': 'Hora de Inicio',
            'hora_fin': 'Hora de Fin',
            'dia': 'Día de la Semana',
            'id_turno': 'Turno'
        }
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'hora_fin': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'dia': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_turno': forms.Select(attrs={
                'class': 'form-select'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fin = cleaned_data.get('hora_fin')

        if hora_inicio and hora_fin:
            if hora_inicio >= hora_fin:
                raise ValidationError("La hora de inicio debe ser anterior a la hora de fin.")

        return cleaned_data


# ——— Formularios de Parámetros Adicionales ———
class TituloForm(BaseModelForm):
    class Meta:
        model = SGM_P_Titulo
        fields = ['descropcion']  # Mantengo el nombre original del campo
        labels = {
            'descropcion': 'Título Académico'
        }
        widgets = {
            'descropcion': forms.TextInput(attrs={
                'placeholder': 'Ej: Ingeniero en Sistemas, Licenciado en Educación, etc.',
                'maxlength': 200
            })
        }


class TipoAulaForm(BaseModelForm):
    class Meta:
        model = SGM_P_Tipo_Aula
        fields = ['descripcion']
        labels = {
            'descripcion': 'Tipo de Aula'
        }
        widgets = {
            'descripcion': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class EdificioForm(BaseModelForm):
    class Meta:
        model = SGM_P_Edificio
        fields = ['nombre', 'descripcion', 'ubicacion']
        labels = {
            'nombre': 'Nombre del Edificio',
            'descripcion': 'Descripción',
            'ubicacion': 'Ubicación'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre del edificio',
                'maxlength': 100
            }),
            'descripcion': forms.TextInput(attrs={
                'placeholder': 'Descripción breve del edificio',
                'maxlength': 200
            }),
            'ubicacion': forms.Textarea(attrs={
                'placeholder': 'Ubicación detallada del edificio...',
                'rows': 2
            })
        }


class TipoAsignaturaForm(BaseModelForm):
    class Meta:
        model = SGM_P_Tipo_Asignatura
        fields = ['descripcion']
        labels = {
            'descripcion': 'Tipo de Asignatura'
        }
        widgets = {
            'descripcion': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class ParaleloForm(BaseModelForm):
    class Meta:
        model = SGM_P_Paralelo
        fields = ['nombre', 'id_jornada']
        labels = {
            'nombre': 'Paralelo',
            'id_jornada': 'Jornada'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: A, B, C, D',
                'maxlength': 10
            }),
            'id_jornada': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class JornadaForm(BaseModelForm):
    class Meta:
        model = SGM_P_Jornada
        fields = ['nombre']
        labels = {
            'nombre': 'Jornada'
        }
        widgets = {
            'nombre': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class TurnoForm(BaseModelForm):
    class Meta:
        model = SGM_P_Turno
        fields = ['nombre', 'hora_inicio', 'hora_fin']
        labels = {
            'nombre': 'Turno',
            'hora_inicio': 'Hora de Inicio',
            'hora_fin': 'Hora de Fin'
        }
        widgets = {
            'nombre': forms.Select(attrs={
                'class': 'form-select'
            }),
            'hora_inicio': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'hora_fin': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fin = cleaned_data.get('hora_fin')

        if hora_inicio and hora_fin:
            if hora_inicio >= hora_fin:
                raise ValidationError("La hora de inicio debe ser anterior a la hora de fin.")

        return cleaned_data


class TipoEvaluacionForm(BaseModelForm):
    class Meta:
        model = SGM_P_Tipo_Evaluacion
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Tipo de Evaluación',
            'descripcion': 'Descripción'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Examen, Tarea, Proyecto, etc.',
                'maxlength': 50
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Descripción del tipo de evaluación...',
                'rows': 3
            })
        }


class CarreraModalidadForm(BaseModelForm):
    class Meta:
        model = SGM_P_Carrera_Modalidad
        fields = ['id_carrera', 'id_modalidad']
        labels = {
            'id_carrera': 'Carrera',
            'id_modalidad': 'Modalidad'
        }
        widgets = {
            'id_carrera': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_modalidad': forms.Select(attrs={
                'class': 'form-select'
            })
        }


# ——— Formularios Transaccionales ———
class MatriculaForm(BaseModelForm):
    class Meta:
        model = SGM_T_Matricula
        fields = ['id_estudiante', 'id_modalidad_carrera', 'id_periodo', 'id_estado', 'fecha_matricula']
        labels = {
            'id_estudiante': 'Estudiante',
            'id_modalidad_carrera': 'Carrera y Modalidad',
            'id_periodo': 'Período Académico',
            'id_estado': 'Estado de Matrícula',
            'fecha_matricula': 'Fecha de Matrícula'
        }
        widgets = {
            'id_estudiante': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_modalidad_carrera': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_periodo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'fecha_matricula': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }

    def clean_fecha_matricula(self):
        fecha = self.cleaned_data.get('fecha_matricula')
        if fecha:
            today = timezone.now().date()
            if fecha > today:
                raise ValidationError("La fecha de matrícula no puede ser futura.")
        return fecha


class PagoForm(BaseModelForm):
    class Meta:
        model = SGM_T_Pago
        fields = ['id_matricula', 'fecha_pago', 'monto', 'id_metodo', 'estado']
        labels = {
            'id_matricula': 'Matrícula',
            'fecha_pago': 'Fecha de Pago',
            'monto': 'Monto',
            'id_metodo': 'Método de Pago',
            'estado': 'Estado del Pago'
        }
        widgets = {
            'id_matricula': forms.Select(attrs={
                'class': 'form-select'
            }),
            'fecha_pago': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'monto': forms.NumberInput(attrs={
                'step': '0.01',
                'min': '0',
                'placeholder': '0.00'
            }),
            'id_metodo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            })
        }

    def clean_monto(self):
        monto = self.cleaned_data.get('monto')
        if monto and monto <= 0:
            raise ValidationError("El monto debe ser mayor a cero.")
        return monto
class OfertaCursoPeriodoForm(forms.ModelForm):
    class Meta:
        model = SGM_T_Oferta_Curso_Periodo
        fields = ['id_curso', 'id_periodo', 'id_docente', 'id_paralelo', 'cupos_max', 'estado']
        widgets = {
            'id_curso': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'id_periodo': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'id_docente': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'id_paralelo': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'cupos_max': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'estado': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
        }
class CursoForm(forms.ModelForm):
    class Meta:
        model = SGM_M_Curso
        fields = ['nombre', 'id_asignatura', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'id_asignatura': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'rows': 3}),
        }

class DetalleMatriculaForm(BaseModelForm):
    class Meta:
        model = SGM_M_Detalle_Matricula
        fields = ['id_matricula', 'id_oferta']
        labels = {
            'id_matricula': 'Matrícula',
            'id_oferta': 'Oferta de Curso'
        }
        widgets = {
            'id_matricula': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_oferta': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class CursoHorarioForm(BaseModelForm):
    class Meta:
        model = SGM_T_Curso_Horario
        fields = ['id_oferta', 'id_horario', 'id_aula']
        labels = {
            'id_oferta': 'Oferta de Curso',
            'id_horario': 'Horario',
            'id_aula': 'Aula'
        }
        widgets = {
            'id_oferta': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_horario': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_aula': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class CalificacionForm(BaseModelForm):
    class Meta:
        model = SGM_P_Calificacion
        fields = ['id_oferta', 'id_tipo_evaluacion', 'nota', 'fecha']
        labels = {
            'id_oferta': 'Oferta de Curso',
            'id_tipo_evaluacion': 'Tipo de Evaluación',
            'nota': 'Calificación',
            'fecha': 'Fecha'
        }
        widgets = {
            'id_oferta': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_tipo_evaluacion': forms.Select(attrs={
                'class': 'form-select'
            }),
            'nota': forms.NumberInput(attrs={
                'step': '0.01',
                'min': '0',
                'max': '10',
                'placeholder': '0.00'
            }),
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }

    def clean_nota(self):
        nota = self.cleaned_data.get('nota')
        if nota is not None:
            if nota < 0 or nota > 10:
                raise ValidationError("La calificación debe estar entre 0 y 10.")
        return nota


# ——— Formularios de Búsqueda y Filtros ———
class BusquedaEstudianteForm(forms.Form):
    """Formulario para búsqueda de estudiantes"""
    cedula = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Número de cédula'
        }),
        label='Cédula'
    )
    nombre = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre del estudiante'
        }),
        label='Nombre'
    )
    carrera = forms.ModelChoiceField(
        queryset=SGM_M_Carrera.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Carrera'
    )


class FiltroMatriculaForm(forms.Form):
    """Formulario para filtrar matrículas"""
    periodo = forms.ModelChoiceField(
        queryset=SGM_P_Periodo_Academico.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Período'
    )
    estado = forms.ModelChoiceField(
        queryset=SGM_P_Estado_Matricula.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Estado'
    )
    carrera = forms.ModelChoiceField(
        queryset=SGM_M_Carrera.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Carrera'
    )


class ReporteNotasForm(forms.Form):
    """Formulario para generar reportes de notas"""
    periodo = forms.ModelChoiceField(
        queryset=SGM_P_Periodo_Academico.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Período'
    )
    curso = forms.ModelChoiceField(
        queryset=SGM_M_Curso.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Curso'
    )
    paralelo = forms.ModelChoiceField(
        queryset=SGM_P_Paralelo.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        label='Paralelo'
    )