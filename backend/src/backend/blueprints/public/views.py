import os
from flask import Blueprint, current_app, flash, jsonify, redirect, render_template, request, url_for

from ...models.models import db, Supplier
from ...models.test.populate import populate_suppliers, populate_colors, populate_coil_options, populate_accessories

public = Blueprint('public', __name__, template_folder="templates/public", url_prefix="/")

# Testing route
@public.route("/insert/populate")
def test():
    with current_app.app_context():
        populate_suppliers(db)
        populate_colors(db)
        populate_coil_options(db)
        populate_accessories(db)    
    
    return redirect(url_for('public.index'))


# 404 handler
@public.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


# 500 handler
@public.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template("500.html"), 500


@public.route("/")
def index():
    elements = {
        "title": os.environ["COMPANY"],
        "company": os.environ["COMPANY"],
    }
    return render_template("index.html", elements=elements)


@public.route("/about-us")
def about():
    elements = {
        "title": os.environ["COMPANY"],
    }
    return render_template("about.html", elements=elements)


@public.route("/contact-us")
def contact():
    elements = {
        "title": os.environ["COMPANY"],
    }
    return render_template("contact.html", elements=elements)


@public.route("/cleaning")
def cleaning():
    elements = {
        "title": os.environ["COMPANY"],
    }
    return render_template("cleaning.html", elements=elements)


@public.route("/delivery")
def delivery():
    elements = {
        "title": os.environ["COMPANY"],
    }
    return render_template("delivery.html", elements=elements)


@public.route("/repairs")
def repairs():
    elements = {
        "title": os.environ["COMPANY"],
    }
    return render_template("repairs.html", elements=elements)


@public.route("/replacements")
def replacements():
    elements = {
        "title": os.environ["COMPANY"],
    }
    return render_template("replacements.html", elements=elements)



# thinking about splitting this into its own blueprint
@public.route("/gutter-delivery")
def gutter_delivery():
    elements = {
        "title": os.environ["COMPANY"],
    }
    return render_template("gutter_delivery.html", elements=elements)



@public.route("/gutter-guards")
def gutter_guards():
    elements = {
        "title": os.environ["COMPANY"],
    }
    return render_template("gutter_guards.html", elements=elements)
