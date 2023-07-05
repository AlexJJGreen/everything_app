from flask import render_template
from . import bp
from .forms import LoginForm

@bp.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)