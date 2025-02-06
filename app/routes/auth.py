from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app import bcrypt, db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def index():
    return "<h2> Deu certo </h2>"

@auth_bp.route('/registro', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        email = request.form.get('email')
        verificar_email = User.query.filter_by(email=email).first()
        if verificar_email: 
            flash('Email já cadastrado', 'error')
            return redirect(url_for('auth_bp.registro'))

        password = request.form.get('password')
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(
            username = request.form.get('username'),
            password_hash = password_hash,
            email = email,
            role = request.form.get('role')
        )
        db.session.add(user)
        db.session.commit()
        flash('Usuário resgistrado com sucesso', 'success')
        return redirect(url_for('auth_bp.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.password_hash and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('main/menu.html'))
        else:
            flash('E-mail ou senha inválidos.', 'error')
            return redirect(url_for('auth_bp.login'))
    return render_template('auth/login.html')

@auth_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Você deslogou do sistema', 'info')
    return redirect(url_for('main_bp.index'))

@auth_bp.route('/menu', methods=['GET', 'POST'])
@login_required
def menu():
    render_template('main/menu.html')