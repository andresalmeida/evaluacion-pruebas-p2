from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.forms import CitaForm
from app.models import Citas, db

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/citas')
def obtener_citas():
    citas = Citas.query.all()
    return render_template('citas.html', citas=citas)

@bp.route('/citas/nueva', methods=['GET', 'POST'])
def nueva_cita():
    form = CitaForm()
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            nueva_cita = Citas(
                paciente_id=data['paciente_id'],
                medico_id=data['medico_id'],
                consultorio_id=data['consultorio_id'],
                fecha=data['fecha'],
                hora=data['hora']
            )
        else:
            nueva_cita = Citas(
                paciente_id=form.paciente_id.data,
                medico_id=form.medico_id.data,
                consultorio_id=form.consultorio_id.data,
                fecha=form.fecha.data,
                hora=form.hora.data
            )
        try:
            db.session.add(nueva_cita)
            db.session.commit()
            flash('Cita creada exitosamente', 'success')
            return redirect(url_for('main.obtener_citas'))
        except Exception as e:
            db.session.rollback()
            flash('Error al crear la cita: {}'.format(e), 'danger')
    return render_template('citas_form.html', form=form)


@bp.route('/citas/editar/<int:id>', methods=['GET', 'POST'])
def editar_cita(id):
    cita = Citas.query.get_or_404(id)
    form = CitaForm(obj=cita)
    if form.validate_on_submit():
        cita.paciente_id = form.paciente_id.data
        cita.medico_id = form.medico_id.data
        cita.consultorio_id = form.consultorio_id.data
        cita.fecha = form.fecha.data
        cita.hora = form.hora.data
        try:
            db.session.commit()
            flash('Cita actualizada exitosamente', 'success')
            return redirect(url_for('main.obtener_citas'))
        except Exception as e:
            db.session.rollback()
            flash('Error al actualizar la cita: {}'.format(e), 'danger')
    return render_template('citas_form.html', form=form)

@bp.route('/citas/eliminar/<int:id>', methods=['POST'])
def eliminar_cita(id):
    cita = Citas.query.get_or_404(id)
    try:
        db.session.delete(cita)
        db.session.commit()
        flash('Cita eliminada exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al eliminar la cita: {}'.format(e), 'danger')
    return redirect(url_for('main.obtener_citas'))
