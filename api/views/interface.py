from flask import Blueprint, render_template
from flask_login import login_required, current_user

ui = Blueprint("ui", __name__, url_prefix="/")

@ui.route("/", methods=['GET'])
def index():
    return render_template("index.html", user=current_user)

@ui.route("/profile", methods=['GET'])
@login_required
def profile():
    return render_template("profile.html", user=current_user)


@ui.route("/docs", methods=['GET'])
def docs():
    return render_template("docs.html", user=current_user)