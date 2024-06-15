from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from ..models import Supplier, ColorOption, CoilOption, Accessory

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


def populate_colors(db: SQLAlchemy) -> None:
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
    dump = []
    lansing = db.session.scalars(
        db.select(Supplier).where(Supplier.supplier == "Lansing Building Products")).first()
    for c in lansing_gutter_coil:
        dump.append(ColorOption(color=c, supplier_id=lansing.id))
    with current_app.app_context():
        try:
            db.session.add_all(dump)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(IntegrityError)


def populate_coil_options(db: SQLAlchemy) -> None:
    colors = db.session.scalars(db.select(ColorOption)).all()
    dump = []

    # five inch
    for c in colors:
        dump.append(CoilOption(style="K-Style", size="Five Inch", color_id=c.id))
        
    # six inch
    for c in colors:
        dump.append(CoilOption(style="K-Style", size="Six Inch", color_id=c.id))   

    with current_app.app_context():
        try: 
            db.session.add_all(dump)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(IntegrityError)
        

def populate_accessories(db: SQLAlchemy) -> None:
    colors = db.session.scalars(db.select(ColorOption)).all()
    six = db.session.scalar(db.select(CoilOption).where(CoilOption.size == "Six Inch"))
    five = db.session.scalar(db.select(CoilOption).where(CoilOption.size == "Five Inch"))

    dump = []
    # coil types
    five_inch = [
        "2x3 A", 
        "2x3 B", 
        "2x3 Downspout", 
        "2x3 Ledge Jumper", 
        "Left Endcap (5\")", 
        "Right Endcap (5\")",
    ]
    six_inch = [
        "3x4 A", 
        "3x4 B", 
        "3x4 Downspout", 
        "3x4 Ledge Jumper", 
        "Left Endcap (6\")", 
        "Right Endcap (6\")",
    ]
    for c in colors:
        # All colors, this should for sure be rechecked against Lansing Options
        for f in five_inch:
            dump.append(Accessory(color_id=c.id, coil_id=five.id, accessory=f))

        for s in six_inch:
            dump.append(Accessory(color_id=c.id, coil_id=six.id, accessory=s))
    
    with current_app.app_context():
        try:
            db.session.add_all(dump)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(IntegrityError)
        

