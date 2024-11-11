import pytest
from datetime import datetime, timedelta
from app import create_app, db
from app.models import Pacientes, Citas, Medicos, Consultorios

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": 'postgresql://darwin:password@localhost:5432/evaluacion'
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_fecha_nacimiento_valores_limites(app):
    with app.app_context():
        # Limpiar registros existentes
        db.session.query(Citas).delete()
        db.session.query(Pacientes).delete()
        db.session.commit()

        # CP01: Fecha mínima válida (90 años atrás desde hoy)
        fecha_min_valida = datetime.now().date() - timedelta(days=365*90)
        paciente_min = Pacientes(id=5, nombre='Test', apellido='Min', fecha_nacimiento=fecha_min_valida, email='test.min@example.com')
        db.session.add(paciente_min)
        db.session.commit()
        assert Pacientes.query.get(5) is not None

        # CP02: Fecha máxima válida (hoy)
        fecha_actual = datetime.now().date()
        paciente_max = Pacientes(id=6, nombre='Test', apellido='Max', fecha_nacimiento=fecha_actual, email='test.max@example.com')
        db.session.add(paciente_max)
        db.session.commit()
        assert Pacientes.query.get(6) is not None

        # CP03: Fecha fuera del límite inferior (más de 90 años atrás)
        fecha_fuera_limite_inf = datetime.now().date() - timedelta(days=365*91)
        paciente_fuera_inf = Pacientes(id=7, nombre='Test', apellido='FueraInf', fecha_nacimiento=fecha_fuera_limite_inf, email='test.fuerainf@example.com')
        db.session.add(paciente_fuera_inf)
        with pytest.raises(Exception):
            db.session.commit()
        db.session.rollback()

def test_hora_cita_valores_limites(app):
    with app.app_context():
        # Limpiar registros existentes
        db.session.query(Citas).delete()
        db.session.commit()

        # Eliminar y volver a insertar los registros referenciados en las tablas Pacientes, Médicos y Consultorios
        db.session.query(Pacientes).filter(Pacientes.id == 1).delete()
        db.session.query(Medicos).filter(Medicos.id == 1).delete()
        db.session.query(Consultorios).filter(Consultorios.id == 1).delete()
        db.session.commit()

        paciente = Pacientes(id=1, nombre='Paciente', apellido='Test', fecha_nacimiento='1980-01-01', email='paciente.test@example.com')
        medico = Medicos(id=1, nombre='Medico', apellido='Test', especialidad='General')
        consultorio = Consultorios(id=1, numero='101', piso=1)
        db.session.add(paciente)
        db.session.add(medico)
        db.session.add(consultorio)
        db.session.commit()

        # CP05: Hora mínima válida
        cita_min = Citas(paciente_id=1, medico_id=1, consultorio_id=1, fecha=datetime.now().date(), hora='08:00:00')
        db.session.add(cita_min)
        db.session.commit()
        assert Citas.query.filter_by(hora='08:00:00').first() is not None

        # CP06: Hora máxima válida
        cita_max = Citas(paciente_id=1, medico_id=1, consultorio_id=1, fecha=datetime.now().date(), hora='17:00:00')
        db.session.add(cita_max)
        db.session.commit()
        assert Citas.query.filter_by(hora='17:00:00').first() is not None

        # CP07: Hora fuera del límite inferior
        cita_fuera_inf = Citas(paciente_id=1, medico_id=1, consultorio_id=1, fecha=datetime.now().date(), hora='07:59:00')
        db.session.add(cita_fuera_inf)
        with pytest.raises(Exception):
            db.session.commit()
        db.session.rollback()

        # CP08: Hora fuera del límite superior
        cita_fuera_sup = Citas(paciente_id=1, medico_id=1, consultorio_id=1, fecha=datetime.now().date(), hora='17:01:00')
        db.session.add(cita_fuera_sup)
        with pytest.raises(Exception):
            db.session.commit()
        db.session.rollback()
