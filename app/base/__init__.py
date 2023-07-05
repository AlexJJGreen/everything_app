from flask import Blueprint

bp = Blueprint("base", __name__, static_folder="static", static_url_path="/base", template_folder="templates")
