from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField,FloatField
from wtforms.validators import DataRequired

# Formulier voor het toevoegen van een stage
class VoegtoeForm(FlaskForm):
    naam = StringField('Vul de naam van het bedrijf waar je stage voor loopt in: ', validators=[DataRequired()])
    periode = StringField('Vul het jaar en de periode waarin je de stage hebt gelopen in: ', validators=[DataRequired()])
    cijfer = FloatField('Vul het cijfer in: ', validators=[DataRequired()])
    submit = SubmitField('Toevoegen')

# Formulier voor het verwijderen van een stage
class VerwijderForm(FlaskForm):

    id = IntegerField('ID van stage: ', validators=[DataRequired()])
    submit = SubmitField('Verwijderen')