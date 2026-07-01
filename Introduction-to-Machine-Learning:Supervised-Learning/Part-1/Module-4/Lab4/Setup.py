# Grade Cell: Import Libraries
#
# This cell imports all necessary libraries for the assignment.
from typing import Tuple, List

import numpy as np
import pandas as pd

# Plotting is optional; imported lazily if needed
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.metrics import mean_squared_error, r2_score

# Set a random state for reproducibility
RANDOM_STATE: int = 42
np.random.seed(RANDOM_STATE)
