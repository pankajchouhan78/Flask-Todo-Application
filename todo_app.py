from flask import Blueprint, render_template, url_for, request, redirect, flash
from models import Todo, db

todo_blueprint = Blueprint('todo_blueprint', '__name__', url_prefix='/todo')
todo=todo_blueprint

@todo.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title'].strip().lower()
        desc = request.form['desc'].strip()
        new_todo = Todo(title=title, description=desc)
        db.session.add(new_todo)
        db.session.commit()
        flash("Todo  created successfully", 'success')
        return redirect('/todo')
    todos = Todo.query.all() 
    return render_template('todo/index.html', todos=todos)

@todo.route('/edit/<int:id>/', methods=['GET', 'POST'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    if request.method == 'POST':
        is_complated = request.form.get('is_complated', False)
        
        if is_complated is not False:
            is_complated = True

        todo.title = request.form['title'].strip().lower()
        todo.description = request.form['desc'].strip()
        todo.is_complated = is_complated
        db.session.commit()
        flash('Todo update successfully!', 'success')
        return redirect('/todo')
    else:
        return render_template('todo/update.html', todo=todo)

@todo.route('/delete/<int:id>/')
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted successfully!', 'success')
    return redirect('/todo')
        
