from flask import Blueprint, render_template

learn = Blueprint("learn", __name__)

@learn.route("/learn")
def learn_page():
    return render_template("learn/index.html")