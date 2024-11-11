from app import db

class Pacientes(db.Model):
    __tablename__ = 'pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), nullable=False)

class Medicos(db.Model):
    __tablename__ = 'medicos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)

class Consultorios(db.Model):
    __tablename__ = 'consultorios'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), nullable=False)
    piso = db.Column(db.Integer, nullable=False)

class Citas(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    consultorio_id = db.Column(db.Integer, db.ForeignKey('consultorios.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)

    paciente = db.relationship('Pacientes', backref=db.backref('citas', lazy=True))
    medico = db.relationship('Medicos', backref=db.backref('citas', lazy=True))
    consultorio = db.relationship('Consultorios', backref=db.backref('citas', lazy=True))
