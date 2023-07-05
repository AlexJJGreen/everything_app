from flask import render_template
from . import bp

@bp.route("/")
def workout_index():
    return render_template("workout_index.html")