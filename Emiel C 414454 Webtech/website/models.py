from website import db, app, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Methode om gebruikers op te halen aan de hand van hun ID voor inlogbeheer
@login_manager.user_loader
def load_user(user_id):
    return Beheerder.query.get(user_id)


# Model voor Beheerder (administrator) met authenticatiefunctionaliteit
class Beheerder(db.Model, UserMixin):
    __tablename__ = 'beheerders'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Model voor Stage met betrekking tot studenten, begeleiders en instellingen
class Stage(db.Model):
    __tablename__ = 'stages'
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.Text)
    periode = db.Column(db.Text)
    cijfer = db.Column(db.Float)
    student = db.relationship('Student', backref='stage', uselist=False, cascade='all, delete-orphan')
    begeleider = db.relationship('Begeleider', backref='stage', uselist=False, cascade='all, delete-orphan')
    instelling = db.relationship('Instelling', backref='stage', uselist=False, cascade='all, delete-orphan')


    def __init__(self, periode, cijfer, naam):
        self.periode = periode
        self.cijfer = cijfer
        self.naam = naam

    def __repr__(self):
        output = f"Stage ID: {self.id} || Stage bedrijf: {self.naam} || Stage periode: {self.periode} || Cijfer: {self.cijfer}."

        if self.student:
            output += f"\n || Student: {self.student.naam}."

        if self.begeleider:
            output += f"\n || Begeleider: {self.begeleider.naam}."

        if self.instelling:
            output += f"\n || Instelling: {self.instelling.naam}, soort: {self.instelling.soort}."

        return output


# Model voor Student
class Student(db.Model):
    __tablename__ = 'studenten'

    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.Text)
    stage_id = db.Column(db.Integer, db.ForeignKey('stages.id'))

    def __init__(self, naam, stage_id):
        self.naam = naam
        self.stage_id = stage_id

    def __repr__(self):
        return f"Deze student heet {self.naam}."


# Model voor Begeleiders
class Begeleider(db.Model):
    __tablename__ = 'begeleiders'

    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.Text)
    stage_id = db.Column(db.Integer, db.ForeignKey('stages.id'))

    def __init__(self, naam, stage_id):
        self.naam = naam
        self.stage_id = stage_id

    def __repr__(self):
        return f"Deze begeleider heet {self.naam}"


# Model van Instellingen
class Instelling(db.Model):
    __tablename__ = 'instellingen'

    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.Text)
    soort = db.Column(db.Text)
    stage_id = db.Column(db.Integer, db.ForeignKey('stages.id'))


    def __init__(self, naam, soort, stage_id):
        self.naam = naam
        self.soort = soort
        self.stage_id = stage_id

    def __repr__(self):
        return f"Deze instelling heet {self.naam}. Dit is een {self.soort} gerichte instelling."


# Creëert de database tabellen
with app.app_context():
    db.create_all()