from flask import render_template
from . import bp
from flask_wtf import FlaskForm

@bp.route("/")
@bp.route("/index")
def workout_index():
    return render_template("workout_index.html")

@bp.route("/create_workout")
def create_workout():
    form = FlaskForm()
    return render_template("create_workout.html")
