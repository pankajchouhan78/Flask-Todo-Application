from flask import Flask
import config
from models import db, Todo, Users
from flask_login import LoginManager

from auth import auth_blueprint
from todo_app import todo_blueprint

app = Flask(__name__)
app.config.from_object(config.Config)
app.secret_key = config.SECRET_KEY  # app ke session aur cookies ko secure karne ke liye use hota hai.
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Creates a user loader callback that returns the user object given an id
@login_manager.user_loader
def user_loader(user_id):
    return Users.query.get(user_id)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_blueprint)
app.register_blueprint(todo_blueprint)


if __name__ == '__main__':
    app.run(debug=True)


#  flask --app main run --debug
# export FLASK_APP=main.py
# flask run --reload