from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from .models import Supplier

# Some lists of known colors and respective suppliers
lansing_gutter_coil = [
    "30 deg white",
    "almond",
    "black",
    "cameo",
    "charcoal grey",
    "classic cream",
    "dark bronze",
    "desert sand",
    "everest",
    "evergreen",
    "harbor grey",
    "linen",
    "montana suede",
    "musket brown",
    "pebblestone clay",
    "royal brown",
    "rugged canyon",
    "sandtone",
    "silver grey",
    "terra bronze",
    "victorian grey",
    "wicker",
]


# populating functions start here
def populate_suppliers(db: SQLAlchemy) -> None:
    suppliers_list = [
        Supplier(supplier="Lansing Building Products",
                 street="8181 National Turnpike",
                 city="Louisville",
                 state="KY",
                 zip="40214"),
        Supplier(supplier="Marsh Building Products",
                 street="3328 Gilmore Industrial Blvd",
                 city="Louisville",
                 state="KY",
                 zip="40213"),
        Supplier(supplier="ABC Supply Co",
                 street=" 4601 Commerce Crossings Dr",
                 street_2="#100",
                 city="Louisville",
                 state="KY",
                 zip="40229"),
        Supplier(supplier="SRS Building Products",
                 street="6705 Preston Hwy",
                 city="Louisville",
                 state="KY",
                 zip="40219"),
    ]
    with current_app.app_context():
        try:
            db.session.add_all(suppliers_list)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)


def populate_colors(db: SQLAlchemy, colors: list, source: Supplier) -> None:
    lansing_id = db.session.scalars(
        db.select(Supplier.id).where(Supplier.supplier == "Lansing Building Products")).first()
    for c in colors:
        print(c)
    print(lansing_id)
