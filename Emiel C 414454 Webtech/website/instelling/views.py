from flask import Blueprint, render_template, redirect, url_for
from website import db
from website.models import Instelling
from website.instelling.forms import VoegtoeInstelling

# Definiëren van de instellingen blueprint met de bijbehorende URL-prefix en template-folder
instellingen_blueprint = Blueprint('instellingen',
                                   __name__,
                                   template_folder="templates/instellingen")

# Route voor het toevoegen van een instelling
@instellingen_blueprint.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeInstelling()

    if form.validate_on_submit():
        naam = form.naam.data
        soort = form.soort.data
        id = form.id.data
        
        # Controleren of de instelling al bestaat op basis van ID
        existing_instelling = Instelling.query.filter_by(id=id).first()
        if existing_instelling:
            existing_instelling.naam = naam  # Naam bijwerken als de instelling al bestaat
            existing_instelling.soort = soort  # Soort bijwerken als de instelling al bestaat
        else:
            new_instelling = Instelling(naam=naam, soort=soort, stage_id=id)
            db.session.add(new_instelling)
        
        db.session.commit()
        return redirect(url_for('stages.lijst')) # Doorverwijzen naar de lijst met stages na toevoegen van instelling
    
    return render_template('instelling_toevoegen.html', form=form)
