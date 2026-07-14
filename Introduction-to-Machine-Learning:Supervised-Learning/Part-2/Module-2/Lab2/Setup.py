Lab 2: Principal Component Analysis (PCA)

In this lab, you will explore Principal Component Analysis (PCA), one of the most important dimensionality reduction techniques in machine learning. You will work with the Wine dataset, which contains chemical measurements from 178 wine samples.

You will:

Understand why standardization is critical before applying PCA
Fit a PCA model and analyze variance explained by each component
Use scree plots and cumulative variance to choose the number of components
Interpret loadings to understand what each principal component represents
Transform data to principal component space and visualize the results
Reconstruct data from a reduced number of components
These concepts are fundamental to dimensionality reduction, data visualization, and preprocessing for downstream machine learning tasks


import pathlib
from typing import Tuple, Dict, List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

RANDOM_STATE: int = 42
np.random.seed(RANDOM_STATE)

_DATA_PATH = pathlib.Path("wine.csv")
if not _DATA_PATH.exists():
    raise FileNotFoundError(
        "wine.csv is missing from the lab directory. Please run the download "
        "script (w2_download_datasets.py) or ask the TA for assistance."
    )
