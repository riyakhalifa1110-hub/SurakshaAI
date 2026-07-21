from flask import Blueprint, render_template, request, session

from app.services.call_service import analyze_call
from app.services.voice_service import speech_to_text

call_bp = Blueprint("call", __name__)


@call_bp.route("/call", methods=["GET", "POST"])
def call_page():

    result = None
    transcript = ""

    if request.method == "POST":

        language = session.get("language", "en")

        transcript = request.form.get("message", "").strip()

        audio = request.files.get("audio")

        # Voice recording uploaded
        if audio and audio.filename:
            transcript = speech_to_text(audio)

        if transcript:
            result = analyze_call(transcript, language)

    return render_template(
        "call/index.html",
        result=result,
        transcript=transcript
    )