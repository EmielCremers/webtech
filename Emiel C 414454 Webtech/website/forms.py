from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from website.models import Beheerder


# Formulier voor inloggen
class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Inloggen')


# Formulier voor registratie
class RegistrationForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Gebruikersnaam', validators=[DataRequired()])
    password = PasswordField('Wachtwoord', validators=[DataRequired(), EqualTo('pass_confirm', message='Wachtwoorden moeten overeenkomen!')])
    pass_confirm = PasswordField('Wachtwoord bevestigen', validators=[DataRequired()])
    submit = SubmitField('Registreren')

    # Controleert of het e-mailadres al in gebruik is
    def check_mail(self, field):
        if Beheerder.query.filter_by(email=field.data).first():
            raise ValidationError('Dit e-mailadres is al geregistreerd!')
        
    
    # Controleert of de gebruikersnaam al in gebruik is    
    def check_username(self, field):
        if Beheerder.query.filter_by(username=field.data).first():
            raise ValidationError('Deze gebruikersnaam wordt al gebruikt. Kies een andere naam')