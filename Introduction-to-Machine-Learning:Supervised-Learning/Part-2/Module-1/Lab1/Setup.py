import pathlib
from typing import Tuple, Dict, List

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

RANDOM_STATE: int = 42
np.random.seed(RANDOM_STATE)

_DATA_PATH = pathlib.Path("us_arrests.csv")
if not _DATA_PATH.exists():
    raise FileNotFoundError(
        "us_arrests.csv is missing from the lab directory. Please run the download "
        "script (w1_download_datasets.py) or ask the TA for assistance."
    )
