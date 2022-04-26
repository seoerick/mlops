import sys
import numpy as np
import pandas as pd
import pickle
from utils import util


if __name__ == "__main__":

    yaml_cfg = util.get_config(sys.argv[1])

    INPUT_PATH = yaml_cfg["paths"]["input"]
    OUTPUT_PATH = yaml_cfg["paths"]["output"]

    movies_df = util.read_df(
        path=f"./{INPUT_PATH}/movie.parquet",
        columns=yaml_cfg["columns"]["movie"],
        format_type="parquet",
    )
    movies_df = movies_df.drop_duplicates()

    movies_df = (
        movies_df.groupby(["movieId", "genres", "title"])
        .agg(size_rating=("rating", np.size), mean_rating=("rating", np.mean))
        .reset_index()
    )
    movies_df["size_rating"] = movies_df["size_rating"].apply(
        lambda x: (x - movies_df["size_rating"].min())
        / (movies_df["size_rating"].max() - movies_df["size_rating"].min())
    )

    catalog = {
        "title": dict(zip(movies_df.movieId, movies_df.title)),
        "genre": dict(zip(movies_df.movieId, movies_df.genres)),
    }

    movies_df = movies_df.assign(genres=movies_df["genres"].str.split("|")).explode(
        "genres"
    )
    genre_list = list(movies_df["genres"].unique())
    movies_df = pd.concat(
        [movies_df.drop(columns=["genres"]), pd.get_dummies(movies_df.genres).mul(1)],
        axis=1,
    )
    movies_df = movies_df.drop(columns=["(no genres listed)"])
    genre_list.remove("(no genres listed)")

    movies_df = (
        movies_df.groupby(["movieId", "title", "size_rating", "mean_rating"])[
            genre_list
        ]
        .sum()
        .reset_index()
    )

    movies_df = movies_df[genre_list + ["size_rating", "mean_rating", "movieId"]]
    movies_df.to_parquet(f"{OUTPUT_PATH}/movie.parquet")
    with open(f"{OUTPUT_PATH}/catalog.pickle", "wb") as handle:
        pickle.dump(catalog, handle, protocol=pickle.HIGHEST_PROTOCOL)
