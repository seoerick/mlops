from movie_recommendation.app import hello_world
from unittest import TestCase


class TestApp(TestCase):
    def test_get_schema(self):
        return_value = hello_world()
        expected = {'data': [{'hello': 'world'}]}
        assert return_value == expected





