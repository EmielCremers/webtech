from flask import Blueprint, render_template, redirect, url_for, flash
from website import db
from website.models import Student
from website.student.forms import VoegtoeStudent

# Definiëren van de studenten blueprint met bijbehorende URL-prefix en template folder
studenten_blueprint = Blueprint('studenten',
                                __name__,
                                template_folder='templates/studenten')

# Route voor het toevoegen van een student
@studenten_blueprint.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = VoegtoeStudent()

    if form.validate_on_submit():
        naam = form.naam.data
        id = form.id.data
        
        # Controleren of de student al bestaat op basis van ID
        existing_student = Student.query.filter_by(id=id).first()
        if existing_student:
            existing_student.naam = naam  # Naam bijwerken als de student al bestaat
        else:
            new_student = Student(naam=naam, stage_id=id)
            db.session.add(new_student)
        
        db.session.commit()
        return redirect(url_for('stages.lijst')) # Doorverwijzen naar de lijst met stages na toevoegen van student
    
    return render_template('student_toevoegen.html', form=form)
