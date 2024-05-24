from flask import Blueprint, current_app, flash, jsonify, redirect, render_template, request, url_for

from ...models.models import db, Supplier

public = Blueprint('public', __name__, template_folder="templates/public", url_prefix="/")

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
        "title": "Greenleaf Cleaning",
    }
    return render_template("index.html", elements=elements)


# 
@public.route("/test", methods=["GET","POST"])
def test():
    with current_app.app_context():
        from ...models.populate import populate_suppliers
        populate_suppliers(db)
    return jsonify("pong")

