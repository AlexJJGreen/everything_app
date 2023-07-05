from flask import render_template
from . import bp

@bp.route("/")
@bp.route("/home")
def index():
    return render_template("index.html")