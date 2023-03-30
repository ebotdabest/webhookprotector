import flask as f
from flask.blueprints import Blueprint

from zenora import APIClient

login_site = Blueprint("login_site", __name__)

@login_site.route("/login")
def login_stp1():
    return f.redirect("https://discord.com/api/oauth2/authorize?client_id=1086590544429465642&redirect_uri=http%3A%2F%2F127.0.0.1%3A5402%2Flogged&response_type=code&scope=identify%20email")

@login_site.route("/logged")
def login_stp2():
    code = f.request.args.get("code")
    cl = APIClient(token = "MTA4NjU5MDU0NDQyOTQ2NTY0Mg.GchsP5.PdT2ur8jYA22RdH8BQQM6DnWSgehuz74TMu2uM", client_secret="fuYDFPo0PAHxRspqpVnUj7ODkNvp_4nN")
    token = cl.oauth.get_access_token(code, "http://127.0.0.1:5402/logged").access_token
    user = APIClient(token, bearer=True).users.get_current_user()


    return user.username + "#" + str(user.discriminator) + f"_________Id:{user.id}" + f"_________BIO:{user.bio}"