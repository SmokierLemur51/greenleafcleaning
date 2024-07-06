import os
from flask import Blueprint, current_app, flash, jsonify, redirect, render_template, request, url_for

from .forms import ContactRequestForm, EstimateRequestForm
from ...models.models import db
from ...models.models import (
    Supplier, 
    ContactRequest, 
    EstimateRequest,
)
public = Blueprint('public', __name__, template_folder="templates/public", url_prefix="/")

# Testing route
@public.route("/insert/populate")
def test():
    # with current_app.app_context():
    #     populate_suppliers(db)
    #     populate_colors(db)
    #     populate_coil_options(db)
    #     populate_accessories(db)    
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
        "company": os.environ["COMPANY"],
        "company": os.environ["COMPANY"],
    }
    return render_template("index.html", elements=elements)


""" Info pages """
@public.route("/about-us")
def about():
    elements = {
        "company": os.environ["COMPANY"],
        "company": os.environ["COMPANY"],
    }
    return render_template("about.html", elements=elements)



@public.route("/cleaning")
def cleaning():
    elements = {
        "title": "Cleaning",
        "company": os.environ['COMPANY'],
    }
    return render_template("cleaning.html", elements=elements)



@public.route("/repairs")
def repairs():
    elements = {
        "title": "Gutter Repairs",
        "company": os.environ["COMPANY"],
    }
    return render_template("repairs.html", elements=elements)


@public.route("/installation")
def replacements():
    elements = {
        "title": "Gutter Installations", 
        "company": os.environ["COMPANY"],
    }
    return render_template("replacements.html", elements=elements)


@public.route("/gutter-guards")
def gutter_guards():
    elements = {
        "title": "Gutter Guards ", 
        "company": os.environ["COMPANY"],
    }
    return render_template("gutter_guards.html", elements=elements)


""" Contact Request Pages """
@public.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactRequestForm()
    print(form.errors)
    if form.validate_on_submit():
        new_ = ContactRequest(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            message=form.message.data,
        )
        with current_app.app_context():    
            db.session.add(new_)
            db.session.commit()
        flash("Thank you! We will be in touch.")
        return redirect(url_for("public.index"))
    elements = {
        "title": "Contact Us",
        "company": os.environ['COMPANY'],
    }
    return render_template("contact.html", elements=elements, form=form)


@public.route("/estimate", methods=["GET", "POST"])
def estimate():
    form = EstimateRequestForm()
    print(form.errors)
    if form.validate_on_submit():
        new_ = EstimateRequest(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            message=form.message.data,
        )
        with current_app.app_context():    
            db.session.add(new_)
            db.session.commit()
        flash("Thank you! We will be in touch.")
        return redirect(url_for("public.index"))
    elements = {
        "title": "Get Estimate",
        "company": os.environ['COMPANY'],
    }
    return render_template("estimate.html", elements=elements, form=form)


""" Gutter Delivery Pages"""
# Might end up splitting this into its own blueprint
@public.route("/delivery")
def delivery():
    elements = {
        "title": "Gutter Delivery",
        "company": os.environ["COMPANY"],
    }   
    return render_template("delivery.html", elements=elements)
