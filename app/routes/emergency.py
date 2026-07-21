from flask import Blueprint, render_template

emergency = Blueprint("emergency", __name__)

@emergency.route("/emergency")
def emergency_page():
    return render_template("emergency/index.html")