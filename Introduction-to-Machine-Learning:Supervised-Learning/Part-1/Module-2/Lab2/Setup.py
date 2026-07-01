import pathlib
from typing import Tuple, Dict, List

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

RANDOM_STATE: int = 42  # global seed for full reproducibility
np.random.seed(RANDOM_STATE)

_DATA_PATH = pathlib.Path("auto.csv")
if not _DATA_PATH.exists():
    raise FileNotFoundError(
        "auto.csv is missing from the lab directory. Please download it or ask the TA "
        "for assistance."
    )
