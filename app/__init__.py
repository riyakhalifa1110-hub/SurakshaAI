import os
import json

from flask import Flask, session, redirect, request


def create_app():

    app = Flask(__name__)
    app.config.from_object("config.Config")

    # ----------------------------
    # Load translations
    # ----------------------------
    translations = {}

    translation_path = os.path.join(
        os.path.dirname(__file__),
        "translations"
    )

    for lang in ["en", "hi", "gu"]:
        with open(
            os.path.join(translation_path, f"{lang}.json"),
            encoding="utf-8"
        ) as f:

            translations[lang] = json.load(f)

            print(lang)
            print("technology_python =", translations[lang].get("technology_python"))
            print("smart_features =", translations[lang].get("smart_features"))
            print("supported_languages =", translations[lang].get("supported_languages"))
            print("--------------------------------")

    # ----------------------------
    # Import Blueprints
    # ----------------------------
    from app.routes.main import main
    from app.routes.sms import sms
    from app.routes.whatsapp import whatsapp
    from app.routes.upi import upi
    from app.routes.url import url
    from app.routes.call import call_bp
    from app.routes.learn import learn
    from app.routes.emergency import emergency
    from app.routes.about import about_bp

    # ----------------------------
    # Register Blueprints
    # ----------------------------
    app.register_blueprint(main)
    app.register_blueprint(sms)
    app.register_blueprint(whatsapp)
    app.register_blueprint(upi)
    app.register_blueprint(url)
    app.register_blueprint(call_bp)
    app.register_blueprint(learn)
    app.register_blueprint(emergency)
    app.register_blueprint(about_bp)

    # ----------------------------
    # Language Route
    # ----------------------------
    @app.route("/set-language/<lang>")
    def set_language(lang):

        if lang in ["en", "hi", "gu"]:
            session["language"] = lang

        return redirect(request.referrer or "/")

    # ----------------------------
    # Global Template Variables
    # ----------------------------
    @app.context_processor
    def inject_language():

        lang = session.get("language", "en")

        return {
            "current_language": lang,
            "t": translations[lang]
        }

    return app