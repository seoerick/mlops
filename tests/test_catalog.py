from unittest import TestCase
from movie_recommendation.script import catalog


class TestMovieCatalog(TestCase):
    def setUp(self) -> None:
        self.movie_catalog = catalog.MovieCatalog()
        self.movie_catalog.catalog = {
                                        "title": {1: "Toy Story (1995)",
                                                  2: "Jumanji (1995)"},
                                        "genre": {1: "Adventure|Animation|Children|Comedy|Fantasy",
                                                  2: "Adventure|Children|Fantasy"}
                                    }

    def test_get_title(self):
        return_value = self.movie_catalog.get_title(movie_id=1)
        expected = "Toy Story (1995)"
        assert return_value == expected

    def test_get_title_not_found(self):
        return_value = self.movie_catalog.get_title(movie_id=404)
        expected = "Not Found"
        assert return_value == expected

    def test_list_title(self):
        return_value = self.movie_catalog.list_title()
        expected = {1: "Toy Story (1995)", 2: "Jumanji (1995)"}
        assert return_value == expected

    def test_get_genre(self):
        return_value = self.movie_catalog.get_genre(movie_id=1)
        expected = "Adventure|Animation|Children|Comedy|Fantasy"
        assert return_value == expected

    def test_get_genre_not_found(self):
        return_value = self.movie_catalog.get_genre(movie_id=404)
        expected = "Not Found"
        assert return_value == expected

    def test_list_genre(self):
        return_value = self.movie_catalog.list_genre()
        expected = {1: "Adventure|Animation|Children|Comedy|Fantasy",
                    2: "Adventure|Children|Fantasy"}
        assert return_value == expected