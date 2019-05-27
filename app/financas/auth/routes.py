from flask import (current_app, flash, redirect, render_template, request,
                   url_for)

from app.financas.auth import auth
from app.financas.models.models import User
from flask_login import login_required, login_user, logout_user

from .forms import LoginForm, RegisterForm


class Login:
    @auth.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        form = LoginForm(request.form)
        if request.method == 'POST':
            if form.validate_on_submit():
                user = User.query.filter_by(
                    name=request.form['username']).first()
                if user is not None and bcrypt.check_password_hash(
                    user.password, request.form['password']
                ):
                    login_user(user)
                    flash('You were logged in. Go Crazy.')
                    return redirect(url_for('home.home'))

                else:
                    error = 'Invalid username or password.'
        return "hello"

    @auth.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You were logged out.')
        return 'deslogado'

    @auth.route(
        '/register/', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if request.method == 'POST':
            user = User(
                request.args.get('username'), request.args.get('password')
            )
            dbsession = current_app.config.get('dbsession')
            dbsession.add(user)
            dbsession.commit()
            login_user(user)
            return 'logado'
        return 'logar'
