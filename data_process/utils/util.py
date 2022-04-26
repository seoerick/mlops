import yaml
from typing import List
import pandas as pd
import math
import operator
from utils.yaml_loader import YamlLoader


def get_config(path: str) -> dict:
    with open(path) as f:
        cfg = yaml.load(f, Loader=YamlLoader)
    return cfg


def read_df(path: str, columns: List[str], format_type: str = "csv") -> pd.DataFrame:
    if format_type == "csv":
        return pd.read_csv(path)[columns]
    if format_type == "parquet":
        return pd.read_parquet(path)[columns]
