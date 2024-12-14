from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user
from models.user import User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/registration', methods=['POST', 'GET'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        if password != confirm_password:
            flash('Пароли не совпадают!', 'error')
            return redirect(url_for('auth.registration'))

        try:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Пользователь зарегистрирован!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ошибка регистрации: {e}', 'error')

    return render_template("auth/registration.html")


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            flash('Успешная авторизация!', 'success')
            next_page = request.args.get("next")
            return redirect(next_page or url_for('home.index'))
        else:
            flash('Неверный email или пароль!', 'error')

    return render_template("auth/login.html")


@auth.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли из системы.', 'success')
    return redirect(url_for('auth.login'))
