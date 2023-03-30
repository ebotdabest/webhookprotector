import flask as f
from flask.blueprints import Blueprint

protect_bp = Blueprint("protect_bp", __name__)

@protect_bp.route("/<hook>", subdomain="<id>")
def test(id, hook):
    ip = f.request.environ.get('HTTP_X_REAL_IP', f.request.remote_addr)
    from tempdb import get_webhook
    try:
        data = get_webhook(id, hook)
        if data != None:
            if ip in data["allowed_ips"]:
                return f"User id: {id}, Hook id: {hook}"
            else:
                return "I'm sorry but you are unauthorized!"
        else:
            return "The webhook is invalid!"
    except KeyError:
        return "As it appears either the user is invalid!"



@protect_bp.route("/", subdomain="db")
def db():
    print("Nice")
    return "Hello"