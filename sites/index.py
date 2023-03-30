import flask as f
from flask.blueprints import Blueprint

index_site = Blueprint("index_site", __name__)

@index_site.route("/")
def index():
    return f.render_template("index.html")