from flask import Blueprint

bp = Blueprint("main", __name__, template_folder="templates", static_url_path="/", static_folder="static")

from . import views