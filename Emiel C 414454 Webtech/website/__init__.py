import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

# Configuratie van de database
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supergeheimesleutel' # Geheime sleutel voor sessies

db = SQLAlchemy(app)
Migrate(app, db)

DATABASE = 'data.db'

login_manager.init_app(app)
login_manager.login_view = 'login' # Het inloggen wordt gedaan via de 'login' route

from website import route, models

with app.app_context():
    db.create_all()
    print("Nieuwe database en tabellen zijn aangemaakt.")

# Importeren van blueprints voor de verschillende onderdelen van de website
from website.stage.views import stages_blueprint
from website.student.views import studenten_blueprint
from website.begeleider.views import begeleiders_blueprint
from website.instelling.views import instellingen_blueprint

# Registreren van de blueprints met hun respectievelijke URL-prefixes
app.register_blueprint(stages_blueprint, url_prefix='/stages')
app.register_blueprint(studenten_blueprint, url_prefix='/studenten')
app.register_blueprint(begeleiders_blueprint, url_prefix='/begeleiders')
app.register_blueprint(instellingen_blueprint, url_prefix='/instellingen')

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()  # Maakt de tabellen aan in de database
        app.run(debug=True)
