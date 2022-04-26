from unittest import TestCase

import pandas as pd
from movie_recommendation.script import movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movielens = movie.MovieLens()
        self.movielens.movies_df = pd.DataFrame(
            {
                'Adventure': [1, 1],
                'Animation': [1, 1],
                'Children': [1, 1],
                'Comedy': [1, 1],
                'Fantasy': [1, 1],
                'Romance': [1, 1],
                'Drama': [1, 1],
                'Action': [1, 1],
                'Crime': [1, 1],
                'Thriller': [1, 1],
                'Horror': [1, 1],
                'Mystery': [1, 1],
                'Sci-Fi': [1, 1],
                'IMAX': [1, 1],
                'Documentary': [1, 1],
                'War': [1, 1],
                'Musical': [1, 1],
                'Western': [1, 1],
                'Film-Noir': [1, 1],
                'size_rating': [1, 1],
                'mean_rating': [2.70, 2.71],
                'movieId': [1, 2]
            }
        )

    def test_get_df_list(self):
        return_value = self.movielens.get_df_list()
        expected = self.movielens.movies_df.values.tolist()
        assert return_value == expected

    def test_get_instance_true(self):
        return_value = self.movielens.get_instance(movie_id=1)
        expected = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.7]
        assert return_value == expected

    def test_get_instance_false(self):
        return_value = self.movielens.get_instance(movie_id=999)
        expected = False
        assert return_value == expected