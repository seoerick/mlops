import os
from typing import Dict, List, AnyStr
import pickle


class MovieCatalog(object):
    def __init__(self):
        self.path = os.getenv("CATALOG_PKL")
        self.catalog = None
        if self.path:
            self.catalog = self.read_catalog()

    def read_catalog(self) -> Dict[AnyStr, Dict[AnyStr, List[AnyStr]]]:
        with open(self.path, "rb") as handle:
            catalog = pickle.load(handle)
        return catalog

    def get_title(self, movie_id: int) -> str:
        if (isinstance(movie_id, int)) and (movie_id in self.catalog["title"]):
            return self.catalog["title"][movie_id]
        else:
            return "Not Found"

    def list_title(self) -> Dict[AnyStr, List[AnyStr]]:
        return self.catalog["title"]

    def get_genre(self, movie_id: int) -> Dict[AnyStr, List[AnyStr]]:
        if (isinstance(movie_id, int)) and (movie_id in self.catalog["genre"]):
            return self.catalog["genre"][movie_id]
        else:
            return "Not Found"

    def list_genre(self) -> List:
        return self.catalog["genre"]
