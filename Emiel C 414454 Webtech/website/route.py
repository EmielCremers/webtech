# Dit is de route.py file, dit is waarmee de webserver draait.
from website import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from website.models import Beheerder, Student
from website.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def index():
    return render_template('welkom.html') # Rendert de de welkompagina


@app.route('/welkom')
@login_required
def welkom():
    return render_template('welkom.html') # Rendert welkom voor ingelogde gebruikers


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent uitgelogd') # Flashbericht bij uitloggen
    return redirect(url_for('welkom'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Beheerder.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Succesvol ingelogd.') # Flashbericht bij succesvol inloggen

            next_page = request.args.get('next')

            if not next_page or not next_page.startswith('/'):
                next_page = url_for('welkom')

            return redirect(next_page)

    return render_template('login.html', form=form) # Rendert inlogformulier


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = Beheerder(email=form.email.data, username=form.username.data, password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Dank voor de registratie. Er kan nu ingelogd worden !') # Flashbericht voor succesvolle registratie
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form) # Rendert het registratieformulier


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 # Rendert de 404-pagina wanneer een pagina niet gevonden is
