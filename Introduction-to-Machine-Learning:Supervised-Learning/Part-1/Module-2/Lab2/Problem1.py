def load_auto_data() -> pd.DataFrame:
    """Load the Auto dataset from ``auto.csv``.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the auto dataset.
    """
    return pd.read_csv(_DATA_PATH)
    raise NotImplementedError


# Compute the answer required by the autograder
q1_shape: Tuple[int, int] = load_auto_data().shape
print(f"Dataset shape: {q1_shape}")
