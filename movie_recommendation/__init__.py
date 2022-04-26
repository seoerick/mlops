from flask import Flask, Blueprint
import os

application = Flask(__name__)
blueprint = Blueprint("api", __name__)
application.register_blueprint(blueprint)
application.config["SECRET_KEY"] = os.urandom(32)
