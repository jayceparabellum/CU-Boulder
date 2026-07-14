5. Analyze Variance Explained (10 points)
A key step in PCA is understanding how much variance each component captures. The scree plot shows individual variance explained, while the cumulative variance plot helps determine how many components to keep.

Compute:

q5_pve: A list of individual Proportion of Variance Explained (PVE) for each component, rounded to 3 decimals
q5_cumulative_pve: A list of cumulative PVE, rounded to 3 decimals
q5_pc1_pc2_total: The total variance explained by PC1 and PC2 combined (float, rounded to 3 decimals)


# Grade Cell: Question 5
#
# Task: Compute individual and cumulative variance explained
#
# Instructions:
# 1. Use q4_explained_variance_ratio to get individual PVE
# 2. Use np.cumsum() to compute cumulative PVE
# 3. Round values to 3 decimal places
# 4. Compute the sum of PC1 and PC2 variance

q5_pve: List[float] = [round(float(v), 3) for v in q4_explained_variance_ratio]

q5_cumulative_pve: List[float] = [
    round(float(v), 3) for v in np.cumsum(q4_explained_variance_ratio)
]

q5_pc1_pc2_total: float = round(
    float(q4_explained_variance_ratio[0] + q4_explained_variance_ratio[1]), 3
)

print(f"Individual PVE: {q5_pve}")
print(f"Cumulative PVE: {q5_cumulative_pve}")
print(f"PC1 + PC2 explain {q5_pc1_pc2_total*100:.1f}% of total variance")
