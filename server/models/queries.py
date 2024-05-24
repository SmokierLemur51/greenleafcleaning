"""
File: models/queries.py

This file will be for functions that will return common queries
"""
from flask_sqlalchemy import SQLAlchemy

from .models import Supplier

def load_suppliers(db: SQLAlchemy) -> list[Supplier]:
    return db.session.scalars(db.select(Supplier)).all()



def load_lansing_coil(db: SQLAlchemy) -> None:
    pass