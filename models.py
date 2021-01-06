"""
Models
Nicholas Johnston
January 5, 2021
"""
from flask_sqlalchemy import SQLAlchemy
from app import app

def SQL_INIT():
    """
    Create instance of sqlalchemy class
    """
    return SQLAlchemy(app)


database = SQL_INIT()


class User(database.Model):
    column = database.Column
    form_value = database.String
    id = column(database.Integer, primary_key=True)
    email = column(form_value, primary_key=True, unique=True, nullable=False)
    password = column(form_value, nullable=False)


database.create_all()
