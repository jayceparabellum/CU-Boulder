4. Fit PCA Model (10 points)
Now we're ready to apply PCA to the standardized data. PCA will find the directions (principal components) that capture the most variance in the data.

Fit a PCA model to the standardized data. Keep all components for now so we can analyze how much variance each captures.

Store the results as:

q4_pca: The fitted PCA object
q4_n_components: The number of components in the fitted model (should equal n_features)
q4_explained_variance_ratio: A numpy array of the variance ratio explained by each component


# Grade Cell: Question 4
#
# Task: Fit a PCA model to the standardized data
#
# Instructions:
# 1. Create a PCA instance (without specifying n_components to keep all)
# 2. Fit the PCA model to q3_scaled_data
# 3. Access the explained_variance_ratio_ attribute

q4_pca = PCA(random_state=RANDOM_STATE)
q4_pca.fit(q3_scaled_data)

q4_n_components: int = q4_pca.n_components_
q4_explained_variance_ratio = q4_pca.explained_variance_ratio_

print(f"Number of components: {q4_n_components}")
print(f"Variance explained by each component:")
for i, var in enumerate(q4_explained_variance_ratio):
    print(f"  PC{i+1}: {var:.4f} ({var*100:.2f}%)")
