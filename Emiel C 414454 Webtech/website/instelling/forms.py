from website.models import Stage
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField 
from wtforms.validators import ValidationError, DataRequired

# Formulier voor het toevoegen van een instelling
class VoegtoeInstelling(FlaskForm):

    naam = StringField("Naam van de instelling: ", validators=[DataRequired()])
    soort = StringField("Soort van de instelling: ", validators=[DataRequired()])
    id = IntegerField("ID van de stage: ", validators=[DataRequired()])
    submit = SubmitField("Toevoegen", validators=[DataRequired()])

    # Valideer of het opgegeven stage ID bestaat
    def validate_id(self, id):
        stage = Stage.query.get(id.data)
        if stage is None:
            raise ValidationError('Dit stage ID bestaat niet. Voer een geldig stage ID in.')