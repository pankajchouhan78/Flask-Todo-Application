import os

class Config:
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# postgresql://username:password@host:port/dtabase_name

SECRET_KEY = "hello world"