import flask as f
from flask_session import Session
from flask_ngrok import run_with_ngrok

from sites import index,login,protect

app = f.Flask(__name__)

Session(app)

app.register_blueprint(index.index_site)

app.register_blueprint(login.login_site)

app.register_blueprint(protect.protect_bp)

if __name__ == '__main__':
    # run_with_ngrok(app)
    app.config["SERVER_NAME"] = "localhost:5000"
    app.run()
