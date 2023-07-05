from flask import Blueprint

bp = Blueprint("workout", __name__, static_folder="static", template_folder="templates")