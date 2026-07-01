####In this assignment, you will practice tree-based methods for both regression and classification, including cost-complexity pruning, bagging, random forests, gradient boosting, and interpretation tools (PDP/ICE and permutation importance). We use scikit-learn built-in datasets saved locally to CSV via the provided downloader.


# Grade Cell: Import Libraries
#
# This cell imports all necessary libraries for the assignment.
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, KFold
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
    confusion_matrix,
)
from sklearn.ensemble import (
    BaggingRegressor,
    RandomForestRegressor,
    RandomForestClassifier,
)
from sklearn.inspection import permutation_importance, PartialDependenceDisplay
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier


# Set a random state for reproducibility
RANDOM_STATE: int = 42
