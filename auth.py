from flask import Flask, Blueprint

auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')

@auth_blueprint.route('/')
def index():
    return "hello world"

