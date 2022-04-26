from flask import Flask, Blueprint
from movie_recommendation.script import catalog, movie
import os

application = Flask(__name__)
blueprint = Blueprint("api", __name__)
application.register_blueprint(blueprint)
application.config["SECRET_KEY"] = os.urandom(32)
movielens = movie.MovieLens()
movie_catalog = catalog.MovieCatalog()
