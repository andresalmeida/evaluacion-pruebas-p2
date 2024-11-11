import pytest
from app import create_app, db
from app.models import Pacientes, Medicos, Citas, Consultorios

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_insert_records(app):
    with app.app_context():
        nuevo_paciente = Pacientes(id=4, nombre='Laura', apellido='Gonzalez', fecha_nacimiento='1989-12-10', email='laura.gonzalez@example.com')
        nuevo_medico = Medicos(id=4, nombre='Ana', apellido='Gomez', especialidad='Neurología')
        nuevo_consultorio = Consultorios(id=4, numero='404', piso=4)
        nueva_cita = Citas(paciente_id=4, medico_id=4, consultorio_id=4, fecha='2024-07-20', hora='10:00:00')

        db.session.add(nuevo_paciente)
        db.session.add(nuevo_medico)
        db.session.add(nuevo_consultorio)
        db.session.add(nueva_cita)
        db.session.commit()

        cita = Citas.query.filter_by(paciente_id=4, medico_id=4, consultorio_id=4).first()
        assert cita is not None

def test_update_record(app):
    with app.app_context():
        paciente = Pacientes.query.get(1)
        if paciente is None:
            paciente = Pacientes(id=1, nombre='Juan', apellido='Perez', fecha_nacimiento='1980-01-01', email='juan.perez@example.com')
            db.session.add(paciente)
            db.session.commit()

        paciente.nombre = 'Carlos'
        db.session.commit()

        updated_paciente = Pacientes.query.get(1)
        assert updated_paciente.nombre == 'Carlos'

def test_delete_record(app):
    with app.app_context():
        paciente = Pacientes.query.get(3)
        if paciente is None:
            paciente = Pacientes(id=3, nombre='Paola', apellido='Ramirez', fecha_nacimiento='1992-11-30', email='paola.ramirez@example.com')
            db.session.add(paciente)
            db.session.commit()

        db.session.delete(paciente)
        db.session.commit()

        deleted_paciente = Pacientes.query.get(3)
        assert deleted_paciente is None
