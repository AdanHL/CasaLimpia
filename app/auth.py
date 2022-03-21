from flask import Blueprint, render_template, session, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from app.models import UserModel, UserData

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    
    return render_template('auth/login.html')