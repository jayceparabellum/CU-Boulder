10. PCA for Reconstruction (10 points)
A key property of PCA is that we can reconstruct the original data from the principal components. Using fewer components gives an approximation.

The reconstruction error tells us how much information is lost when we reduce dimensionality.

Implement a function to:

Transform data to PC space using only k components
Reconstruct (inverse transform) back to original feature space
Compute the Mean Squared Error (MSE) between original and reconstructed data
Store the results as:

q10_reconstruction_error: A function that takes k and returns MSE (rounded to 4 decimals)
q10_mse_all_components: MSE when using all components (should be ~0)
q10_mse_2_components: MSE when using only 2 components
q10_mse_5_components: MSE when using 5 components (our 80% threshold)


# Grade Cell: Question 10
#
# Task: Implement PCA reconstruction and compute reconstruction error
#
# Instructions:
# 1. Create a function that fits PCA with k components and computes reconstruction MSE
# 2. MSE = mean((original - reconstructed)^2)
# 3. Compute MSE for all components, 2 components, and 5 components

def q10_reconstruction_error(k: int) -> float:
    """Fit PCA with k components, reconstruct, return MSE (4 decimals)."""
    pca_k = PCA(n_components=k, random_state=RANDOM_STATE)
    scores_k = pca_k.fit_transform(q3_scaled_data)
    reconstructed = pca_k.inverse_transform(scores_k)
    mse = np.mean((q3_scaled_data - reconstructed) ** 2)
    return round(float(mse), 4)

q10_mse_all_components: float = q10_reconstruction_error(q3_scaled_data.shape[1])
q10_mse_2_components: float = q10_reconstruction_error(2)
q10_mse_5_components: float = q10_reconstruction_error(5)

print(f"Reconstruction MSE with all components: {q10_mse_all_components}")
print(f"Reconstruction MSE with 2 components: {q10_mse_2_components}")
print(f"Reconstruction MSE with 5 components: {q10_mse_5_components}")
