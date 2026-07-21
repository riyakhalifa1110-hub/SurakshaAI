from flask import Blueprint, render_template, request, session
from app.services.gemini_service import analyze_sms

sms = Blueprint("sms", __name__)


@sms.route("/sms", methods=["GET", "POST"])
def sms_page():

    result = None

    if request.method == "POST":

        message = request.form.get("sms")

        if message:

            language = session.get("language", "en")

            result = analyze_sms(message, language)

    return render_template(
        "sms/index.html",
        result=result
    )