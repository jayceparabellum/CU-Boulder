7. Examine Loadings (10 points)
Loadings tell us how each original feature contributes to each principal component. By examining loadings, we can interpret what each PC represents.

For PC1 and PC2:

Find the features with the largest absolute loadings
These are the features that drive each component
Store the results as:

q7_loadings: A numpy array of shape (n_components, n_features) containing all loadings
q7_pc1_top_feature: The name of the feature with the largest absolute loading on PC1
q7_pc2_top_feature: The name of the feature with the largest absolute loading on PC2
q7_pc1_top_loading: The loading value of the top feature on PC1 (rounded to 3 decimals)

# Grade Cell: Question 7
#
# Task: Examine and interpret PCA loadings
#
# Instructions:
# 1. Access the loadings from pca.components_
# 2. For PC1 (index 0), find the feature with largest |loading|
# 3. For PC2 (index 1), find the feature with largest |loading|
# 4. Use q1_columns to get feature names

q7_loadings = q4_pca.components_

feature_names = q1_columns

pc1_loadings = q7_loadings[0]
pc1_top_idx = int(np.argmax(np.abs(pc1_loadings)))
q7_pc1_top_feature: str = feature_names[pc1_top_idx]
q7_pc1_top_loading: float = round(float(pc1_loadings[pc1_top_idx]), 3)

pc2_loadings = q7_loadings[1]
pc2_top_idx = int(np.argmax(np.abs(pc2_loadings)))
q7_pc2_top_feature: str = feature_names[pc2_top_idx]

print(f"Loadings shape: {q7_loadings.shape}")
print(f"PC1 top feature: {q7_pc1_top_feature} (loading {q7_pc1_top_loading})")
print(f"PC2 top feature: {q7_pc2_top_feature}")
