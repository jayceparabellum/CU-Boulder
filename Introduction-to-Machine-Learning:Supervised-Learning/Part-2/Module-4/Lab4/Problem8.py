8. Visualize Clusters in PCA Space (10 points)
Since our data has 4 features, we can use PCA to project the data to 2 dimensions for visualization. Color the points by their hierarchical cluster assignments.

Store the results as:

q8_pca: A fitted PCA object with 2 components
q8_pca_data: A numpy array of shape (n_samples, 2) with the projected data
q8_variance_explained: Total variance explained by 2 PCs (float, rounded to 3 decimals)
q8_plot_created: Set to True after creating the scatter plot
# Grade Cell: Question 8
#
# Task: Visualize hierarchical clusters using PCA projection
#
# Instructions:
# 1. Fit PCA with n_components=2 to the standardized data
# 2. Transform the data to 2D
# 3. Create a scatter plot colored by cluster labels (q6_labels)
# 4. Compute total variance explained by the 2 PCs
​
q8_pca = PCA(n_components=2, random_state=RANDOM_STATE)
q8_pca_data = q8_pca.fit_transform(q2_scaled_data)
​
q8_variance_explained: float = round(float(q8_pca.explained_variance_ratio_.sum()), 3)
​
plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    q8_pca_data[:, 0], q8_pca_data[:, 1],
    c=q6_labels, cmap="viridis", alpha=0.7, edgecolor="k"
)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Hierarchical Clusters in PCA Space (Complete Linkage, K=3)")
plt.colorbar(scatter, label="Cluster")
plt.tight_layout()
plt.show()
​
q8_plot_created: bool = True
​
print(f"PCA data shape: {q8_pca_data.shape}")
print(f"Variance explained by 2 PCs: {q8_variance_explained*100:.1f}%")
