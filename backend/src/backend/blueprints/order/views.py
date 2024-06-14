from flask import Blueprint, current_app, flash, jsonify, redirect, render_template, request, url_for


order = Blueprint('order', __name__, template_folder="templates/order", url_prefix="/order")

@order.route("/")
def create():
    elements = {
        "title": "Greenleaf Cleaning",
    }
    return render_template("create.html", elements=elements)

