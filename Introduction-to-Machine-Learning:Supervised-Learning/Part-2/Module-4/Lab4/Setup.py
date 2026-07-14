import pathlib
from typing import Tuple, Dict, List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

RANDOM_STATE: int = 42
np.random.seed(RANDOM_STATE)

_DATA_PATH = pathlib.Path("iris.csv")
if not _DATA_PATH.exists():
    raise FileNotFoundError(
        "iris.csv is missing from the lab directory. Please run the download "
        "script (w4_download_datasets.py) or ask the TA for assistance."
    )
