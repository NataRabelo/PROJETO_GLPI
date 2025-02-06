from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import Ticket
from app import bcrypt, db

ticket_bp = Blueprint('ticket_bp', __name__)

@ticket_bp.route('/criar_ticket', methods=['GET', 'POST'])
@login_required
def criar_ticket():
    ticket = Ticket(
        title = request.form.get('title'),
        description = request.form.get('description'),
        status = request.form.get('status'),
        priority = request.form.get('prioriry'),
        user_id = request.form.get('user'),
        category_id = request.form.get('category')
    )
    db.session.add(ticket)
    db.session.commit()
    flash('ticket criado com sucesso', 'success')
    return redirect(url_for('auth_bp.menu'))

@ticket_bp.route('/listar_ticket', methods=['GET', 'POST'])
@login_required
def listar_ticket():
    tickets = Ticket.query.all()
    return render_template('ticket/list.html', tickets=tickets)

@ticket_bp.route('ler_ticket', methods=['GET', 'POST'])
@login_required
def ler_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    return render_template('ticket/detail.html', ticket=ticket)

@ticket_bp.route('atualizar_ticket', methods=['GET', 'POST'])
@login_required
def atualizar_ticket(id):
    ticket = Ticket.query.get_or_404(id)

    if request.method == 'POST':
        ticket.title = request.form.get('title')
        ticket.description = request.form.get('description')
        ticket.status = request.form.get('status')
        ticket.priority = request.form.get('priority')
        ticket.user_id = request.form.get('user')
        ticket.category_id = request.form.get('category')

        db.session.commit()
        flash('ticket atualizado com sucesso!', 'success')
        return redirect(url_for('ticket_bp.listar'))
    return render_template('ticket/details') 