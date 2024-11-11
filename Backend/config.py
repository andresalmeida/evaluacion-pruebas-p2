import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://darwin:password@localhost:5432/evaluacion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
