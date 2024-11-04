from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Users, db
from flask_login import login_user, logout_user
auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')

@auth_blueprint.route('/')
def index():
    return "hello world"

# pip install flask-login

@auth_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        user = Users(username=username, password=password)
        # Add the user to the database
        db.session.add(user)
        try:
            db.session.commit()
            flash('Registration successful!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Username might already be taken.', 'error')
            return redirect(url_for('auth_blueprint.register'))
        
        return redirect(url_for('auth_blueprint.login'))
        
    else:
        return render_template('auth/register.html')
    
@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':     
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        user = Users.query.filter_by(username=username).first()
        
        if user.password == password:
            # Use the login_user method to log in the user
            login_user(user)
            return redirect('/todo')
        else:
            flash('Login failed. Password Invalid.', 'error')
            return redirect(url_for('auth_blueprint.login'))
    else:
        return render_template('auth/login.html')
    
@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('todo_blueprint.index'))
