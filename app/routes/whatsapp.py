from flask import Blueprint, render_template, request, session
import os
from werkzeug.utils import secure_filename

from app.services.whatsapp_service import analyze_whatsapp
from app.services.ocr_service import extract_text_from_image

whatsapp = Blueprint("whatsapp", __name__)

UPLOAD_FOLDER = "uploads"


@whatsapp.route("/whatsapp", methods=["GET", "POST"])
def whatsapp_page():

    result = None
    extracted_text = ""

    if request.method == "POST":

        # Get selected language
        language = session.get("language", "en")

        message = request.form.get("message", "").strip()
        image = request.files.get("image")

        if image and image.filename:

            os.makedirs(UPLOAD_FOLDER, exist_ok=True)

            filename = secure_filename(image.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)

            image.save(filepath)

            extracted_text = extract_text_from_image(filepath).strip()

            if extracted_text:
                result = analyze_whatsapp(extracted_text, language)

            os.remove(filepath)

        elif message:

            extracted_text = message

            result = analyze_whatsapp(message, language)

    return render_template(
        "whatsapp/index.html",
        result=result,
        extracted_text=extracted_text
    )