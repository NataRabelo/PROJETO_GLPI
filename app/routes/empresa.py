from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app.models import Usuario
from app import bcrypt, db

empresa = Blueprint('empresa', __name__)
