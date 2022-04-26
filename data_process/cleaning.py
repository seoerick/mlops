import sys
from utils import util


if __name__ == "__main__":
    yaml_cfg = util.get_config(sys.argv[1])

    INPUT_PATH = yaml_cfg["paths"]["input"]
    OUTPUT_PATH = yaml_cfg["paths"]["output"]

    movies_df = util.read_df(
        path=f"./{INPUT_PATH}/movies.csv", columns=yaml_cfg["columns"]["movie"]
    )
    tags_df = util.read_df(
        path=f"./{INPUT_PATH}/tags.csv", columns=yaml_cfg["columns"]["tag"]
    )
    ratings_df = util.read_df(
        path=f"./{INPUT_PATH}/ratings.csv", columns=yaml_cfg["columns"]["rating"]
    )

    tags_grouped_df = tags_df.groupby(["movieId", "userId"], as_index=False)["tag"].agg(
        list
    )
    df_tag_rating = ratings_df.merge(
        tags_grouped_df, how="left", on=["movieId", "userId"]
    )
    df_movies_tag_rating = df_tag_rating.merge(movies_df, how="inner", on=["movieId"])

    df_movies_tag_rating.rename(columns={"timestamp": "timestamp_rating"}, inplace=True)
    df_movies = df_movies_tag_rating[yaml_cfg["columns"]["final_columns"]]

    df_movies_tag_rating.to_parquet(f"./{OUTPUT_PATH}/movie.parquet")
