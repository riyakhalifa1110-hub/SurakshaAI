from flask import Blueprint, render_template, request, session

from app.services.upi_service import analyze_upi

upi = Blueprint("upi", __name__)


@upi.route("/upi", methods=["GET", "POST"])
def upi_page():

    result = None

    if request.method == "POST":

        message = request.form.get("message")

        if message:

            language = session.get("language", "en")

            result = analyze_upi(message, language)

    return render_template(
        "upi/index.html",
        result=result
    )