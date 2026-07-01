import pathlib
from typing import Tuple, Dict, List

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

RANDOM_STATE: int = 42  # global seed for full reproducibility
np.random.seed(RANDOM_STATE)

_DATA_PATH = pathlib.Path("california_housing.csv")
if not _DATA_PATH.exists():
    raise FileNotFoundError(
        "california_housing.csv is missing from the lab directory. Please download it or ask the TA "
        "for assistance."
    )
