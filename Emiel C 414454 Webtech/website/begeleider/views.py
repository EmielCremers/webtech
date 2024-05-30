from flask import Blueprint, render_template, redirect, url_for
from website import db
from website.models import Begeleider
from website.begeleider.forms import VoegtoeBegeleider

# Definiëren van de begeleiders blueprint met de bijbehorende URL-prefix en template-folder
begeleiders_blueprint = Blueprint('begeleiders',
                                  __name__,
                                  template_folder='templates/begeleiders')

# Route voor het toevoegen van een begeleider
@begeleiders_blueprint.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeBegeleider()

    if form.validate_on_submit():
        naam = form.naam.data
        id = form.id.data
        
        # Controleren of de begeleider al bestaat op basis van ID
        existing_begeleider = Begeleider.query.filter_by(id=id).first()
        if existing_begeleider:
            existing_begeleider.naam = naam  # Naam bijwerken als de begeleider al bestaat
        else:
            new_begeleider = Begeleider(naam=naam, stage_id=id)
            db.session.add(new_begeleider)
        
        db.session.commit()
        return redirect(url_for('stages.lijst')) # Doorverwijzen naar de lijst met stages na toevoegen van begeleider
    
    return render_template('begeleider_toevoegen.html', form=form)
