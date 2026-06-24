

def load_housing() -> pd.DataFrame:
    """Load the California Housing data from ``california_housing.csv``.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the 8 predictors plus the target column ``MedHouseVal``.
    """
    #####personal code below this line####
    return pd.read_csv(_DATA_PATH)
    #####Personal code ends above this line####


# Compute the answer required by the autograder
q1_shape: Tuple[int, int] = load_housing().shape
print(f"Dataset shape: {q1_shape}")

