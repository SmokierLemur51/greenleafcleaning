""" 
File: models/insert.py

This file will be for the functions I will use to insert data into 
the database. These functions will contain context and error handling. 
"""
from flask import current_app

from flask_sqlalchemy import SQLAlchemy

from .models import ContactRequest

def insert_contact_request(db: SQLAlchemy, c: ContactRequest) -> dict:
    with current_app.app_context():
        try:
            db.session.add(c)
            db.session.commit()
            return {}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"error": e, "contact_request": c}
    