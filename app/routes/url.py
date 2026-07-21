from flask import Blueprint, render_template, request, session

from app.services.url_service import analyze_url

url = Blueprint("url", __name__)


@url.route("/url", methods=["GET", "POST"])
def url_page():

    result = None

    if request.method == "POST":

        message = request.form.get("message")

        if message:

            language = session.get("language", "en")

            result = analyze_url(message, language)

    return render_template(
        "url/index.html",
        result=result
    )