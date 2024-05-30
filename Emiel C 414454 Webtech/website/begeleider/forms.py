from website.models import Stage
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField 
from wtforms.validators import ValidationError, DataRequired

# Formulier voor het toevoegen van een begeleider
class VoegtoeBegeleider(FlaskForm):

    naam = StringField('Naam van de begeleider: ', validators=[DataRequired()])
    id = IntegerField('ID van de stage: ', validators=[DataRequired()])
    submit = SubmitField('Toevoegen')

    # Valideer of het opgegeven stage ID bestaat
    def validate_id(self, id):
        stage = Stage.query.get(id.data)
        if stage is None:
            raise ValidationError('Dit stage ID bestaat niet. Voer een geldig stage ID in.')