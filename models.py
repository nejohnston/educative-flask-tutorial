"""
Models
Nicholas Johnston
January 5, 2021
"""
from flask_sqlalchemy import SQLAlchemy
from app import app


def sql_init():
    """
    Create instance of sqlalchemy class
    """
    return SQLAlchemy(app)

# class User(sql_init().Model):

