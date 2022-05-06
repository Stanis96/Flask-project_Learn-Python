from flask import request
from werkzeug.urls import url_parse
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from app.users.forms import  LoginForm, RegistrationForm
from app.db import db
from app.users.models import User

blueprint = Blueprint('user', __name__, url_prefix='/')


@blueprint.route('/login', methods=['GET', 'POST'])
def login_page(): 
    if current_user.is_authenticated:
        return redirect(url_for('main.index_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('user.login_page'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index_page')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index_page'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index_page'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('user.login_page'))
    return render_template('register.html', title='Register', form=form)
