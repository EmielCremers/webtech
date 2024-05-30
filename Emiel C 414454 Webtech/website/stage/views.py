from flask import Blueprint, render_template, redirect, url_for
from website import db
from website.stage.forms import VoegtoeForm, VerwijderForm
from website.models import Stage

# Definiëren van stages blueprint met de bijbehorende URL-prefix en template folder
stages_blueprint = Blueprint('stages',
                             __name__,
                             template_folder='templates/stages')

# Route voor het toevoegen van een stage
@stages_blueprint.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeForm()

    if form.validate_on_submit():
        periode = form.periode.data
        cijfer = form.cijfer.data
        naam = form.naam.data

        n_stage = Stage(periode, cijfer, naam)
        db.session.add(n_stage)
        db.session.commit()
        return redirect(url_for('stages.lijst')) # Doorverwijzen naar de lijst met stages na toevoegen van stage
    
    return render_template('toevoegen.html', form=form)

# Route voor het weergeven van de lijst met stages
@stages_blueprint.route('lijst')
def lijst():
    stages = Stage.query.all()
    return render_template('lijst.html', stages=stages)

# Route voor het verwijderen van een stage
@stages_blueprint.route('/verwijderen', methods=['GET', 'POST'])
def verwijderen():
    form = VerwijderForm()
    
    if form.validate_on_submit():
        id = form.id.data
        stag = Stage.query.get(id)
        db.session.delete(stag)
        db.session.commit()

        return redirect(url_for('stages.lijst')) # Doorverwijzen naar de lijst met stages na verwijderen van stage
    
    return render_template('verwijderen.html', form=form)