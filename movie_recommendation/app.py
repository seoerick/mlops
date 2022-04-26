import os
from movie_recommendation.script import util
from movie_recommendation.script import catalog, movie
from flask import Flask, request, make_response


application = Flask(__name__)
application.config["SECRET_KEY"] = os.urandom(32)

movielens = movie.MovieLens()
movie_catalog = catalog.MovieCatalog()


@application.route("/similar_movie", methods=["GET"])
def similar_movie():
    movieId = int(request.args.get("movieId"))
    test_instance = movielens.get_instance(movieId)
    if not test_instance:
        return make_response("Invalid movieId, see more in endpoint /list_movie", 400)
    k = 10
    neighbors = util.get_neighbors(movielens.get_df_list(), test_instance, k)

    similar_movies = {"movies": []}
    for neighbors_movie in neighbors:
        similar_movieId = neighbors_movie[-1]
        similar_movies["movies"].append(
            {
                "movieId": int(similar_movieId),
                "Title": movie_catalog.get_title(similar_movieId),
                "Genres": movie_catalog.get_genre(similar_movieId),
            }
        )
    return similar_movies


@application.route("/list_movie", methods=["GET"])
def list_movies():
    return {"movies": [movie_catalog.list_title()]}


@application.route("/", methods=["GET"])
def hello_world():
    return {"data": [{"hello": "world"}]}


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5005)
