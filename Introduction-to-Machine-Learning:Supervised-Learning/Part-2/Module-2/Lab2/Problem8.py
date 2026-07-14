Now let's transform the standardized data to principal component space. This gives us the scores - the coordinates of each observation in the new PC coordinate system.

Transform the data and store in a DataFrame for easier analysis.

Store the results as:

q8_scores: A numpy array of shape (n_samples, n_components) with the transformed data
q8_scores_df: A pandas DataFrame with the scores, with columns named "PC1", "PC2", etc.
q8_pc1_range: A tuple (min, max) of PC1 scores (values rounded to 2 decimals)


# Grade Cell: Question 8
#
# Task: Transform data to principal component space
#
# Instructions:
# 1. Use pca.transform() on the standardized data
# 2. Create a DataFrame with column names "PC1", "PC2", etc.
# 3. Find the range (min, max) of PC1 scores

q8_scores = q4_pca.transform(q3_scaled_data)

pc_columns = [f"PC{i + 1}" for i in range(q8_scores.shape[1])]
q8_scores_df = pd.DataFrame(q8_scores, columns=pc_columns)

q8_pc1_range: Tuple[float, float] = (
    round(float(q8_scores_df["PC1"].min()), 2),
    round(float(q8_scores_df["PC1"].max()), 2),
)

print(f"Scores shape: {q8_scores.shape}")
print(f"DataFrame columns: {list(q8_scores_df.columns[:5])}...")
print(f"PC1 range: {q8_pc1_range}")
