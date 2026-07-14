9. Visualize PCA Results (10 points)
One of PCA's most powerful uses is visualization. By plotting PC1 vs PC2, we can see structure in high-dimensional data that would otherwise be invisible.

Create a function to plot PC1 vs PC2 scores, and identify observations that are outliers (far from the center in PC space).

Store the results as:

q9_plot_created: Set to True after creating the scatter plot
q9_pc1_pc2_corr: The correlation between PC1 and PC2 scores (should be ~0 since PCs are orthogonal)
q9_furthest_from_origin: Index of the sample furthest from origin in PC1-PC2 space


# Grade Cell: Question 9
#
# Task: Visualize PCA results and identify outliers
#
# Instructions:
# 1. Create a scatter plot of PC1 vs PC2
# 2. Calculate correlation between PC1 and PC2 scores
# 3. Find the sample furthest from origin (largest sqrt(PC1^2 + PC2^2))

plt.figure(figsize=(8, 6))
plt.scatter(q8_scores_df["PC1"], q8_scores_df["PC2"], alpha=0.7, edgecolor="k")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Wine Data in PC1–PC2 Space")
plt.axhline(0, color="gray", lw=0.5)
plt.axvline(0, color="gray", lw=0.5)
plt.tight_layout()
plt.show()

q9_plot_created: bool = True

q9_pc1_pc2_corr: float = round(
    float(np.corrcoef(q8_scores_df["PC1"], q8_scores_df["PC2"])[0, 1]), 6
)

distances = np.sqrt(q8_scores_df["PC1"] ** 2 + q8_scores_df["PC2"] ** 2)
q9_furthest_from_origin: int = int(distances.idxmax())

print(f"PC1–PC2 correlation: {q9_pc1_pc2_corr}")
print(f"Furthest sample index: {q9_furthest_from_origin}")
