from flask import Blueprint, current_app, flash, jsonify, redirect, render_template, request, url_for

from ...models.models import db, Supplier

public = Blueprint('public', __name__, template_folder="templates/public", url_prefix="/")

# Testing route
@public.route("/test", methods=["GET","POST"])
def test():
    with current_app.app_context():
        from ...models.populate import populate_suppliers
        populate_suppliers(db)
    return jsonify("pong")



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
        "title": "Go-Go Gutters",
    }
    return render_template("index.html", elements=elements)


@public.route("/contact-us")
def contact():
    elements = {
        "title": "Go-Go Gutters",
    }
    return render_template("contact.html", elements=elements)


@public.route("/cleaning")
def cleaning():
    elements = {
        "title": "Go-Go Gutters",
    }
    return render_template("cleaning.html", elements=elements)


@public.route("/repairs")
def repairs():
    elements = {
        "title": "Go-Go Gutters",
    }
    return render_template("repairs.html", elements=elements)


@public.route("/replacements")
def replacements():
    elements = {
        "title": "Go-Go Gutters",
    }
    return render_template("replacements.html", elements=elements)



# thinking about splitting this into its own blueprint
@public.route("/gutter-delivery")
def gutter_delivery():
    elements = {
        "title": "Go-Go Gutters",
    }
    return render_template("gutter_delivery.html", elements=elements)



@public.route("/gutter-guards")
def gutter_guards():
    elements = {
        "title": "Go-Go Gutters",
    }
    return render_template("gutter_guards.html", elements=elements)