import os
import pandas as pd


class MovieLens(object):
    def __init__(self):
        self.path = os.getenv("DATASET_TRAIN_MODEL")
        self.movies_df = None
        if self.path:
            self.movies_df = pd.read_parquet(self.path)

    def get_instance(self, movie_id: int):
        instance = self.movies_df[self.movies_df["movieId"] == movie_id]
        if not instance.empty:
            return instance.values.tolist()[0][:-1]
        else:
            return False

    def get_df_list(self):
        return self.movies_df.values.tolist()
