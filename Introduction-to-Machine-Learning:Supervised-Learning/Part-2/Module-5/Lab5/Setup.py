
# Introduction to Machine Learning: Unsupervised Learning
#########
**Instructor:** Daniel Acuna, Ph.D.
**Position:** Associate Professor of Computer Science
**Institution:** University of Colorado Boulder

---

Lab 5: Matrix Completion and Recommender Systems

---

In this lab, you will explore **Matrix Completion**, a powerful technique
for filling in missing values in matrices using low-rank approximation.
This approach is the foundation of many **recommender systems** like
Netflix and Amazon product recommendations.

You will work with a synthetic **user-movie rating matrix** that mimics
real recommender system data, with most entries missing. You will:

- Understand the structure of sparse rating matrices
- Implement mean imputation as a baseline
- Use SVD for low-rank matrix approximation
- Build an iterative matrix completion algorithm
- Evaluate imputation quality using held-out validation
- Apply your methods to predict user preferences

These skills are essential for building recommendation engines,
handling missing data in machine learning pipelines, and understanding
the connection between SVD/PCA and matrix factorization.
#########






import pathlib
from typing import Tuple, Dict, List, Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import svd

RANDOM_STATE: int = 42
np.random.seed(RANDOM_STATE)

_DATA_PATH = pathlib.Path("ratings.csv")
if not _DATA_PATH.exists():
    raise FileNotFoundError(
        "ratings.csv is missing from the lab directory. Please run the download "
        "script (w5_download_datasets.py) or ask the TA for assistance."
    )
