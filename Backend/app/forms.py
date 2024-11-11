from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime, timedelta

class CitaForm(FlaskForm):
    paciente_id = IntegerField('ID del Paciente', validators=[DataRequired()])
    medico_id = IntegerField('ID del Médico', validators=[DataRequired()])
    consultorio_id = IntegerField('ID del Consultorio', validators=[DataRequired()])
    fecha = DateField('Fecha', validators=[DataRequired()])
    hora = TimeField('Hora', validators=[DataRequired()])
    submit = SubmitField('Crear Cita')

    def validate_fecha(form, field):
        if field.data < datetime.now().date():
            raise ValidationError("La fecha de la cita no puede ser anterior a la fecha actual.")

    def validate_hora(form, field):
        if field.data < datetime.strptime("08:00:00", "%H:%M:%S").time() or field.data > datetime.strptime("17:00:00", "%H:%M:%S").time():
            raise ValidationError("La hora de la cita debe estar entre las 08:00 AM y las 05:00 PM.")

class PacienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Registrar Paciente')

    def validate_fecha_nacimiento(form, field):
        if field.data > datetime.now().date():
            raise ValidationError("La fecha de nacimiento no puede ser en el futuro.")
        if field.data < datetime.now().date() - timedelta(days=365*90):
            raise ValidationError("La persona no puede tener más de 90 años.")
