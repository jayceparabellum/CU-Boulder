# Grade Cell: Question 8
#
# Task: Visualize clusters using PCA projection
#
# Instructions:
# 1. Fit PCA with n_components=2 to the standardized data
# 2. Transform the data to 2D
# 3. Create a scatter plot colored by cluster labels
# 4. Compute total variance explained by the 2 PCs

q8_pca = PCA(n_components=2, random_state=RANDOM_STATE)
q8_pca_data = q8_pca.fit_transform(q2_scaled_data)

q8_variance_explained: float = round(float(q8_pca.explained_variance_ratio_.sum()), 3)

km = KMeans(n_clusters=q6_chosen_k, random_state=RANDOM_STATE, n_init=10)
cluster_labels = km.fit_predict(q2_scaled_data)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    q8_pca_data[:, 0], q8_pca_data[:, 1],
    c=cluster_labels, cmap="viridis", alpha=0.7, edgecolor="k"
)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title(f"Iris Clusters in PCA Space (K={q6_chosen_k})")
plt.colorbar(scatter, label="Cluster")
plt.tight_layout()
plt.show()

q8_plot_created: bool = True

print(f"PCA data shape: {q8_pca_data.shape}")
print(f"Variance explained by 2 PCs: {q8_variance_explained*100:.1f}%")
