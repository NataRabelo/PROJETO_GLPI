from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app.models import Usuario
from app import bcrypt, db

auth = Blueprint('auth', __name__)

@auth.route('/registrar', methods=['GET', 'POST'])
@login_required
def registrar():
    if request.method == 'POST':
        email           = request.form.get('email')
        nome            = request.form.get('nome')
        senha           = request.form.get('senha')
        tipo_usuario    = request.form.get('tipo_usuario')
        empresa         = request.form.get('empresa')

        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario:
            flash('Email já cadastrado.', 'danger')
            return redirect(url_for('auth.login'))
        
        usuario = Usuario(
            nome=nome, 
            email=email,
            senha=bcrypt.generate_password_hash(senha).decode('utf-8'),
            tipo_usuario=tipo_usuario,
            empresa=empresa
        )
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('auth.login'))
    
    return render_template('registrar.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, senha):
            login_user(usuario)
            return redirect(url_for('main.index'))
        else:
            flash('Email ou senha incorretos.', 'danger')

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))